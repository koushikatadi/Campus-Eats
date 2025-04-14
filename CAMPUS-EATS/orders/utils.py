import time
from django.core.mail import send_mail
from django.conf import settings
def run_this_function():
    print("Function started")
    print("Function started..")

    time.sleep(2)
    print("Function executed")


def send_email_to_client(recipient_list):
    Subject = "This email is from Campus Eats"
    message = "YOUR FOOD IS READY 🍔"
    from_email = settings.EMAIL_HOST_USER

    send_mail(Subject, message, from_email, recipient_list)
