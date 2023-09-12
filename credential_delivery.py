```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from CredentialSchema import CredentialSchema

def deliverCredentials():
    # Define the system credentials
    system_credentials = CredentialSchema()

    # Define the email parameters
    sender_address = 'agi@businessplan.com'
    sender_pass = 'password'
    receiver_address = '[Email Address]'
    mail_content = f'Hello, \n\nHere are your system credentials:\n\n{system_credentials}\n\nBest,\nAGI'

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'System Credentials Delivery'   
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls() 
    session.login(sender_address, sender_pass) 
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    print('Mail Sent')

deliverCredentials()
```