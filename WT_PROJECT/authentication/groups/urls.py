from django.conf.urls import url

from . import views

app_name = 'groups'

urlpatterns = [
    url("^$", views.ListGroups.as_view(), name="all"),
    url("^new/$", views.CreateGroup.as_view(), name="create"),
    url("^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
    url("join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    url("leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
]
