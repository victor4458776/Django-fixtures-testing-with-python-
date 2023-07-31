# The first test checks that a user with a usable password is being validated by Django. 
# The second test checks an edge case in which the user’s password is unusable and should not be validated by Django.

(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> def test_check_password(db) -> None:
...     user = User.objects.create_user("A")
...     user.set_password("secret")
...     assert user.check_password("secret") is True
... 
>>> def test_check_unusable(db) -> None:
...     user = User.objects.create_user("A")
...     user.set_password("secret")
...     user.set_unusable_password()
...     assert user.check_password("secret") is False
... 
>>> print(test_check_password)
<function test_check_password at 0x7b0a59b8fe50>
>>> 

#ANOTHER PASSWORD TEST
import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user_A(db) -> User:
    return User.objects.create_user("A")

def test_should_check_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    assert user_A.check_password("secret") is True

def test_should_not_check_unusable_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    user_A.set_unusable_password()
    assert user_A.check_password("secret") is False
  # function called user_A() that creates and returns a new User instance. To mark the function as a fixture, 
  # you decorated it with the pytest.fixture decorator. 
  # Once a function is marked as a fixture, it can be injected into test cases
