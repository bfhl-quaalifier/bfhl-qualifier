import requests

# Configuration

NAME = "Your Name"
REG_NO = "REG12347"
EMAIL = "your.email@example.com"

# 1. Generate Webhook

print("Sending request to generate webhook...")

response = requests.post(
    "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
    json={
        "name": NAME,
        "regNo": REG_NO,
        "email": EMAIL
    }
)

if response.status_code != 200:
    print("Failed to generate webhook:", response.text)
    exit()

data = response.json()
webhook_url = data['webhook']
access_token = data['accessToken']

print("Webhook generated successfully!")
print("Webhook URL:", webhook_url)
print("Access Token:", access_token)


# Based on REG_NO last digit:
#   Odd → Question 1
#   Even → Question 2

print("\nGo to the appropriate SQL question link:")
print("- Odd → https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxoskJWY/view?usp=sharing")
print("- Even → https://drive.google.com/file/d/1PO1ZvmDqAZJv77XRYsVben11Wp2HVb/view?usp=sharing")

# Read SQL query from file
with open("../sql/solution.sql", "r") as file:
    final_sql_query = file.read().strip()


# 3. Submit SQL Query

print("\nSubmitting final SQL query...")

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submission_response = requests.post(
    "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON",
    headers=headers,
    json={"finalQuery": final_sql_query}
)

if submission_response.status_code == 200:
    print("Submission successful!")
else:
    print("Submission failed:", submission_response.text)
