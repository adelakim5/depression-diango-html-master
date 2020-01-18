from rest_framework.routers import DefaultRouter 
from django.urls import path, include 
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet),

urlpatterns = [
    path('posts/', include(router.urls)),
    path('hello',views.hello, name="hello"),
    path('chart', views.chart, name="chart"),
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('reserve', views.reserve, name="reserve"),
    path('diary', views.diary, name="diary"),
    path('accounts/', include('allauth.urls')),
    path('oauth/', views.oauth, name="oauth"),
    path('verification', views.verification, name="verification"),
    path('diary_title', views.diary_title, name="diary_title"),
    path('diary_detail/<int:pk>', views.diary_detail, name="diary_detail"),
    path('diary_delete/<int:pk>', views.diary_delete, name="diary_delete"),
] 