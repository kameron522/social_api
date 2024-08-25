# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/posts/', include('apps.posts.urls', namespace='posts')),
    path('api/accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('api/messages/', include('apps.messages.urls', namespace='messages')),
    path('api/likes/', include('apps.likes.urls', namespace='likes')),
    path('api/comments/', include('apps.comments.urls', namespace='comments')),
    path('api/relations/', include('follows.urls', namespace='follows')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
