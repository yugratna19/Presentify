import PyPDF2
import re

def extract_titles_from_pdf(pdf_path):
    titles = []
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            
            # Implement your title/subtitle extraction logic here
            
            # For example, extracting lines in uppercase and considering bold texts
            lines = text.split('\n')
            potential_titles = [line.strip() for line in lines if line.isupper() or '**' in line]
            titles.extend(potential_titles)
    
    return titles

# Usage
pdf_path = r'FormulaEncyclopedia-Proposal.pdf'
extracted_titles = extract_titles_from_pdf(pdf_path)
item = ''
for titles in extracted_titles:
    item = item  + titles + '\n'
print(re.findall(r"\b[^\d\W_]+(?: [^\d\W_]+)*\b", item))
