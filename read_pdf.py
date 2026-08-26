from pypdf import PdfReader
import sys

pdf_path = r'C:/Users/admin/Desktop/LLM-wiki/00-Inbox/松煊科技-临床试验垂域智能体.pdf'
reader = PdfReader(pdf_path)
print(f'共 {len(reader.pages)} 页')
print('=' * 60)

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        print(f'--- 第{i+1}页 ---')
        print(text)
        print()
