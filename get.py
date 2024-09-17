import requests

headers = {"Authorization": "Basic cmtfbGl2ZV81MUw5c3JLQ29GamtETjR4UGtvdEs2V0dHUHFmd2tnd3RFNkkxcTFURTlrdktzZ0s3SlQ5Mk5oaUFHeGpKeDQ0ejdHZnBzU1hZNmtpTVkyTTFWWkhFajJZVjAwbjRPS3pUSlg6"}
result = requests.get("https://api.stripe.com/v1/customers", headers=headers).json()

license_code = [customer['metadata']['license_code'] for customer in result['data']]
print(license_code)
