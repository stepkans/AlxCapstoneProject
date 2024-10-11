from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Register View
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Here, send activation email with token (e.g., using a token generator)
        return Response({"message": "User registered successfully. Check your email for account activation."}, status=status.HTTP_201_CREATED)

# # Login View
# class LoginView(generics.GenericAPIView):
#     serializer_class = LoginSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']  # Returning the user object
#             refresh = RefreshToken.for_user(user)  # Generating the tokens
#             user = authenticate(email=serializer.data['email'], password=serializer.data['password'])  
#         #Returning the token in the response
#             return Response({
#                 'message': 'Logged in successfully',
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#login View
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']  # Now 'user' will exist in validated_data
        refresh = RefreshToken.for_user(user)  # Generate tokens for the authenticated user

        return Response({
            'message': 'Logged in successfully',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)    