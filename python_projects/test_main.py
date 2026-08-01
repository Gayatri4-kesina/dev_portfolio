"""import pytest

from main import LinuxUser
 
@pytest.mark.parametrize("uid,expected",[
    (0,True),
    (1000,True),
    (-1,False),
    ("abc",False),
    (999,True),
    ])
def test_user_uid(uid,expected):
   user=LinuxUser()
   assert user.is_valid_uid(uid) == expected
  

@pytest.fixture
def user():
   user=LinuxUser()
   user.add_users("gayathri",1000,["sudo","family"])
   return user

def test_user_add(user):
   user.add_users("testuser",1001,["sudo","developers"])
   assert user.username == "testuser"

def test_group_add(user):
   user.add_groups("developers")
   assert "developers" in user.groups

def test_rm_group(user):
   user.rm_groups("developers")
   assert "developers" not in user.groups

def test_add_uid(user):
   with pytest.raises(ValueError):
     user.add_users("bad",-5,["sudo"])
"""


import pytest
from main import LinuxUser

@pytest.fixture
def user():
    u = LinuxUser()
    u.add_users("gayathri", 1000, ["sudo", "family"])
    return u

@pytest.mark.parametrize("uid, expected", [
    (0, True),
    (1000, True),
    (-1, False),
    ("abc", False),
    (999, True),
])
def test_valid_uid(uid, expected):
    u = LinuxUser()
    assert u.is_valid_uid(uid) == expected

def test_create_user(user):
    assert user.username == "gayathri"
    assert user.uid == 1000
    assert user.groups == ["sudo", "family"]

def test_add_group(user):
    user.add_groups("developers")
    assert "developers" in user.groups

def test_remove_group(user):
    user.rm_groups("family")
    assert "family" not in user.groups

def test_remove_nonexistent_group(user, capsys):
    user.rm_groups("nonexistent")
    captured = capsys.readouterr()
    assert "doesn't exist" in captured.out

def test_invalid_uid(user):
    with pytest.raises(ValueError):
        user.add_users("bad", -5, ["sudo"])

def test_str_output(user):
    result = str(user)
    assert "gayathri" in result
    assert "1000" in result
