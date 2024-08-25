from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('edit/<int:comment_pk>/', views.Update.as_view()),
    path('delete/<int:comment_pk>/', views.Destroy.as_view()),
    path('post/<int:post_pk>/add-comment/', views.Store.as_view()),
]
