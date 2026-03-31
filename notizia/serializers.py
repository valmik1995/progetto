from rest_framework import serializers
from .models import Notizia

class NotiziaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notizia
        fields = ('id', 'title', 'description', 'comune')
