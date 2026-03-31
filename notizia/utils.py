from django.utils.text import slugify

def unique_slug_generator(model_instance, title, slug_field):
    """
    :param model_instance:
    :param title:
    :param slug_field:
    :return:
    """

    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class.default_manager.filter(slud=slug).exists():
        object_pk = model_class.__default_manager.latest('pk')
        object_pk = object_pk + 1

        slug = f'{slud}-{object_pk}'

    return slug
