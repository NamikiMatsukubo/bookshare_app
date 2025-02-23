from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLogoutView

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.timeline, name='timeline'),
    path('create/', views.post_creat, name='post_creat'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('user/<str:username>/', views.user_page, name='user_page'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('register/', views.register, name='register'),
]   