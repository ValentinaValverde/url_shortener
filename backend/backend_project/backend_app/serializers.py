from .models import Url, User
from rest_framework import serializers

# User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Url
        fields = ["title", "long_url", "short_url", "user_id"]
