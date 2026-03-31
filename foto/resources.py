from import_export import resources
from foto.models import Galleria

class GalleriaResource(resources.ModelResource):
    class Meta:
        model = Galleria
