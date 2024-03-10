from django.urls import path
from . import views

urlpatterns = [
    path('<str:lang>/', views.weekdays, name='weekdays'),
    path('', views.weekdays, {'lang': 'all'}, name='all_weekdays'),
]
