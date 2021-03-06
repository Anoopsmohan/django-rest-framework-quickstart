__author__ = 'anoop.sm'

from django.contrib.auth.models import User
from rest_framework import serializers
from snippet5.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets5 = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets5')
