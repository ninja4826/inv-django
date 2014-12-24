from django.conf.urls import patterns, url

from workorder import views

urlpatterns = patterns('',
    url(r'^(?P<workorder_id>\d+)/edit/$', views.edit_work_items, name="edit_work_items"),
)