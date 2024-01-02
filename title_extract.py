import PyPDF2

def extract_titles_from_pdf(pdf_path):
    titles = []
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            
            # Implement your title/subtitle extraction logic here
            
            # For example, extracting lines in uppercase as potential titles
            lines = text.split('\n')
            potential_titles = [line.strip() for line in lines if line.isupper()]
            titles.extend(potential_titles)
    
    return titles

# Usage
pdf_path = r'C:\Users\ACER\Desktop\Minor Project\Presentify\FormulaEncyclopedia-Proposal.pdf'
extracted_titles = extract_titles_from_pdf(pdf_path)
num = '0123456789'
for i in range(0,len(extracted_titles)):
    if '.' in extracted_titles[i]:
        extracted_titles[i]= extracted_titles[i].replace(".","")
    extracted_titles[i] = ''.join(char for char in extracted_titles[i] if char.isalpha() or char == " ").strip()
print(extracted_titles)
