# ==============================
# pdf_extractor.py
# ==============================

import pdfplumber
import re


# --------------------------------
# Extract complete text from PDF
# --------------------------------

def extract_pdf_text(pdf_file):

    text = ""

    try:

        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"


        return text.strip()


    except Exception as e:

        return f"PDF Error: {str(e)}"



# --------------------------------
# Extract Salary from PDF Text
# --------------------------------

def extract_salary(text):

    patterns = [
        r"salary\s*[:\-]?\s*(\d+)",
        r"net\s*salary\s*[:\-]?\s*(\d+)",
        r"basic\s*salary\s*[:\-]?\s*(\d+)",
        r"pay\s*[:\-]?\s*(\d+)"
    ]


    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return int(match.group(1))


    return None



# --------------------------------
# Extract Company Name
# --------------------------------

def extract_company(text):

    patterns = [
        r"company\s*name\s*[:\-]?\s*(.*)",
        r"employer\s*[:\-]?\s*(.*)",
        r"organization\s*[:\-]?\s*(.*)"
    ]


    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )


        if match:

            return match.group(1).strip()


    return "Not Found"



# --------------------------------
# Complete PDF Analysis
# --------------------------------

def analyze_pdf(pdf_file):


    text = extract_pdf_text(pdf_file)


    salary = extract_salary(text)


    company = extract_company(text)



    result = {

        "raw_text": text,

        "salary": salary,

        "company": company

    }


    return result