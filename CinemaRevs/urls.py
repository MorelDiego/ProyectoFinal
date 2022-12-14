"""ProyectoFinalMorel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CinemaRevs import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='Index'),
    path('contacto/', views.contact, name='Contact'),
    path('about/', views.about, name='About'),
    path('reviews/', views.reviews, name='Reviews'),
    path('search/', views.search, name='Search'),
    path('editprofile/', views.editProfile, name='EditProfile'),
    path('reviews_list/', views.ReviewsListView.as_view(), name='ReviewsList'),
    path('reviews_detail/<pk>', views.ReviewsDetailView.as_view(), name='ReviewsDetail'),
    path('reviews_delete/<pk>', views.ReviewsDeleteView.as_view(), name='ReviewsDelete'),
    path('reviews_create/', views.ReviewsCreateView.as_view(), name='ReviewsCreate'),
    path('reviews_update/<pk>', views.ReviewsUpdateView.as_view(), name='ReviewsUpdate'),
    path('signup/', views.SignUpView.as_view(), name='SignUp'),
    path('login/', views.AdminLoginView.as_view(), name='Login'),
    path('logout/', views.AdminLogoutView.as_view(), name='Logout'),
    path('profile/<pk>', views.ProfileView.as_view(), name='Profile'),
    path('addavatar/', views.addAvatar, name='Avatar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)