from rest_framework import serializers
from .models import Character, Quote

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.HyperlinkedRelatedField(view_name='character_detail', read_only=True)

    character_id = serializers.PrimaryKeyRelatedField(
        queryset = Character.objects.all(),
        source = 'character'
    )

    class Meta:
        model = Quote
        fields = ('id', 'quote', 'manga_volume', 'character', 'character_id', 'manga_image')

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    quote_id = serializers.HyperlinkedRelatedField(view_name='quote_detail', read_only=True)

    quotes = QuoteSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = ('id', 'name', 'manga', 'bio', 'quotes', 'character_image', 'quote_id')