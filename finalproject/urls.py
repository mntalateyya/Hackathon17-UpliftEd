"""UpliftEd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import UpliftEd.views
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^UpliftEd/', include('UpliftEd.url')),
    url(r'^$',UpliftEd.views.home, name='home'),
    url(r'^index/',UpliftEd.views.index, name='index'),
    url(r'^user/(?P<id>[0-9]+)/',UpliftEd.views.user, name = 'user'),
    url(r'^category/(?P<id>[a-z]+)/',UpliftEd.views.category, name = 'category'),
    url(r'^video/',UpliftEd.views.video, name = 'video'),
    url(r'^playlist/(?P<id>[0-9]+)/',UpliftEd.views.playlist, name = 'playlist'),
    url(r'^upload_video/',UpliftEd.views.upload_video, name = 'upload_video'),
    url(r'^postupload', UpliftEd.views.post_upload, name='post_upload'),
    url(r'^postsignup', UpliftEd.views.post_signup, name='post_signup'),
    url(r'^signin/',UpliftEd.views.signin, name = 'signin'),
    url(r'^video/(?P<id>[0-9]+)/upvote',UpliftEd.views.upvote, name = 'upvote'),
    url(r'^video/(?P<id>[0-9]+)/downvote',UpliftEd.views.downvote, name = 'downvote'),
    url(r'^subscribe/(?P<id>[0-9]+)/$',UpliftEd.views.subscribe, name = 'subscribe')
]
