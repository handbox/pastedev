from django.contrib.auth.models import User, Group
from rest_framework import serializers

from pastedev.paste.models import Paste


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PasteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paste
        fields = ('id', 'content', 'title')
