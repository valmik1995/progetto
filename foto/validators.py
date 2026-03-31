import os
import magic
from pathlib import Path
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.core.validators import RegexValidator


PHONE_NUMBER_REGEX = RegexValidator(r'^(0|[1-9]\d*)$', 'inserisci solo anno in questo campo')

@deconstructible
class FileMimeValidator:

    messages = {
        "malicious_file": "I files sembra dannoso. Le estensioni consentite sono: '%(allowed_extensions)s'.",
        "not_supported": "Estensione dei files '%(extension)s' non supportata. "
                         "Estensione dei files autorizzati: '%(allowed_extensions)s'."
    }
    code = 'invalid_extension'
    ext_cnt_mapping = {
        'jpeg': 'image/jpeg',
		'jpg': 'image/jpeg',
        'png': 'image/png'
    }

    def __init__(self, ):
        self.allowed_extensions = [allowed_extension.lower() for
            allowed_extension in self.ext_cnt_mapping.keys()]

    def __call__(self, data):
        extension = Path(data.name).suffix[1:].lower()
        content_type = magic.from_buffer(data.read(1024), mime=True)
        if extension not in self.allowed_extensions:
            raise ValidationError(
                self.messages['not_supported'],
                code=self.code,
                params={
                    'extension': extension,
                    'allowed_extensions': ', '.join(self.allowed_extensions)
                }
            )
        if content_type != self.ext_cnt_mapping[extension]:
            raise ValidationError(
                self.messages['malicious_file'],
                code=self.code,
                params={
                    'allowed_extensions': ', '.join(self.allowed_extensions)
                }
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.allowed_extensions == other.allowed_extensions and
            self.message == other.message and
            self.code == other.code
        )

@deconstructible
class FileMimeValidatorHeic:

    messages = {
        "malicious_file": "I files sembra dannoso. Le estensioni consentite sono: '%(allowed_extensions)s'.",
        "not_supported": "Estensione dei files '%(extension)s' non supportata. "
                         "Estensione dei files autorizzati: '%(allowed_extensions)s'."
    }
    code = 'invalid_extension'
    ext_cnt_mapping = {
        'heic': 'image/heic',
    }

    def __init__(self, ):
        self.allowed_extensions = [allowed_extension.lower() for
            allowed_extension in self.ext_cnt_mapping.keys()]

    def __call__(self, data):
        extension = Path(data.name).suffix[1:].lower()
        content_type = magic.from_buffer(data.read(1024), mime=True)
        if extension not in self.allowed_extensions:
            raise ValidationError(
                self.messages['not_supported'],
                code=self.code,
                params={
                    'extension': extension,
                    'allowed_extensions': ', '.join(self.allowed_extensions)
                }
            )
        if content_type != self.ext_cnt_mapping[extension]:
            raise ValidationError(
                self.messages['malicious_file'],
                code=self.code,
                params={
                    'allowed_extensions': ', '.join(self.allowed_extensions)
                }
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.allowed_extensions == other.allowed_extensions and
            self.message == other.message and
            self.code == other.code
        )


