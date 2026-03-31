from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Rimosso: from django.utils import six (non più necessario)

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # In Python 3, usiamo direttamente str() invece di six.text_type
        return (
            str(user.pk) + str(timestamp) +
            str(user.profile.signup_confirmation)
        )

account_activation_token = TokenGenerator()
