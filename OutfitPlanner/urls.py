from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from OutfitPlanner import views
from OutfitPlanner.views import MainView, All_ClothesView, ClothView, CategoriesView, ClothesOfCategoryView, AboutUs, \
    ChangePasswordView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainView.as_view(), name='MainPage'),
    path('clothes/', All_ClothesView.as_view(), name='clothes'),
    path('clothes/<int:id>/', ClothView.as_view(), name='cloth'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<int:id>/', ClothesOfCategoryView.as_view(), name='category'),
    path('aboutus/', AboutUs.as_view(), name='aboutus'),

    path('login/', LoginView.as_view(template_name='outfit/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='outfit/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('register/', views.register, name='register'),

    path('add/', views.add_cloth, name='add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)