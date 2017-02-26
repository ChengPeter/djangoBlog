from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<article_id>\d+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<cate_id>\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', views.ArchiveView.as_view(), name='archive'),
    url(r'^about/$',  views.About, name='about'),
    url(r'^contact/$',  views.Contact, name='contact'),
    url(r'^list/$', views.ArticleListView.as_view(), name='list'),
    url(r'^search/$', views.Article_search, name='search'),
    url(r'^submit/$', views.SendMail, name='submit'),
    url(r'^feed/$', views.RSSFeed(), name='rss'),
]
