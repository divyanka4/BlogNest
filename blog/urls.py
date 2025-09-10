from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),  # Landing page
    path('blog/', views.post_list, name='post_list'),  # Blog list page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('subscribe/', views.subscribe, name='subscribe'),
    path('profile/', views.profile, name='profile'),

    # # Authentication URLs
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    # path('accounts/signup/', views.signup_view, name='signup'),
    
    # Blog post URLs 
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_create, name='post_create'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
