from langchain_groq import ChatGroq
from pypdf import PdfReader
import pandas as pd
import re
import replicate
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()  # Ensure your .env file contains GROQ_API_KEY

# Extract Information from PDF file
def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract data from text using Groq
def extracted_data(pages_data):
    template = """Please Extract all the following values: invoice no., Description, Quantity, date, 
    Unit price, Amount, Total, email, phone number and address from this data: {pages}

    Expected output: remove any dollar symbols 
    {{'Invoice no.': '1001329','Description': 'Office Chair','Quantity': '2','Date': '5/4/2023',
    'Unit price': '1100.00','Amount': '2200.00','Total': '2200.00','Email': 'Santoshvarma0988@gmail.com',
    'Phone number': '9999999999','Address': 'Mumbai, India'}}
    """

    prompt_template = PromptTemplate(input_variables=["pages"], template=template)

    llm = ChatGroq(temperature=0.7, model="llama3-8b-8192", api_key=os.getenv("GROQ_API_KEY"))
    
    full_response = llm.invoke(prompt_template.format(pages=pages_data)).content

    return full_response

# Iterate over uploaded PDF files
def create_docs(user_pdf_list):
    df = pd.DataFrame({
        'Invoice no.': pd.Series(dtype='str'),
        'Description': pd.Series(dtype='str'),
        'Quantity': pd.Series(dtype='str'),
        'Date': pd.Series(dtype='str'),
        'Unit price': pd.Series(dtype='str'),
        'Amount': pd.Series(dtype='str'),
        'Total': pd.Series(dtype='str'),
        'Email': pd.Series(dtype='str'),
        'Phone number': pd.Series(dtype='str'),
        'Address': pd.Series(dtype='str')
    })

    for filename in user_pdf_list:
        print(f"Processing: {filename}")
        raw_data = get_pdf_text(filename)
        print("Extracted raw text from PDF.")

        llm_extracted_data = extracted_data(raw_data)
        print("Received structured data from LLM.")

        pattern = r'{(.+)}'
        match = re.search(pattern, llm_extracted_data, re.DOTALL)

        if match:
            extracted_text = match.group(1)
            try:
                data_dict = eval('{' + extracted_text + '}')
                print(data_dict)
            except Exception as e:
                print(f"Error parsing response: {e}")
                data_dict = {}
        else:
            print("No match found.")
            data_dict = {}

        df = df._append([data_dict], ignore_index=True)
        print("*DONE")

    return df