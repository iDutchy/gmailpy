import smtplib
import asyncio
import functools

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Error(Exception):
    pass

class Client:
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password
        
        
    def send(self, receiver, body, subject="No subject", bcc=None, attachment_bytes=None, attachment_name=None):
        sender_email = self.mail
        password = self.password

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver
        message["Subject"] = subject
        message["Bcc"] = bcc

        message.attach(MIMEText(body, "plain"))
        
        if not attachment_name and attachment_bytes:
            raise Error('You did not provide an attachment name for your attachment!')
            
        if attachment_name and not attachment_bytes:
            raise Error('Can not set an attachment name without an attachment!')
        
        if attachment_bytes and attachment_name:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment_bytes)

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attachment_name}",
            )

            message.attach(part)

        text = message.as_string()

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver, text)

        async def send_async(self, receiver, body, subject="No subject", bcc=None, attachment_bytes=None, attachment_name=None):
            loop = asyncio.get_event_loop()
            sync_send = functools.partial(send, receiver, body, subject, bcc, attachment_bytes, attachment_name)
            return await loop.run_in_executor(None, sync_send)
