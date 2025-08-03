# scripts/automated_reporter.py
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def get_report_data():
    """
    Placeholder to get data for the weekly report.
    """
    print("Gathering data for the weekly report...")
    # This would query the integrated data source
    report_data = {
        "Brand Marketer": {"metric": "Brand Sentiment", "value": "Positive", "change": "+2%"},
        "Media Buyer": {"metric": "ROAS", "value": "3.9x", "change": "+0.1x"},
        "Analyst": {"metric": "Data Accuracy", "value": "98%", "change": "0%"},
        "Designer": {"metric": "Top Creative CTR", "value": "2.1%", "change": "+0.3%"}
    }
    print("Data gathered.")
    return report_data

def generate_report_html(data):
    """
    Generates an HTML report from the data.
    """
    print("Generating HTML report...")
    html = "<h1>Weekly BMAD Performance Report</h1>"
    html += f"<p>Report for week ending: {datetime.now().strftime('%Y-%m-%d')}</p>"
    html += "<table border='1'><tr><th>Role</th><th>Metric</th><th>Value</th><th>WoW Change</th></tr>"
    for role, metrics in data.items():
        html += f"<tr><td>{role}</td><td>{metrics['metric']}</td><td>{metrics['value']}</td><td>{metrics['change']}</td></tr>"
    html += "</table>"
    print("HTML report generated.")
    return html

def send_email_report(html_content):
    """
    Simulates sending the report via email.
    """
    # In a real app, use environment variables for email config
    sender_email = "reporter@bmad.com"
    receiver_email = "marketing-team@bmad.com"
    smtp_server = "localhost"
    port = 1025 # Default for local debug servers

    message = MIMEText(html_content, "html")
    message["Subject"] = f"Weekly BMAD Performance Report - {datetime.now().strftime('%Y-%m-%d')}"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    print(f"Simulating sending email to {receiver_email}...")
    # In a real scenario, the following lines would be used.
    # try:
    #     with smtplib.SMTP(smtp_server, port) as server:
    #         server.sendmail(sender_email, receiver_email, message.as_string())
    #     print("Email sent successfully!")
    # except Exception as e:
    #     print(f"Failed to send email: {e}")
    
    # For this simulation, we'll just print that it was successful.
    print("Email sent successfully! (Simulation)")


def main():
    """Main function to run the automated reporter."""
    print("--- Running Automated Reporting System ---")
    data = get_report_data()
    report_html = generate_report_html(data)
    
    # Save a copy of the report
    report_file = "weekly_report.html"
    with open(report_file, "w") as f:
        f.write(report_html)
    print(f"Saved report to {report_file}")
        
    send_email_report(report_html)
    print("--- Automated Reporting System Finished ---")

if __name__ == "__main__":
    main() 