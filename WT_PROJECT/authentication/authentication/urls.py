
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('log_app.urls')),
    path("groups/",include("groups.urls", namespace="groups")),
    path("posts/", include("posts.urls", namespace="posts")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
