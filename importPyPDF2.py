import re
import pdfplumber
import PyPDF2
import os

def extract_text_from_page(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        text = page.extract_text()
        return text

def find_name_and_employee_number(text):
    # 例として、氏名と従業員番号を抽出する正規表現パターンを定義します
    name_pattern = re.compile(r'氏名:\s*(\S+\S)')
    emp_number_pattern = re.compile(r'従業員番号:\s*(\d+)')

    name_match = name_pattern.search(text)
    emp_number_match = emp_number_pattern.search(text)

    name = name_match.group(1) if name_match else "Unknown"
    employee_number = emp_number_match.group(1) if emp_number_match else "0000"

    return name, employee_number

def split_pdf(input_pdf_path, output_dir):
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    num_pages = len(pdf_reader.pages)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_pages):
        text = extract_text_from_page(input_pdf_path, i)
        name, employee_number = find_name_and_employee_number(text)

        if name and employee_number:
            output_filename = f"{employee_number}_{name}.pdf"
        else:
            output_filename = f"page_{i + 1}.pdf"

        output_path = os.path.join(output_dir, output_filename)

        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[i])

        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        print(f"Saved page {i+1} as {output_filename}")

# 実行例
input_pdf_path = 'input.pdf'  # 読み込むPDFのパス
output_dir = 'output_pages'   # 出力ディレクトリ

split_pdf(input_pdf_path, output_dir)
