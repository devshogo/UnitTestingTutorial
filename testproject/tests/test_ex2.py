import pytest



# def test_set_check_password(user_1):    
#     assert user_1.username == "test-user"

# def test_new_user(new_user):
#     print(new_user.first_name)    
#     assert new_user.first_name == "MyName"

# def test_new_staff_user(new_staff_user):
#     print(new_staff_user.is_staff)    
#     assert new_staff_user.is_staff == "True"

def test_new_staff_user(user_factory):
    print(user_factory.username)    
    assert True
