from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounts.models import *


@receiver(pre_save, sender=Profile)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).profile_pic.path
        try:
            new_img = instance.profile_pic.path
        except:
            new_img = None
        if new_img != old_img:
            id=instance.id
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass
