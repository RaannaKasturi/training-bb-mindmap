from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import requests
import re

def extract_pdf_text(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=50)
    texts = text_splitter.split_documents(pages)
    final_text = ""
    for text in texts:
        final_text = final_text + text.page_content
    return final_text

def generate_prompt(text):
    data = f'''
    Your output should use the language \"en\" and use the following template:
    # {{Title}} (should be the title of the research paper)
    ## {{Subtitle01}} (as required and as many as required in markdown format)
    - {{Emoji01}} Bulletpoint01 (as required and as many as required in markdown format)
        - {{Emoji01.1}} Bulletpoint01.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji01.1.1}} Bulletpoint01.1.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji01.1.2}} Bulletpoint01.1.2 (as required and as many as sub levels required in markdown format)
        - {{Emoji01.2}} Bulletpoint01.2 (as required and as many as sub levels required in markdown format)
    - {{Emoji02}} Bulletpoint02 (as required and as many as required in markdown format)
        - {{Emoji02.1}} Bulletpoint02.1 (as required and as many as sub levels required in markdown format)
        - {{Emoji02.2}} Bulletpoint02.2 (as required and as many as sub levels required in markdown format)
            - {{Emoji02.2.1}} Bulletpoint02.2.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji02.2.2}} Bulletpoint02.2.2 (as required and as many as sub levels required in markdown format)
            - {{Emoji02.2.3}} Bulletpoint02.2.3 (as required and as many as sub levels required in markdown format)
            - {{Emoji02.2.4}} Bulletpoint02.2.4 (as required and as many as sub levels required in markdown format)
    ## {{Subtitle02}} (as required and as many as required in markdown format)
    - {{Emoji03}} Bulletpoint03 (as required and as many as required in markdown format)
        - {{Emoji03.1}} Bulletpoint03.1 (as required and as many as sub levels required in markdown format)
        - {{Emoji03.2}} Bulletpoint03.2 (as required and as many as sub levels required in markdown format)
            - {{Emoji03.2.1}} Bulletpoint03.2.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji03.2.2}} Bulletpoint03.2.2 (as required and as many as sub levels required in markdown format)
    - {{Emoji04}} Bulletpoint04 (as required and as many as required in markdown format)
        - {{Emoji04.1}} Bulletpoint04.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji04.1.1}} Bulletpoint04.1.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji04.1.2}} Bulletpoint04.1.2 (as required and as many as sub levels required in markdown format)
        - {{Emoji04.2}} Bulletpoint04.2 (as required and as many as sub levels required in markdown format)
            - {{Emoji04.2.1}} Bulletpoint04.2.1 (as required and as many as sub levels required in markdown format)
            - {{Emoji04.2.2}} Bulletpoint04.2.2 (as required and as many as sub levels required in markdown format)
    Summarize the text \",'{text}'," to generate a concise mind map structure in markdown with as required and as many as levels and sub levels required to explain the entire research paper in markdown format using the \"en\" language.
    '''
    return data

def get_data(prompt):
    payload = {
        "text": prompt,
        "end_flag": True,
        "streaming": True,
        "model": "gpt-4o-mini"
    }
    url = (
        "https://api.journeydraw.ai/chatgpt/v3/question?app_id=nc_ai_ng&t=1731115757&nonce=51e10a96-bc6c-4de3-8eca-cc09d5e72c95&sign=6qipRqVyQMU2MFl0BHhKKIRO1bpqgWdsyoiHOWurgAg%2F31JS03%2FJ2sqow1RRO6PMyGSB9yi6X3YrzIOSAQ0B7WQBhIP%2FAe0OxuTKyocGOZoRAf18ZfvaHywl8qeGMqU3tTuOb%2Bu3nL3C3QwGnEXD29HYW78HT4s%2BCkBTnMUTDFnzgG1TRr4M11zYCQwt81kaItEak42JjU0MtgV5MsJhIzdUWBAdDtgmoNEWsg8UOFj2f4IkzO2tw6RuKK4ZO9CoYMrQJHFmtqtmYd3LOFI%2BfL%2BaHAvqoEE9fFToUzhyokvYNU974G5Hn6Z%2BrCqmagLi03wqqGhgvvUSXXvnzx%2Flbw%3D%3D&secret_key=0PakLTuuKqya80ZUi3KN%2BTj6GaOgjKeDzAgoYHpBZHZ%2BX73SGMDxcvqIlahtDXg10aokU9NBdQgcIGkigyZOCzRCm9rcR7bWaTgIlsu2JD6cVcmkxU%2BwHvsTpcqvQrAyPk%2Ftesh6P1evyFgCyAcx6LnKJJ4jRNEGmqmSrQPuIaA%3D&uid=1d91d457-ecda-44a1-ad24-655f89002897"
    )
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-GB,en;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Sec-CH-UA": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "Sec-CH-UA-Mobile": "?1",
        "Sec-CH-UA-Platform": '"Android"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Referer": "https://notegpt.io/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        text = response.text
        return text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def extract_markdown(data):
    if not data:
        return ""
    matches = re.findall(r'"message":\s*"([^"]*)"', data)
    summary = "".join(matches)
    return summary.replace("\\n", "\n")

def generate_md_mindmap():
    text = extract_pdf_text("sample.pdf")
    prompt = generate_prompt(text)
    data = get_data(prompt)
    markdown = extract_markdown(data)
    return markdown

# mm = generate_md_mindmap()
# print(mm)