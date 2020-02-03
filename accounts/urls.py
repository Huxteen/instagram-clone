
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('profile/<int:post_id>', views.delete_profile, name='delete_profile'),
    path('update-profile/<int:post_id>', views.update_profile, name='update_profile'),
]