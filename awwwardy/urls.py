
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/(?P<user_id>\d+)?$', views.profile, name='profile'),
    url(r'^update/profile$', views.updateprofile, name='updateprofile'),
    url(r'^project/(\d+)/$',views.ratings_views,name='project'),
    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<post_id>[0-9]+)/$', views.ratings_views, name='add_review'),
    url(r'^search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

