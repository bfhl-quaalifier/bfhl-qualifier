import requests
import os

# Your Personal Info
NAME = "Sarthak Kacholiya"
REG_NO = "0827IT221132"
EMAIL = "sarthakkacholiya220758@acropolis.in"

# Step 1: Generate Webhook
def generate_webhook():
    print("🔗 Generating webhook...")

    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": NAME,
        "regNo": REG_NO,
        "email": EMAIL
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        print("Webhook generated successfully.")
        print("Webhook URL:", data.get("webhook"))
        print("Access Token:", data.get("accessToken"))
        return data["accessToken"]
    else:
        print(" Failed to generate webhook:", response.text)
        exit()

# -----------------------------
# Step 2: Load SQL Query
# -----------------------------
def load_sql_query():
    sql_path = os.path.join("..", "sql", "solution.sql")
    if not os.path.exists(sql_path):
        print(f" SQL file not found at {sql_path}")
        exit()
    
    with open(sql_path, "r") as file:
        query = file.read().strip()
    print("Loaded SQL query.")
    return query

# Step 3: Submit Final Query
def submit_query(access_token, final_query):
    print("📤 Submitting final SQL query...")

    url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    payload = {
        "finalQuery": final_query
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Submission successful!")
        print("Response:", response.json())
    else:
        print("Submission failed:", response.text)

# Main Logic
if __name__ == "__main__":
    token = generate_webhook()
    query = load_sql_query()
    submit_query(token, query)
