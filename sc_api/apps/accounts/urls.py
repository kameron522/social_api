from django.urls import path
from . import views
from rest_framework.authtoken import views as authtoken_views

app_name = 'accounts'

urlpatterns = [
    path('', views.Index.as_view()),
    path('create/', views.Store.as_view()),
    path('update/<int:pk>/', views.Update.as_view()),
    path('delete/<int:pk>/', views.Destroy.as_view()),
    path('token-auth/', authtoken_views.obtain_auth_token),
    path('delete-token/', views.DeleteToken.as_view()),
]
