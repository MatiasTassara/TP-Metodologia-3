from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('info/<int:id>',views.info,name='info'),
]