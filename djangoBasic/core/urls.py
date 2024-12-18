from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from core.admin import admin
from .views import UserViewSet, CompanyViewSet, company_detail, login_view, logout_user, register_view, user_detail

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('companies', CompanyViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user/', user_detail, name='user_detail'),
    path('company/', company_detail, name='company_detail'),
]