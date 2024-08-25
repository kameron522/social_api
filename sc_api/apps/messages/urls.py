from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('', views.Index.as_view()),
    path('send/<int:receiver_pk>/', views.Store.as_view()),
    path('update/<int:pk>/', views.Update.as_view()),
    path('delete/<int:pk>/', views.Destroy.as_view()),
    path('my-messages/', views.UserMessages.as_view()),
    path('<int:pk>/delete/', views.DelImg.as_view()),
    path('<int:pk>/', views.Show.as_view()),
]
