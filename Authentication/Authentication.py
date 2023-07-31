>>> from django.contrib.auth.models import Group
>>> Group.objects.filter(pk=1).delete()
(1, {'auth.Group': 1})

>>> 
now exiting InteractiveConsole...
victoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ python3 manage.py loaddata group.json
Installed 1 object(s) from 1 fixture(s)

>>> from django.contrib.auth.models import Group
>>> group = Group.objects.get(pk=1)
>>> vars(group)
{'_state': <django.db.models.base.ModelState object at 0x7946bbeaa6d0>, 'id': 1, 'name': 'appusers'}
>>> from django.test import TestCase
>>> from django.contrib.auth.models import Group
>>> 
>>> class MyTest(TestCase):
...     def test_should_create_group(self):
...         group = Group.objects.get(pk=1)
...         self.assertEqual(group.name, "appusers")
... 
>>> print(MyTest)
<class 'MyTest'>

#RESULTS
victoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ python3 manage.py test test
Found 43 test(s).
System check identified no issues (0 silenced).
.....................s.....................
----------------------------------------------------------------------
Ran 43 tests in 8.396s

OK (skipped=1)
