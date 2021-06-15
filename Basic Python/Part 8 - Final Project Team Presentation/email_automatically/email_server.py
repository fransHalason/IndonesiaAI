# Import library
import smtplib, ssl
from email.mime.text import MIMEText
from email.utils import formataddr


# User configuration
sender_email = 'nihaopython21@gmail.com'
sender_name = 'Nihao Python'

receiver_email = 'projectspython3@gmail.com'
receiver_name = 'Projects Python'

password = input('Please, type your password:\n')

# Email body
email_body = '''This is a test email sent by Python. Isn't that cool?'''

print("Sending the email ...")

# Configurating the email information
msg = MIMEText(email_body, 'plain')
msg['To'] = formataddr((receiver_name, receiver_email))
msg['From'] = formataddr((sender_name, sender_email))
msg['Subject'] = 'Hello, my best friend ' + receiver_name

try:
    # Creating a SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Encryps the email
    context = ssl.create_default_context()
    server.starttls(context=context)
    # We log in into our Gmail account
    server.login(sender_email, password)
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent')
except:
    print(f"Oh no! Something bad happened!\n{e}")
finally:
    print('Closing the server....')
    server.quit()
