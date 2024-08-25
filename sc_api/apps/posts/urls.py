from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.Index.as_view()),
    path('create/', views.Store.as_view()),
    path('update/<int:pk>/', views.Update.as_view()),
    path('delete/<int:pk>/', views.Destroy.as_view()),
    path('<int:pk>/', views.Show.as_view()),
    
]
