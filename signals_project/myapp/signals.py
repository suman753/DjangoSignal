import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading
from django.db import transaction

#  Check If Django Signals Run Synchronously

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulate delay
    print("Signal finished")

#  Check If Django Signals Run in the Same Thread


@receiver(post_save, sender=User)
def my_thread_checker(sender, instance, **kwargs):
    print(f"Signal is running in thread: {threading.current_thread().name}")



# Check If Django Signals Run in the Same Transaction

@receiver(post_save, sender=User)
def my_transaction_checker(sender, instance, **kwargs):
    print("Inside signal")
    print(f"Transaction state: {transaction.get_autocommit()}")  # 0 means inside a transaction
