from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class PhoneNumberValidator(RegexValidator):
    regex = '^98(9[0-3,9]\d{8}|[1-9]\d{9}$'
    message = _('Phone')
    code = 'invalid phone'

class UsernameValidator(RegexValidator):
    regex = '^[a-zA-Z][a-zA-Z0-9_\.]+$'
    message = _('Username is invalid')
    code = 'Invalid Username'

validate_phone_number = PhoneNumberValidator()
validate_username = UsernameValidator()