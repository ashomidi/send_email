import random
import smtplib
from email.message import EmailMessage
import ssl

email_sender = "some_email@gmail.com"
email_password = "Get it from your google account"
email_recipient = input("Enter your email: ")
otp = random.randint(10000, 99999)

email_subject = "OTP Verification"
email_body = f"Your otp is {otp}"

em = EmailMessage()

em["Subject"] = email_subject
em["From"] = email_sender
em["To"] = email_recipient
em.set_content(email_body)

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls(context=context)
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_recipient, em.as_string())

inp_otp = int(input("Enter OTP: "))
if otp == inp_otp:
    print("You're in")
else:
    print("Sorry!")
