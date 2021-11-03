"""
    Email utility file contains logic of mailing attachments and several notifications to user.
"""
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailUtility:
    """
        Class provides methods handling mailing logic of attachments and remainders
    """
    def __init__(self):
        # Accepting username and password from env file.
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.from_address = 'no-reply@classmatebot.com'
        self.subject = 'CLASSMATE BOT NOTIFICATION'

    def send_email(self, recipient: str, attachment=None, subject: str = '', body: str = '',
                   filename: str = ''):
        """
             Adds the homework to json in the specified format.

             Parameters:
                 recipient: user email address.
                 attachment: file attachments.
                 subject: subject of the email.
                 body: body of the email.
                 filename: specifies the file name it should use for attachment data.

             Returns:
                 returns either an error stating a reason for failure or returns a success message
                 indicating that the reminder has been added

         """
        # Recipient address are to be provided as list.
        to_address = recipient if type(recipient) is list else [recipient]

        msg = MIMEMultipart()
        msg['Subject'] = subject if subject else self.subject
        msg['From'] = self.from_address
        msg['To'] = recipient
        body = body if body else "This mail was sent from classmatebot notification service," \
                                 " Please unsubscribe to stop notifications."
        msg.attach(MIMEText(body, 'plain'))

        if attachment:
            # Attaching the attachment data only if it exists.
            part = MIMEBase('application', "octet-stream")
            part.set_payload(attachment)
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(part)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(list(self.from_address), to_address, msg.as_string())
            server.close()
            print("successfully sent the mail to " + recipient)
        except Exception as error:
            with open("err.log", "a") as f:
                f.write(f"Error while sending email : {str(error)}\n")

