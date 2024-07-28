import time
import smtplib
from email.mime.text import MIMEText

def monitor_logs(log_file, alert_email):
    with open(log_file, "r") as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if "ERROR" in line:
                send_alert(alert_email, line)
            time.sleep(1)

def send_alert(to_email, message):
    msg = MIMEText(message)
    msg["Subject"] = "Log Alert"
    msg["From"] = "admin@example.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.example.com") as server:
        server.login("username", "password")
        server.sendmail("admin@example.com", [to_email], msg.as_string())
    print(f"Alert sent to {to_email}")

if __name__ == "__main__":
    monitor_logs("/var/log/myapp/app.log", "alert@example.com")
