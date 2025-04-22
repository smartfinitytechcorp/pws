from django.urls import path
# from .views import *
from . import views
urlpatterns = [
    path('', views.WritingModel, name='WritingModel'),
    path('reviews/', views.All_reviews, name='all_reviews'),
    path('', views.Subscribe, name='subscribe'),
    path('upload-csv/', views.profile_upload, name="profile_upload"),
]