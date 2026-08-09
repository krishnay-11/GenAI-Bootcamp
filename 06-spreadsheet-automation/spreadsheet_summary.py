import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

GOOGLE_SPREADSHEET_API_KEY = os.getenv("GOOGLE_SPREADSHEET_API_KEY")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SHEET_NAME = os.getenv("SHEET_NAME")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def get_spreadsheet_data():
    """Fetch spreadsheet data"""
    service = build('sheets', 'v4', developerKey=GOOGLE_SPREADSHEET_API_KEY)
    all_rows = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_NAME).execute()['values']
    with open('last_row.txt') as file:
        last_row = int(file.read())
    new_rows = all_rows[last_row:]
    headers = all_rows[0]
    return all_rows, new_rows, headers

def summarize_with_ai(text):
    system_prompt = """
    You are a helpful assistant that summarizes spreadsheet data.
    You will receive new rows that were added to a Google Spreadsheet. 
    Please provide a clear, concise summary of this data"
    """
    model = init_chat_model("gemini-3.1-flash-lite",api_key=GEMINI_API_KEY, model_provider="google_genai")
    message = [{"role": "system", "content": system_prompt},
               {"role": "user", "content": f"Here are the new rows from the spreadsheet \n {text}"}]
    response = model.invoke(message).content
    return response

def send_email(subject, body):
    """Send email with the summary."""
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()
    print(f"Email sent successfully to {RECIPIENT_EMAIL}")


all_rows, new_rows, headers = get_spreadsheet_data()
total_rows = len(all_rows)
with open("last_row.txt", 'w') as file:
    file.write(str(total_rows))

message = f"Headers: {headers} \nNew rows: {new_rows}"
print(message)
summary = summarize_with_ai(message)

body = f"Here is today's summary \n\n{summary}\n\n Thanks!"
send_email("Daily Spreadsheet Summary", body)

print("ALL ROWS", all_rows)
print("NEW ROWS", new_rows)
print(summary)
