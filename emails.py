#!/usr/bin/env python3

# https://docs.python.org/3/library/email.examples.html
# https://docs.python.org/3/library/email.html

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):

    msg = email.message.EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    attachment_name = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)

    with open(attachment_path, 'rb') as fp:
      msg.add_attachment(fp.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_name)
    return msg


def send_email(package):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(package)
  mail_server.quit()
