ictoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ python3 manage.py shell
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

# The Group model is part of Django’s authentication system. Groups are very useful for managing permissions in a Django project.
>>> from django.contrib.auth.models import Group
>>> group = Group.objects.create(name="appusers")
>>> group.pk
1

#LINUX-UBUNTU COMMANDS
victoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ python3 manage.py dumpdata auth.Group --pk 1 --indent 4 > group.json
victoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ ls
db.sqlite3  django_fixtures  group.json  manage.py

#DESCRIPTION
# auth.Group: This describes which model to dump. The format is <app_label>.<model_name>.

# --pk 1: This describes which object to dump. The value is a comma-delimited list of primary keys, such as 1,2,3.

# --indent 4: This is an optional formatting argument that tells Django how many spaces to add before each indention level in the generated file. Using indentions makes the fixture file more readable.

# > group.json: This describes where to write the output of the command. In this case, the output will be written to a file called group.json.
# GROUP-JSON
[
{
    "model": "auth.group",
    "pk": 1,
    "fields": {
        "name": "appusers",
        "permissions": []
    }
}
# The fixture file contains a list of objects. In this case, you have only one object in the list. 
# Each object includes a header with the name of the model and the primary key, as well as a dictionary with the value 
#  for each field in the model. You can see that the fixture contains the name of the group appusers. 
