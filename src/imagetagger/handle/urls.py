from django.conf.urls.defaults import *
from imagetagger.handle import views

urlpatterns = patterns('',
    (r'^$', views.list_unhandled),
    (r'^(?P<image_id>\d+).jpg$', views.full, {},'image_full'),
    (r'^save/(?P<image_id>\d+).post$', views.save_unhandled_image, {},'save_unhandled_image'),
    (r'^thumb_(?P<image_id>\d+).jpg$', views.thumb, {},'image_thumb'),
)
