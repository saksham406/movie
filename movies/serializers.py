from curses import meta
from zlib import MAX_WBITS
from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    image= serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Moviedata
        fields=[ 'id', 'name','duration','ratings','typ','image']

