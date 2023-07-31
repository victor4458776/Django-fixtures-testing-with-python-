# Django-fixtures-testing-with-python-
If you’re working in Django, pytest fixtures can help you create tests for your models that are uncomplicated to maintain. Writing good tests is a crucial step in sustaining a successful app, and fixtures are a key ingredient in making your test suite efficient and effective. Fixtures are little pieces of data that serve as the baseline for your tests.

Django steps: 

-How to create and load test fixtures in Django 

-How to create and load pytest fixtures for Django models 

-How to use factories to create test fixtures for Django models in pytest 

-How to create dependencies between test fixtures using the factory as fixture pattern

# COMMANDS TO START THE PROJECT

victoralonsogarcia8@penguin:~$ mkdir django_fixtures

victoralonsogarcia8@penguin:~$ cd django_fixtures

victoralonsogarcia8@penguin:~/django_fixtures $ source venv/bin/activate

# COMMANDS TO START THE DJANGO TESTING-PROJECT

victoralonsogarcia8@penguin:~/django_fixtures$ ls

victoralonsogarcia8@penguin:~/django_fixtures$ pip install django

# COMMANDS TO START MIGRATIONS

# FIXTURES-PATH

victoralonsogarcia8@penguin:~/django_fixtures$ django startproject django_fixtures

victoralonsogarcia8@penguin:~/django_fixtures$ django-admin startproject django_fixtures

victoralonsogarcia8@penguin:~/django_fixtures$ cd django_fixtures

victoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ ls

django_fixtures  manage.py

victoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ python3 manage.py migrate

# MANAGE DJANGO DATA AND TESTS THE DATABASE

Maintaining Django Fixtures:

Django fixtures are great, but they also pose some challenges:

Keeping fixtures updated: Django fixtures must contain all the required fields of the model. If you add a new field that is not nullable, you must update the fixtures. Otherwise, they will fail to load. Keeping Django fixtures updated can become a burden when you have lots of them.

Maintaining dependencies between fixtures: Django fixtures that depend on other fixtures must be loaded together and in a particular order. Keeping up with fixtures as new test cases are added and old test cases are modified can be challenging.

For these reasons, Django fixtures are not an ideal choice for models that change often. For example, it would be very difficult to maintain Django fixtures for models that are used to represent core objects in the app such as sales, orders, transactions, or reservations.

On the other hand, Django fixtures are a great option for the following use cases:

Constant data: This applies to models that rarely change, such as country codes and zip codes.

Initial data: This applies to models that store your app’s lookup data, such as product categories, user groups, and user types.
