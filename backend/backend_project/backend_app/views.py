from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


from .models import User, Url
from .serializers import UserSerializer, UrlSerializer


# Create your views here.
# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UrlView(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [IsAuthenticated]

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
          
        try:
           refresh_token = request.data["refresh_token"]
           token = RefreshToken(refresh_token)
           token.blacklist()
           return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
           return Response(status=status.HTTP_400_BAD_REQUEST)