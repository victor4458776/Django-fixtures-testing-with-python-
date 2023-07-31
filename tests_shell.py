>>> from django.test import TestCase
>>> from django.contrib.auth.models import Group
>>> class Test(TestCase):
...     fixtures = ["group.json"]
...     def test_group(self):
...         group = Group.objects.get(pk=1)
...         self.assertEqual(group.name, "appusers")
... 
>>> print(fixtures) # try to extract data-values

victoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ python3 manage.py test test 
Found 43 test(s).
System check identified no issues (0 silenced).
.....................s.....................
----------------------------------------------------------------------
Ran 43 tests in 8.259s

OK (skipped=1)
# The group was loaded and the test passed. You can now use the group appusers in your tests.

Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User, Group
>>> appusers = Group.objects.get(name="appusers")
>>> victor = User.objects.create_user("victor")
>>> victor.pk
1
>>> victor.groups.add(appusers)
>>> print(appusers)
appusers
