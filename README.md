# Invoice Extraction Bot

**An AI-powered Streamlit application that extracts structured invoice data from PDF files using Groq's LLaMA-3 model.**

---

## Project Overview

This application simplifies the process of reading and extracting useful information from invoices in PDF format. By leveraging **LangChain** and **Groq's LLaMA-3**, the app intelligently identifies and extracts fields like:

* Invoice number
* Description
* Quantity
* Date
* Unit price
* Amount
* Total
* Email
* Phone number
* Address

Users can upload multiple invoices, and download the extracted data as a CSV.

---

## Features

* 📁 **Multiple PDF Uploads**: Upload several invoice PDFs in one go
* 🧹 **Smart Extraction**: Uses LLaMA-3 for precise field extraction
* 📄 **Download as CSV**: One-click export of cleaned invoice data
* 🌐 **Simple UI**: Clean and minimal Streamlit interface

---

## Tech Stack

* **Python 3.10+**
* [Streamlit](https://streamlit.io/) - Frontend framework
* [LangChain](https://www.langchain.com/) - LLM orchestration
* [Groq LLaMA-3](https://groq.com/) - High-speed LLM for data extraction
* [pypdf](https://pypi.org/project/pypdf/) - PDF reading and parsing
* [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable handling

---

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/thelakshyadubey/Invoice_Extraction_Bot.git
cd Invoice_Extraction_Bot
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables:

Create a `.env` file and add your Groq API key:

```env
REPLICATE_API_KEY=your_replicate_api_key
GROQ_API_KEY=your_groq_api_key_here
```

---

## Usage

1. Launch the application:

```bash
streamlit run app.py
```

2. In your browser:

   * Upload one or more PDF invoices
   * Click "Extract Data"
   * View and download structured CSV output

---

## Folder Structure

```text
invoice-extraction-bot/
├── app.py               # Streamlit application entry point
├── utils.py             # Core PDF & LLM logic
├── requirements.txt     # List of required packages
└── .env                 # (Not tracked) Contains your GROQ_API_KEY
```

---

## How It Works

1. **PDF Upload**: Upload one or more PDF invoices.
2. **Text Extraction**: Raw text is extracted using `pypdf`.
3. **LLM Query**: LangChain formats the data and queries Groq’s LLaMA-3 model for structured invoice extraction.
4. **CSV Output**: Results are shown on the screen and downloadable as CSV.

---

## Author

**Lakshya Dubey**
---

## Sample Output

```csv
Invoice no.,Description,Quantity,Date,Unit price,Amount,Total,Email,Phone number,Address
1001329,Office Chair,2,5/4/2023,1100.00,2200.00,2200.00,lakshya.dubey04@gmail.com,9999999999,Indore, India
```

---
## Preview
![image](https://github.com/user-attachments/assets/3fae0f2c-145a-455e-b459-19419588b7c1)
