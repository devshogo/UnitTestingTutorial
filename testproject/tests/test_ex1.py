# from cgi import test
# from importlib.util import module_for_loader
from itertools import count
import pytest

from django.contrib.auth.models import User


# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True




# @pytest.mark.markerName
# @pytest.mark.xfail

# @pytest.mark.skip


# function  runs once per test
# class run once per class of test
# module run once per module 
# session run once per session


# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test', 'test@test.com', 'test')
#     count = User.objects.all().count()
#     print(count)
#     assert User.objects.count() == 1
    

# @pytest.mark.django_db
# def test_user_create1():
#     count = User.objects.all().count()
#     print(count)
#     assert count ==0


# @pytest.mark.django_db
# def test_my_user():
#     me = User.objects.get(username='test')
#     assert me.is_superuser


# @pytest.fixture()
# def fixture_1():
#     print('run fixture_1')
#     return 1

# def test_example_1(fixture_1):
#     print('run example_1')
#     num = fixture_1
#     assert num == 1

# def test_example():
#     print('test1')
#     assert 1 == 1

# def test_example2():
#     print('test 2')
#     assert 1 == 1


# run the command (pytest -x) 
# to stop the test when one of the tests fails
# pytest -m "markerName"
# pytest -rP // to get reports