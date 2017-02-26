from django.conf.urls import include, url
from django.contrib import admin
from blog import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'peterchengsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.IndexView.as_view()),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls', namespace='ueditor', app_name='ueditor')),
]
