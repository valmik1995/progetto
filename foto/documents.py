
from django_elasticsearch_dsl import Document, fields
from elasticsearch_dsl import analyzer, tokenizer
from django_elasticsearch_dsl.registries import registry
from django.contrib.auth.models import User
from foto.models import Galleria, TaggedGalleria, Categoria
from taggit.models import TaggedItemBase

autocomplete_analyzer = analyzer('autocomplete_analyzer', tokenizer=tokenizer( 'trigram', 'nGram', min_gram=1, max_gram=20), filter=['lowercase'])
html_strip = analyzer('html_strip',tokenizer="standard",filter=["lowercase", "stop", "snowball"],char_filter=["html_strip"])

@registry.register_document
class GalleriaDocument(Document):
    id = fields.IntegerField(attr='id', multi=True)

    category = fields.ObjectField(properties={
        'name': fields.TextField(),
    })
    user = fields.ObjectField(properties={
        'username': fields.TextField(),
    })
    tags = fields.ObjectField(properties={
        'slug': fields.TextField(),
        'name': fields.TextField(),
    })
    class Index:
        name = 'galleria'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0,
        'max_ngram_diff': 20,
        }

    class Django:
        model = Galleria
        fields = [
            'title',
            'description',
            'image',
            'image_thumbails',
            'image_watermarks',
        ]
        related_models = [Categoria, User, TaggedGalleria]

    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super(GalleriaDocument, self).get_queryset().select_related('category', 'user').prefetch_related('tags')


    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Car instance(s) from the related model.
            The related_models option should be used with caution because it can lead in the index
            to the updating of a lot of items.
            """
        if isinstance(related_instance, Categoria):
            return related_instance.galleria_set.all()
        elif isinstance(related_instance, User):
            pass
