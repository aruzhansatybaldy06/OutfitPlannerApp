from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'OutfitPlanner'
admin.site.site_title = 'OutfitPlanner'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OutfitPlanner.urls')),
]
