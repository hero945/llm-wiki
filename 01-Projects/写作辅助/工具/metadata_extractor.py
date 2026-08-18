"""
ICH M11 方案摘要元数据提取器
支持：规则提取 + LLM 增强（预留接口）
"""

import json
import re
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional


class MetadataExtractor:
    """从方案摘要文本中提取结构化元数据"""

    def __init__(self, schema_path: str, use_llm: bool = False):
        self.schema_path = Path(schema_path)
        self.schema = self._load_schema()
        self.use_llm = use_llm
        self.issues = []

    def _load_schema(self) -> Dict[str, Any]:
        """加载元数据 Schema"""
        with open(self.schema_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def extract_from_text(self, text: str, source: str = "unknown") -> Dict[str, Any]:
        """从文本中提取元数据"""
        text = self._preprocess(text)

        result = {
            "trial_identification": self._extract_identification(text),
            "objectives": self._extract_objectives(text),
            "design": self._extract_design(text),
            "population": self._extract_population(text),
            "interventions": self._extract_interventions(text),
            "endpoints": self._extract_endpoints(text),
            "statistics": self._extract_statistics(text),
            "schedule": self._extract_schedule(text),
            "safety": self._extract_safety(text),
            "ethics_regulatory": self._extract_ethics(text),
            "extraction_meta": {
                "source": source,
                "extraction_method": "rule_based",
                "extraction_date": datetime.now().isoformat(),
                "issues": self.issues
            }
        }

        # 如果启用 LLM，用 LLM 补充复杂字段
        if self.use_llm:
            result = self._llm_enhance(text, result)
            result["extraction_meta"]["extraction_method"] = "hybrid"

        return result

    def extract_from_file(self, file_path: str) -> Dict[str, Any]:
        """从文件中提取元数据"""
        path = Path(file_path)
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        return self.extract_from_text(text, source=str(path))

    def _preprocess(self, text: str) -> str:
        """文本预处理"""
        # 统一换行符
        text = text.replace('\r\n', '\n').replace('\r', '\n')
        # 移除多余空行
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text

    # ==================== 各字段提取规则 ====================

    def _extract_identification(self, text: str) -> Dict[str, Any]:
        """提取试验标识信息"""
        result = {}

        # 完整标题
        title_match = re.search(
            r'(?:完整标题|试验标题|研究标题|标题)[：:]\s*(.+?)(?:\n|$)',
            text, re.IGNORECASE
        )
        if title_match:
            result["full_title"] = title_match.group(1).strip()

        # 短标题
        short_title_match = re.search(
            r'短标题[：:]\s*(.+?)(?:\n|$)',
            text, re.IGNORECASE
        )
        if short_title_match:
            result["short_title"] = short_title_match.group(1).strip()

        # 方案编号
        protocol_match = re.search(
            r'(?:方案编号|研究编号|Protocol Number|Protocol No)[：:]\s*([A-Za-z0-9\-_]+)',
            text, re.IGNORECASE
        )
        if protocol_match:
            result["protocol_number"] = protocol_match.group(1).strip()

        # 分期
        phase_match = re.search(
            r'([IⅠ]+/?[IⅡ]+/?[IⅢ]+/?[IVⅣ]+)\s*期?临床',
            text, re.IGNORECASE
        )
        if phase_match:
            phase_str = phase_match.group(1).upper()
            phase_map = {
                'I': 'I', 'Ⅰ': 'I',
                'II': 'II', 'Ⅱ': 'II',
                'III': 'III', 'Ⅲ': 'III',
                'IV': 'IV', 'Ⅳ': 'IV',
                'I/II': 'I/II', 'Ⅰ/Ⅱ': 'I/II',
                'II/III': 'II/III', 'Ⅱ/Ⅲ': 'II/III'
            }
            result["phase"] = phase_map.get(phase_str, phase_str)

        # 适应症
        indication_match = re.search(
            r'(?:治疗|用于|在)([^\n，。]{3,30})(?:患者|受试者|人群)',
            text
        )
        if indication_match:
            result["indication"] = indication_match.group(1).strip()
        elif "full_title" in result:
            # 从标题中提取适应症
            title = result["full_title"]
            ind_match = re.search(r'在(.+?)患者', title)
            if ind_match:
                result["indication"] = ind_match.group(1).strip()

        # 治疗领域
        if "indication" in result:
            indication = result["indication"]
            if any(k in indication for k in ["银屑病", "湿疹", "皮炎", "白癜风"]):
                result["therapeutic_area"] = "皮肤科"
            elif any(k in indication for k in ["肺癌", "乳腺癌", "肿瘤", "癌"]):
                result["therapeutic_area"] = "肿瘤"
            elif any(k in indication for k in ["类风湿", "强直性脊柱炎", "银屑病关节炎"]):
                result["therapeutic_area"] = "风湿免疫"

        return result

    def _extract_objectives(self, text: str) -> Dict[str, Any]:
        """提取试验目的"""
        result = {}

        # 主要目的
        primary_match = re.search(
            r'主要目的[：:]\s*(.+?)(?=\n\s*(?:次要目的|主要终点|2\.|二、))',
            text, re.DOTALL | re.IGNORECASE
        )
        if primary_match:
            primary_desc = self._clean_text(primary_match.group(1))
            result["primary"] = [{
                "description": primary_desc,
                "endpoint": self._extract_primary_endpoint(text)
            }]

        # 次要目的
        secondary_match = re.search(
            r'次要目的[：:]\s*(.+?)(?=\n\s*(?:次要终点|探索性目的|3\.|三、))',
            text, re.DOTALL | re.IGNORECASE
        )
        if secondary_match:
            secondary_desc = self._clean_text(secondary_match.group(1))
            result["secondary"] = [{
                "description": secondary_desc,
                "endpoint": "见次要终点"
            }]

        # 探索性目的
        exploratory_match = re.search(
            r'探索性目的[：:]\s*(.+?)(?=\n\s*(?:\d+\.|$))',
            text, re.DOTALL | re.IGNORECASE
        )
        if exploratory_match:
            exploratory_desc = self._clean_text(exploratory_match.group(1))
            result["exploratory"] = [{
                "description": exploratory_desc
            }]

        return result

    def _extract_primary_endpoint(self, text: str) -> str:
        """提取主要终点"""
        endpoint_match = re.search(
            r'主要终点[：:]\s*(.+?)(?=\n\s*(?:次要终点|次要目的|3\.|三、))',
            text, re.DOTALL | re.IGNORECASE
        )
        if endpoint_match:
            return self._clean_text(endpoint_match.group(1))
        return ""

    def _extract_design(self, text: str) -> Dict[str, Any]:
        """提取试验设计"""
        result = {
            "study_type": "干预性"
        }

        # 设计模式
        design_text = text
        if "平行组" in design_text or "平行" in design_text:
            result["design_pattern"] = "平行组"
        elif "交叉" in design_text:
            result["design_pattern"] = "交叉设计"
        elif "析因" in design_text:
            result["design_pattern"] = "析因设计"
        elif "单组" in design_text or "开放单臂" in design_text:
            result["design_pattern"] = "单组"
        elif "适应性" in design_text or "自适应" in design_text:
            result["design_pattern"] = "适应性设计"
        elif "主方案" in design_text:
            result["design_pattern"] = "主方案"
        else:
            result["design_pattern"] = "其他"

        # 盲法
        if "双盲" in design_text:
            result["blinding"] = "双盲"
        elif "单盲" in design_text:
            result["blinding"] = "单盲"
        elif "开放" in design_text or "开放标签" in design_text:
            result["blinding"] = "开放"
        elif "三盲" in design_text:
            result["blinding"] = "三盲"

        # 随机化
        result["randomization"] = {
            "yes_no": "随机" in design_text,
            "method": None,
            "stratification": []
        }
        if "分层" in design_text:
            # 尝试匹配 "按因素A、因素B分层" 或 "按因素A分层"
            strat_match = re.search(r'按\s*([^\n，。]{1,20}?)\s*分层', design_text)
            if strat_match:
                factors_text = strat_match.group(1).strip()
                # 排除统计方法描述和无效匹配
                invalid_keywords = ['检验', '校正', '因素', '随机化']
                if (len(factors_text) <= 30 and
                    not any(kw in factors_text for kw in invalid_keywords) and
                    factors_text not in ['随机化', '主要终点分析']):
                    factors = [f.strip() for f in re.split(r'[、,，和与]', factors_text) if f.strip()]
                    result["randomization"]["stratification"] = factors
                else:
                    result["randomization"]["stratification"] = []
            else:
                result["randomization"]["stratification"] = []

        # 对照类型
        if "安慰剂对照" in design_text or "安慰剂" in design_text:
            result["control_type"] = "安慰剂"
        elif "阳性对照" in design_text or "活性对照" in design_text:
            result["control_type"] = "阳性对照"
        elif "标准治疗" in design_text:
            result["control_type"] = "标准治疗"
        elif "低剂量" in design_text:
            result["control_type"] = "低剂量对照"
        elif "无对照" in design_text or "单臂" in design_text:
            result["control_type"] = "无对照"
        else:
            result["control_type"] = "其他"

        # 组数
        arm_match = re.search(r'(\d+)\s*个(?:治疗|剂量|干预|试验|研究)?组', design_text)
        if arm_match:
            result["number_of_arms"] = int(arm_match.group(1))
        else:
            # 尝试从 1:1:1 推断
            ratio_match = re.search(r'(\d+):(\d+)(?::(\d+))?', design_text)
            if ratio_match:
                result["number_of_arms"] = sum(1 for g in ratio_match.groups() if g)

        # 样本量
        sample_match = re.search(r'(?:入组|纳入|计划)\s*约?\s*(\d+)\s*例', design_text)
        if sample_match:
            result["sample_size"] = {
                "total": int(sample_match.group(1))
            }

        # 时间
        result["duration"] = {}
        screening_match = re.search(r'筛选期(?:最长)?\s*(\d+)\s*周', design_text)
        if screening_match:
            result["duration"]["screening"] = f"最长 {screening_match.group(1)} 周"

        treatment_match = re.search(r'治疗期\s*(\d+)\s*周', design_text)
        if treatment_match:
            result["duration"]["treatment"] = f"{treatment_match.group(1)} 周"

        followup_match = re.search(r'(?:治疗后随访期|随访期)\s*(\d+)\s*周', design_text)
        if followup_match:
            result["duration"]["follow_up"] = f"{followup_match.group(1)} 周"

        total_match = re.search(r'总持续时间(?:最长)?\s*约?\s*(\d+)\s*周', design_text)
        if total_match:
            result["duration"]["total_per_participant"] = f"最长 {total_match.group(1)} 周"

        return result

    def _extract_population(self, text: str) -> Dict[str, Any]:
        """提取试验人群"""
        result = {}

        # 诊断
        diag_match = re.search(
            r'诊断为(中重度[^\n，。]{2,20})(?:，|患者|受试者)',
            text
        )
        if diag_match:
            result["diagnosis"] = diag_match.group(1).strip()
        elif "indication" in (self._extract_identification(text) or {}):
            result["diagnosis"] = self._extract_identification(text).get("indication", "")

        # 年龄范围
        age_match = re.search(r'(\d+)\s*[-~至]\s*(\d+)\s*周岁?', text)
        if age_match:
            result["age_range"] = {
                "min": int(age_match.group(1)),
                "max": int(age_match.group(2)),
                "unit": "岁"
            }

        # 性别
        if "男女不限" in text:
            result["gender"] = "男女不限"
        elif "男性" in text and "女性" not in text:
            result["gender"] = "男性"
        elif "女性" in text and "男性" not in text:
            result["gender"] = "女性"

        # 入排标准
        result["key_inclusion_criteria"] = self._extract_list_section(
            text, "关键入选标准", "关键排除标准"
        )
        result["key_exclusion_criteria"] = self._extract_list_section(
            text, "关键排除标准", r'(?:\d+\.|$)'
        )

        return result

    def _extract_interventions(self, text: str) -> List[Dict[str, Any]]:
        """提取试验干预"""
        interventions = []

        # 找到"试验干预"章节
        section_match = re.search(
            r'(?:5|试验干预|5\.\s*试验干预)\s*[\n:]\s*(.+?)(?=\n\s*(?:6|统计考虑|安全性评估|7|目标人群|4|目标人群|伦理与监管|$))',
            text, re.DOTALL | re.IGNORECASE
        )
        if not section_match:
            return interventions

        section_text = section_match.group(1)
        # 按行分割，每行描述一个干预组
        lines = [line.strip() for line in section_text.split('\n') if line.strip()]

        for line in lines:
            intervention = self._parse_intervention_line(line)
            if intervention:
                interventions.append(intervention)

        return interventions

    def _parse_intervention_line(self, line: str) -> Optional[Dict[str, Any]]:
        """解析单个干预组描述行"""
        # 格式1: 组名：药物名 剂量 mg，给药途径，频率/时间点
        # 格式2: 组名：药物名，给药途径，按相同时间点给药
        # 格式3: 安慰剂组：安慰剂，给药途径，频率

        # 先匹配组名
        group_match = re.match(r'([^：:]+组)[：:]\s*(.+)', line)
        if not group_match:
            return None

        group_name = group_match.group(1).strip()
        content = group_match.group(2).strip()

        intervention_type = "试验药物"
        drug_name = None
        dosage = None
        route = None
        frequency = None
        duration = None

        # 判断是否安慰剂
        if "安慰剂" in group_name or "安慰剂" in content:
            intervention_type = "安慰剂"
            drug_name = "安慰剂"
            dosage = "不适用"
        else:
            # 提取药物名和剂量
            # 模式：药物名 剂量 mg
            dose_match = re.search(r'([^，,]+?)\s*(\d+(?:\.\d+)?)\s*mg?\b', content, re.IGNORECASE)
            if dose_match:
                drug_name = dose_match.group(1).strip()
                dosage = f"{dose_match.group(2)} mg"
            else:
                # 没有剂量，可能是生物制剂按固定剂量
                drug_match = re.match(r'([^，,]+?)[，,]', content)
                if drug_match:
                    drug_name = drug_match.group(1).strip()
                    dosage = "见方案详情"

        # 提取给药途径
        route_keywords = ['皮下注射', '静脉输注', '口服', '吸入', '肌肉注射', '皮内注射', '局部用药', '滴眼']
        for keyword in route_keywords:
            if keyword in content:
                route = keyword
                break

        # 提取给药频率
        freq_match = re.search(r'每\s*(\d+)\s*周一次|每日一次|每日两次|每周一次|每月一次|单次', content)
        if freq_match:
            if freq_match.group(1):
                frequency = f"每 {freq_match.group(1)} 周一次"
            else:
                frequency = freq_match.group(0)

        # 提取持续时间
        duration_match = re.search(r'共\s*(\d+)\s*周|第\s*0\s*周单次', content)
        if duration_match:
            if '单次' in duration_match.group(0):
                duration = "单次给药"
            else:
                duration = f"共 {duration_match.group(1)} 周"

        # 如果没有任何有效信息，返回 None
        if not drug_name and not route:
            return None

        return {
            "name": drug_name or "未识别",
            "type": intervention_type,
            "dosage": dosage or "未识别",
            "route": route or "未识别",
            "frequency": frequency or "未识别",
            "duration": duration or "未识别"
        }

    def _extract_endpoints(self, text: str) -> Dict[str, Any]:
        """提取终点"""
        result = {}

        # 主要终点
        primary_endpoint = self._extract_primary_endpoint(text)
        if primary_endpoint:
            result["primary"] = [{
                "name": primary_endpoint,
                "timepoint": self._extract_timepoint(primary_endpoint),
                "assessment": self._extract_assessment(primary_endpoint)
            }]

        # 次要终点
        secondary_match = re.search(
            r'次要终点[：:]\s*(.+?)(?=\n\s*(?:\d+\.\s+|\d+、|[一二三四五六七八九十]+、|探索性目的|统计考虑|安全性评估|伦理与监管|$))',
            text, re.DOTALL | re.IGNORECASE
        )
        if secondary_match:
            secondary_text = secondary_match.group(1)
            # 提取列表项
            items = re.findall(r'[\-\•]\s*(.+?)(?=\n[\-\•]|\n\n|$)', secondary_text, re.DOTALL)
            result["secondary"] = []
            for item in items:
                clean_item = self._clean_text(item)
                if clean_item:
                    result["secondary"].append({
                        "name": clean_item,
                        "timepoint": self._extract_timepoint(clean_item),
                        "assessment": self._extract_assessment(clean_item)
                    })

        return result

    def _extract_statistics(self, text: str) -> Dict[str, Any]:
        """提取统计考虑"""
        result = {}

        alpha_match = re.search(r'[αa]\s*=\s*([0-9.]+)\s*\(?双?侧?\)?', text, re.IGNORECASE)
        if alpha_match:
            result["alpha"] = float(alpha_match.group(1))

        power_match = re.search(r'把握度\s*(\d+)\s*%', text)
        if power_match:
            result["power"] = int(power_match.group(1)) / 100

        method_match = re.search(r'主要终点分析采用(.+?)(?:[。\n]|,)', text)
        if method_match:
            result["primary_analysis_method"] = method_match.group(1).strip()

        missing_match = re.search(r'缺失数据采用(.+?)(?:[。\n]|,)', text)
        if missing_match:
            result["missing_data_handling"] = missing_match.group(1).strip()

        multi_match = re.search(r'多重性(?:调整|校正)?采用(.+?)(?:[。\n]|,)', text)
        if multi_match:
            result["multiplicity_adjustment"] = multi_match.group(1).strip()

        return result

    def _extract_schedule(self, text: str) -> Dict[str, Any]:
        """提取时间与访视"""
        result = {}

        # 从主要和次要终点中提取关键评估时间点
        key_assessments = []

        # PASI 评估
        pas_time = self._extract_timepoint_from_text(text, "PASI")
        if pas_time:
            key_assessments.append({
                "assessment": "PASI",
                "timepoints": [pas_time]
            })

        # sPGA 评估
        spga_time = self._extract_timepoint_from_text(text, "sPGA")
        if spga_time:
            key_assessments.append({
                "assessment": "sPGA",
                "timepoints": [spga_time]
            })

        # DLQI 评估
        dlqi_time = self._extract_timepoint_from_text(text, "DLQI")
        if dlqi_time:
            key_assessments.append({
                "assessment": "DLQI",
                "timepoints": [dlqi_time]
            })

        # 通用：提取所有 "第 X 周 评估 Y" 模式
        assessment_pattern = r'第\s*(\d+)\s*周\s*([^，。\n]{2,30}?)(?:评估|检查|测定|评分)'
        for match in re.finditer(assessment_pattern, text):
            timepoint = f"第 {match.group(1)} 周"
            assessment = match.group(2).strip()
            # 合并同一评估的不同时间点
            existing = next((a for a in key_assessments if a["assessment"] == assessment), None)
            if existing:
                if timepoint not in existing["timepoints"]:
                    existing["timepoints"].append(timepoint)
            else:
                key_assessments.append({
                    "assessment": assessment,
                    "timepoints": [timepoint]
                })

        if key_assessments:
            result["key_assessments"] = key_assessments

        return result

    def _extract_safety(self, text: str) -> Dict[str, Any]:
        """提取安全性信息"""
        result = {}

        if "独立的数据监查委员会" in text or "DMC" in text:
            result["data_monitoring_committee"] = True

        ae_match = re.search(r'(?:研究期间|试验期间|治疗后随访期)([^。]+?收集不良事件)', text)
        if ae_match:
            result["ae_collection_period"] = ae_match.group(0).strip()

        return result

    def _extract_ethics(self, text: str) -> Dict[str, Any]:
        """提取伦理与监管信息"""
        result = {}

        if "伦理委员会批准" in text or "IRB" in text or "IEC" in text:
            result["irb_iec_required"] = True

        if "签署书面知情同意书" in text or "知情同意" in text:
            result["informed_consent_required"] = True

        if "数据监查委员会" in text or "DMC" in text:
            result["data_monitoring_committee"] = True

        return result

    # ==================== 工具方法 ====================

    def _clean_text(self, text: str) -> str:
        """清理文本"""
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n+', ' ', text)
        return text

    def _extract_list_section(self, text: str, start_marker: str, end_marker: str) -> List[str]:
        """提取列表形式的章节内容"""
        pattern = f"{re.escape(start_marker)}[：:]\\s*(.+?)(?={end_marker})"
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if not match:
            return []

        section_text = match.group(1)
        # 提取列表项（支持 -、•、数字编号）
        items = re.findall(r'(?:[\-\•]\s*|\d+\.\s*)(.+?)(?=\n(?:[\-\•]|\d+\.)|\n\n|$)', section_text, re.DOTALL)
        return [self._clean_text(item) for item in items if self._clean_text(item)]

    def _extract_timepoint(self, text: str) -> Optional[str]:
        """从文本中提取时间点"""
        match = re.search(r'第\s*(\d+)\s*周', text)
        if match:
            return f"第 {match.group(1)} 周"
        return None

    def _extract_assessment(self, text: str) -> Optional[str]:
        """从文本中提取评估方法"""
        if "PASI" in text:
            return "银屑病面积和严重程度指数"
        if "sPGA" in text:
            return "静态医师整体评估"
        if "DLQI" in text:
            return "皮肤病生活质量指数"
        return None

    def _extract_timepoint_from_text(self, text: str, keyword: str) -> Optional[str]:
        """从包含关键词的句子中提取时间点"""
        pattern = f"{re.escape(keyword)}.{{0,30}}第\\s*(\\d+)\\s*周"
        match = re.search(pattern, text)
        if match:
            return f"第 {match.group(1)} 周"
        return None

    # ==================== LLM 增强接口（预留） ====================

    def _llm_enhance(self, text: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """使用 LLM 增强复杂字段的提取"""
        # TODO: 接入 Claude / GPT / 国产模型 API
        # 这里预留接口，当前版本仅做日志记录
        self.issues.append("LLM 增强尚未实现，当前使用规则提取")
        return result

    def save(self, result: Dict[str, Any], output_path: str):
        """保存提取结果到 JSON"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)


# ==================== 命令行入口 ====================

if __name__ == "__main__":
    import sys

    # 默认使用示例文件
    synopsis_file = "example_synopsis.txt"
    schema_file = "metadata_schema.yaml"
    output_file = "extracted_metadata.json"

    if len(sys.argv) > 1:
        synopsis_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    extractor = MetadataExtractor(schema_file)
    result = extractor.extract_from_file(synopsis_file)
    extractor.save(result, output_file)

    print("[OK] 元数据提取完成")
    print(f"来源：{synopsis_file}")
    print(f"输出：{output_file}")
    print("\n提取摘要：")
    print(f"- 试验标题：{result.get('trial_identification', {}).get('full_title', 'N/A')}")
    print(f"- 分期：{result.get('trial_identification', {}).get('phase', 'N/A')}")
    print(f"- 适应症：{result.get('trial_identification', {}).get('indication', 'N/A')}")
    print(f"- 设计：{result.get('design', {}).get('design_pattern', 'N/A')} / {result.get('design', {}).get('blinding', 'N/A')}")
    print(f"- 样本量：{result.get('design', {}).get('sample_size', {}).get('total', 'N/A')}")
    print(f"- 干预组数：{len(result.get('interventions', []))}")
    print(f"- 主要终点：{result.get('endpoints', {}).get('primary', [{}])[0].get('name', 'N/A')}")

    if result.get('extraction_meta', {}).get('issues'):
        print("\n[注意]")
        for issue in result['extraction_meta']['issues']:
            print(f"  - {issue}")
