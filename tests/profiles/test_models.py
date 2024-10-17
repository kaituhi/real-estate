import pytest

def test_profile_str(profile):
    """Test the string representation of the profile model."""
    assert profile.__str__() == f"{profile.user.username}'s profile"
