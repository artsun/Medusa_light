from rest_framework import serializers

from newsroom.models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('date', 'subject', 'content',)
