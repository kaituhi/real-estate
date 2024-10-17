import pytest

def test_user_str(base_user):
    """Test the string representation of the custom user model."""
    assert base_user.__str__() == f"{base_user.username}"

def test_user_short_name(base_user):
    """Test the get_short_name method of the user model."""
    short_name = f"{base_user.username}"
    assert base_user.get_short_name() == short_name

def test_user_full_name(base_user):
    """Test the get_full_name method of the user model."""
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name

def test_base_user_email_is_normalized(base_user):
    """Ensure that a new user's email is normalized."""
    email = "alpha@REALESTATE.COM"
    assert base_user.email == email.lower()

def test_super_user_email_is_normalized(super_user):
    """Ensure that an admin user's email is normalized."""
    email = "alpha@REALESTATE.COM"
    assert super_user.email == email.lower()

def test_super_user_is_not_staff(user_factory):
    """Ensure an error is raised when an admin user has is_staff=False."""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superusers must have is_staff=True"

def test_super_user_is_not_superuser(user_factory):
    """Ensure an error is raised when an admin user has is_superuser=False."""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "Superusers must have is_superuser=True"

def test_create_user_with_no_email(user_factory):
    """Ensure an error is raised when creating a user without an email address."""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"

def test_create_user_with_no_username(user_factory):
    """Ensure an error is raised when creating a user without a username."""
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "Users must submit a username"

def test_create_user_with_no_first_name(user_factory):
    """Ensure an error is raised when creating a user without a first name."""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "Users must submit a first name"

def test_create_user_with_no_last_name(user_factory):
    """Ensure an error is raised when creating a user without a last name."""
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "Users must submit a last name"

def test_create_superuser_with_no_email(user_factory):
    """Ensure an error is raised when creating a superuser without an email address."""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"

def test_create_superuser_with_no_password(user_factory):
    """Ensure an error is raised when creating a superuser without a password."""
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Superusers must have a password"

def test_user_email_incorrect(user_factory):
    """Ensure an error is raised when a non-valid email address is provided."""
    with pytest.raises(ValueError) as err:
        user_factory.create(email="realestate.com")
    assert str(err.value) == "You must provide a valid email address"
