from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sell/', views.sell, name='sell'),
    path('sell/confirm/', views.confirm, name='confirm'),
    path('<int:chair_id>/', views.detail, name='detail'),
    path('<int:chair_id>/buy', views.buy, name='buy')
]
