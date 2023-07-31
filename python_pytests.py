ictoralonsogarcia8@penguin:~/django_fixtures/pytest.ini/django_pytest$ nano
victoralonsogarcia8@penguin:~/django_fixtures/pytest.ini/django_pytest$ lsdb.sqlite3  django_pytest  manage.py  test1.py
victoralonsogarcia8@penguin:~/django_fixtures/pytest.ini/django_pytest$ python3 manage.py shell
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> 
>>> def test_should_create_user_with_username() -> None:
...     user = User.objects.create_user("Haki")
...     assert user.username == "Haki"
... 
>>> 
now exiting InteractiveConsole...
victoralonsogarcia8@penguin:~/django_fixtures/pytest.ini/django_pytest$ pytest test1.py
========================== test session starts ===========================
platform linux -- Python 3.9.2, pytest-7.4.0, pluggy-1.2.0
rootdir: /home/victoralonsogarcia8/django_fixtures/pytest.ini/django_pytest
plugins: django-4.5.2
collected 1 item                                                         

test1.py .                                                         [100%]

=========================== 1 passed in 0.09s ============================
