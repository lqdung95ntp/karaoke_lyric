from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search/<song_slug>', views.search, name='search'),
    path('personal', views.personal, name='personal'),
]