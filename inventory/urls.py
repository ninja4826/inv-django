from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>\d+)/$', views.show, name='show'),
    url(r'^new/', views.new_product, name="new_product"),
    url(r'^(?P<product_id>\d+)/delete/$', views.delete, name="delete"),
)