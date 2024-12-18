from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Company
from .serializers import UserSerializer, CompanySerializer
from rest_framework import status 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication] 
    
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user:
        login(request, user)
        return Response({"message": "Logged in successfully"})
    return Response({"error": "Invalid credentials"}, status=400)

@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@api_view(['POST'])
def register_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')

    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    if password != confirm_password:
        return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({"error": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(email=email, password=password)
    user.save()

    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


# User Detail Page
@login_required
def user_detail(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
    return render(request, 'users/user_detail.html', {'user': user})


# Company Detail Page
@login_required
def company_detail(request):
    company = request.user.company
    return render(request, 'company/company_detail.html', {'company': company})