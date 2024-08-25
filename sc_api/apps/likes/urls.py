from . import views
from django.urls import path

app_name = 'likes'

urlpatterns = [
    path('delete/<int:like_pk>/', views.Destroy.as_view()),
    path('post/<int:post_pk>/add-like/', views.Store.as_view()),
]
