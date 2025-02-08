Question 1: By default are django signals executed synchronously or asynchronously?
Answer: By default, Django signals are executed synchronously. This means they run in the same process and block execution until they complete.

Question 2: Do django signals run in the same thread as the caller?
Answer: Yes, Django signals run in the same thread.
 
Question 3: By default do django signals run in the same database transaction as the caller?
Answer: Yes, signals run in the same transaction unless handled asynchronously.

How to Run This Project:

1.Clone the Repository
git clone https://github.com/suman753/DjangoSignal.git
cd signals_project

2.Install Dependencies
pip install django

3. Run Migrations
python manage.py makemigrations
python manage.py migrate

4. Create a Superuser (Optional)
python manage.py createsuperuser

5.Run Django Server
python manage.py runserver

6.Access the Admin Panel (If Needed)
Now, open http://127.0.0.1:8000/admin/ and test signals by creating users. Login using the superuser credentials. Add a new User (This will trigger the post_save signal).

7. Test Django Signals in Shell
Open a new terminal and run:
python manage.py shell
Inside the shell, run:
from django.contrib.auth.models import User
User.objects.create(username="test_user")
(for second time run use different username or else use this command: python manage.py flush
to delete all previously saved data)


You can see console output.
Signal 1 (Synchronous Execution Check)
Signal 2 (Same Thread Check)
Signal 3 (Transaction Check)

Signal started
(5 seconds delay)
Signal finished
Signal is running in thread: MainThread
Inside signal
Transaction state: 0

..................................
and to run rectangle_test.py go to the directory where the file rectangle_test.py is present then run:python rectangle_test.py 
output will be :
{'length': 10}
{'width': 5}

#code.....signals.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading
from django.db import transaction

#Check If Django Signals Run Synchronously
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulate delay
    print("Signal finished")

#Check If Django Signals Run in the Same Thread
@receiver(post_save, sender=User)
def my_thread_checker(sender, instance, **kwargs):
    print(f"Signal is running in thread: {threading.current_thread().name}")


#Check If Django Signals Run in the Same Transaction
@receiver(post_save, sender=User)
def my_transaction_checker(sender, instance, **kwargs):
    print("Inside signal")
    print(f"Transaction state: {transaction.get_autocommit()}")  # 0 means inside a transaction


#code....rectangle_test.py
class Rectangle:
    def __init__(self, length: int, width: int):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width
        self._attributes = [("length", self.length), ("width", self.width)]
    
    def __iter__(self):
        """Make the Rectangle object iterable."""
        for attr, value in self._attributes:
            yield {attr: value}

#Example Usage
if __name__ == "__main__":
    rect = Rectangle(10, 5)  # Create an object of Rectangle

    # Print the attributes one by one using iteration
    for item in rect:
        print(item)


