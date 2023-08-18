from functions import *
send_sms("+254712764453", "Hello There... ")

otp_code = generate_random()
print(otp_code)

status = passwordValidity("1234567890Admin@")
print(status)

valid_phone = check_phone("+254712764453")
print(valid_phone)