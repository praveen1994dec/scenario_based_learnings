import requests

def send_slack_notification(webhook_url, message):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Notification sent to Slack")
    else:
        print(f"Failed to send Slack notification, status code: {response.status_code}")

if __name__ == "__main__":
    webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    send_slack_notification(webhook_url, "Deployment completed successfully")
