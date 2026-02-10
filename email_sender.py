import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrets import sender_email, receiver_email, password

# Email details

subject = "Test Email from Python"
body = "Hello! This email was sent using Python."

# Create email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

# Send email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)

print("Email sent successfully!")
