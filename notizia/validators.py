import os
import magic
from pathlib import Path
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

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
class FileMimeValidatorVideo:

    messages = {
        "malicious_file": "I files sembra dannoso. Le estensioni consentite sono: '%(allowed_extensions)s'.",
        "not_supported": "Estensione dei files '%(extension)s' non supportata. "
                         "Estensione dei files autorizzati: '%(allowed_extensions)s'."
    }
    code = 'invalid_extension'
    ext_cnt_mapping = {
        'mp4': 'video/mp4',
		'mov': 'video/quicktime	',
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

# def validate_is_jpeg(file):
#     valid_mime_types = ['image/jpeg']
#     file_mime_type = magic.from_buffer(file.read(1024), mime=True)
#     if file_mime_type not in valid_mime_types:
#         raise ValidationError('Unsupported file type.')
#     valid_file_extensions = ['.jpeg']
#     ext = os.path.splitext(file.name)[1]
#     if ext.lower() not in valid_file_extensions:
#         raise ValidationError('Unacceptable file extension.')


# def validate_file_type(upload):
#     # Make uploaded file accessible for analysis by saving in tmp
#     tmp_path = 'tmp/%s' % upload.name[2:]
#     default_storage.save(tmp_path, ContentFile(upload.file.read()))
#     full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
#     # Get MIME type of file using python-magic and then delete
#     file_type = magic.from_file(full_tmp_path, mime=True)
#     default_storage.delete(tmp_path)
#     # Raise validation error if uploaded file is not an acceptable form of media
#     if file_type not in settings.IMAGE_TYPES:
#         raise ValidationError('File type not supported. JPEG, PNG.')



# class MimetypeValidator(object):
# 	def __init__(self, mimetypes):
# 		self.mimetypes = mimetypes
#
# 	def __call__(self, value):
# 		try:
# 			mime = magic.from_buffer(value.read(1024), mime=True)
# 			if not mime in self.mimetypes:
# 				raise ValidationError('%s is not an acceptable file type' % value)
# 		except AttributeError as e:
# 			raise ValidationError('This value could not be validated for file type' % value)
