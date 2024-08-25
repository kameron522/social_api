from django.urls import path
from . import views


urlpatterns = [
    path('user/<int:receiver_pk>/follow/', views.Store.as_view()),
    path('user/<int:receiver_pk>/unfollow/', views.Destroy.as_view()),
]
