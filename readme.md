# Lead Generation Tool MVP

A Python-based lead generation pipeline that searches for professionals across various social platforms, scrapes their profile information, and uses AI to intelligently extract contact details like names, emails, and phone numbers.

> **Note:** This is a minimal MVP for one of our tools. For a complete and customized tool and services, contact [@ahamed_innovations](https://instagram.com/ahamed_innovations) on Instagram or visit [www.ahamedbasith.com](https://www.ahamedbasith.com). We will build complete solutions for you end-to-end.

## Features

- **Multi-Platform Search:** Automatically generates targeted Google search queries for LinkedIn, Facebook, Instagram, and Reddit.
- **Google Search Integration:** Uses SerpAPI to efficiently gather relevant profile links based on a target profession and location.
- **Asynchronous Scraping:** Fast, concurrent web scraping using `aiohttp` and `BeautifulSoup` to quickly parse page text while ignoring irrelevant scripts and styles.
- **AI-Powered Data Extraction:** Leverages Google's **Gemini 2.5 Flash** model in batch processing mode to intelligently extract structured lead data (Name, Company, Email, Phone) from raw, unstructured website text.
- **Fallback Regex Extraction:** Uses precise regular expressions to catch any emails or phone numbers the AI might miss.
- **Lead Scoring & Filtering:** Automatically scores leads based on data completeness (e.g., extra points for business emails). Low-quality leads without at least an email address are filtered out.
- **CSV Export:** Automatically deduplicates leads by email and saves the final output to a clean CSV file.

## Prerequisites

Before running this tool, you must obtain API keys for the following services:
- **SerpAPI:** For accessing Google Search results programmatically. ([Get an API Key](https://serpapi.com/))
- **Google Gemini API:** For intelligent text extraction via the `google-genai` SDK. ([Get an API Key](https://aistudio.google.com/app/apikey))

## Installation

1. Ensure you have **Python 3.8+** installed.
2. Clone this repository or download the source code.
3. *(Optional but highly recommended)* Create and activate a virtual environment:
   ```bash
   python -m venv env
   # On Windows:
   .\env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory of the project and add your API keys:

```env
SERP_API_KEY=your_serpapi_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

Run the main script to start the lead generation process:

```bash
python main.py
```

The script will interactively prompt you for a target profession and an optional location:
```
Enter profession: Real Estate Agent
Enter location (optional): Miami
```

The console will display the pipeline's progress as it builds queries, fetches links, scrapes content, and processes the text through Gemini AI.

## Output

Once the pipeline completes, the extracted leads will be saved to `outputs/leads.csv`. The CSV will contain the following columns:
- `name`: The contact's full name.
- `company`: The contact's associated company or organization.
- `url`: The source URL where the lead was found.
- `email`: The contact's email address.
- `phone`: The contact's phone number.
- `score`: An internal score denoting the completeness of the extracted lead data.
