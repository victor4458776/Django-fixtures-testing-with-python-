victoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ python3 manage.py dumpdata auth.User --pk 1 --indent 4
[
{
    "model": "auth.user",
    "pk": 1,
    "fields": {
        "password": "!eQzItfkA3j1VfJv97XIh3ZVAV805SBG04qqZC8KC",
        "last_login": null,
        "is_superuser": false,
        "username": "victor",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2023-07-31T15:19:07.415Z",
        "groups": [
            1
        ],
        "user_permissions": []
    }
}
]
# User permissions-security issues
# Username and password -related issues, because anyone can check the password with..
# python3 manage.py dumpdata auth.User --pk 1 --indent 4 (you can get some users)
# Using primary keys to reference objects in fixtures is not always a good idea. The primary key of a group is an arbitrary 
# identifier that the database assigns to the group when it is created. In another environment, or on another computer, 
# the appusers group can have a different ID and it wouldn’t make any difference on the object.

ictoralonsogarcia8@penguin:~/django_fixtures/django_fixtures$ python3 manage.py dumpdata auth.User --pk 1 --indent 4 --natural-foreign
[
{
    "model": "auth.user",
    "pk": 1,
    "fields": {
        "password": "!eQzItfkA3j1VfJv97XIh3ZVAV805SBG04qqZC8KC",
        "last_login": null,
        "is_superuser": false,
        "username": "victor",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2023-07-31T15:19:07.415Z",
        "groups": [
            [
                "appusers"
            ]
        ],
        "user_permissions": []
    }
}
]

