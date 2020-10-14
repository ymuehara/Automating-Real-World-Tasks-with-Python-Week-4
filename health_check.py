#!/usr/bin/env python3

#https://psutil.readthedocs.io/en/latest/

import os
import shutil
import psutil
import socket
from emails import generate_error_report, send_email


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage < 80


def check_disk_space():
    disk_usage = shutil.disk_usage("/")
    available_space = disk_usage.free / disk_usage.total * 100
    return available_space > 20


def check_available_memory():
    available_memory = psutil.virtual_memory().available
    available_memory_inMB = available_memory / (1024**2)
    return available_memory_inMB > 500


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


if check_cpu_usage():
    error_message = "CPU usage is over 80%"
elif not check_disk_space():
    error_message = "Available disk space is less than 20%"
elif not check_available_memory():
    error_message = "Available memory is less than 500MB"
elif not check_localhost():
    error_message = "localhost cannot be resolved to 127.0.0.1"
else:
    pass

# email is sent if any issues are detected in the system statistics above


def email_error(error_message):
    user = "your_username"
    sender = "automation@example.com"
    receiver = f"{user}@example.com"
    subject = f"Error - {error_message}"
    body = "Please check your system and resolve the issue as soon as possible"
    message = generate_error_report(sender, receiver, subject, body)
    send_email(message)


if __name__ == "__main__":
    email_error(error_message)
