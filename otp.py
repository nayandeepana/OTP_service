import random
import smtplib

def length(otplength):
    
    otp=[]
    for i in range(0,otplength):
        otp.append(random.randint(0,9))
    print(otp)
    return otp

otp=length(4)
result=""
result=' '.join(map(str, otp))

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "test@gmail.com" #Enter your email here
TO_EMAIL = "senderemail@gmail.com" #Enter sender email here
PASSWORD = "********" #Enter Your password here
print("Sending Email........")
MESSAGE = f"""Subject: Your OTP is {result}
This is a test mail 
to test the server of python script
Thankss
Test Account"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()

otpvalidate=input('Enter OTP : ')

if otpvalidate == result :
    print("OTP validated Successfully!!")
else:
    print("Wrong OTP Entered X ")

