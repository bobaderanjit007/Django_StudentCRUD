from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('students/', views.student),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
]

