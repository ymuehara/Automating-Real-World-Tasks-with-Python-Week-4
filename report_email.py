#!/usr/bin/env python3

# https://docs.python.org/3/library/email.examples.html

import os
from datetime import datetime
import reports
import emails


def process_data(path):
    data_processed = []
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(path + file, 'r') as f:
                inline = f.readlines()
                name = inline[0].strip()
                weight = inline[1].strip()
                data_processed += f"name: {name} <br/>weight: {weight}<br/><br/>"
    return data_processed


if __name__ == "__main__":

    path = "supplier-data/descriptions/"

    current_date = datetime.now().strftime('%m %d, %Y')
    title = f"Process Updated on {current_date}"
    info = process_data(path)
    reports.generate_report("/tmp/processed.pdf", title, info)

    username = "your_lab_username"
    sender = "automation@example.com"
    receiver = f"{username}@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. " \
           "A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)

