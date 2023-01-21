from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='posts'

urlpatterns = [
    url("^$", views.PostList.as_view(), name="all"),
    url("new/$", views.CreatePost.as_view(), name="create"),
    url("by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    url("by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    url("delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)
