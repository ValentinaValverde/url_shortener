from rest_framework import viewsets
from .models import User, Url
from .serializers import UserSerializer, UrlSerializer

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UrlView(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer