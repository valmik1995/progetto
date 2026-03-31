import os
from django.conf import settings
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from foto.models import *
from foto.tasks import watermarks
from django.core.mail import send_mail

@receiver(pre_delete, sender=Galleria)
def remove_files (sender, instance, **kwargs) :
    if os.path.exists(instance.image.name):
        os.remove(os.path.join(settings.MEDIA_ROOT, instance.image.name))
        os.remove(os.path.join(settings.MEDIA_ROOT, instance.image_thumbails.name))
        os.remove(os.path.join(settings.MEDIA_ROOT, instance.image_watermarks.name))
            

@receiver(post_save, sender=Galleria)
def function(sender, instance, created, **kwargs):
    if not created:
        id = []
        id.append(instance.id)
        watermarks(id)
    if created:
        subject = f'Galleria Immagini inserimento da parte di {instance.user}'
        from_email = settings.DEFAULT_FROM_EMAIL
        message = 'This is my test message'
        recipient_list = ['valerio.podrini@gmail.com',]
        html_message = f'<h1>Titolo: {instance.title} </h1><p>Descrizione: {instance.description} Categoria: {instance.category}</p>'
        send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)


# @receiver(pre_delete, sender=Galleria)
# def Galleria_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     instance.image.delete(False)
#     instance.image_thumbails.delete(False)
#     instance.image_foto.delete(False)


@receiver(pre_save, sender=Galleria)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img:
            id=instance.id
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass



    
