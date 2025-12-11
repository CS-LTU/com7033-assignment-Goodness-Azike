import os
import sys
from pydantic import ValidationError

# Make sure the backend root (where controller/ lives) is on sys.path
CURRENT_DIR = os.path.dirname(__file__)
BACKEND_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if BACKEND_ROOT not in sys.path:
    sys.path.insert(0, BACKEND_ROOT)

from controller.auth import SignupRequest


def test_password_too_short():
    """Password shorter than 8 characters should fail validation."""
    try:
        SignupRequest(
            firstName="Test",
            lastName="User",
            email="test@example.com",
            role="patient",
            phone="07000000000",
            password="Abc12",
            confirmPassword="Abc12",
            dateOfBirth="1995-01-01",
            gender="female"
        )
        assert False, "Expected ValidationError for short password"
    except ValidationError as e:
        error_messages = [err["msg"] for err in e.errors()]
        assert any("at least 8 characters" in msg for msg in error_messages)


def test_password_valid():
    """A strong password should pass validation."""
    obj = SignupRequest(
        firstName="Test",
        lastName="User",
        email="test2@example.com",
        role="patient",
        phone="07000000000",
        password="StrongPass1",
        confirmPassword="StrongPass1",
        dateOfBirth="1995-01-01",
        gender="female"
    )
    assert obj.password == "StrongPass1"

