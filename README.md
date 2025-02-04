Question 1: By default are django signals executed synchronously or asynchronously?
Answer: By default, Django signals are executed synchronously. This means they run in the same process and block execution until they complete.

Question 2: Do django signals run in the same thread as the caller?
Answer: Yes, Django signals run in the same thread.
 
Question 3: By default do django signals run in the same database transaction as the caller?
Answer: Yes, signals run in the same transaction unless handled asynchronously.

How to Run This Project:

1.Clone the Repository
git clone https://github.com/your-username/signals_project.git
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



