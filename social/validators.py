from django.core.validators import RegexValidator

PHONE_NUMBER_REGEX = RegexValidator(r'^(0|[1-9]\d*)$', 'inserisci solo anno in questo campo')
