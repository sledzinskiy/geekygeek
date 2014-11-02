from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^home/', 'KolyAndron.view.home', name='home'),
     url(r'^$', 'KolyAndron.view.home', name='home'),
     url(r'^myprofile/', 'KolyAndron.view.myprofile', name='myprofile'),
     url(r'^groups/', 'KolyAndron.view.groups', name='groups'),
     url(r'^groups/(\d{1,2})/', 'KolyAndron.view.group', name='group'),
     url(r'^geeks/', 'KolyAndron.view.geeks', name='geeks'),
     url(r'^news/', 'KolyAndron.view.news', name='news'),
     url(r'^news/(\d{1,2})/', 'KolyAndron.view.newsdetail', name='newsdetail'),
     url(r'^about/', 'KolyAndron.view.about', name='about'),
     # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
