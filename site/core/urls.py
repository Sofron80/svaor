from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from company.views import index, contact, company, catalog, category, tovar, zakaz, error

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^zakaz/$', zakaz, name="zakaz"),
    url(r'^contacts/$', contact, name="contacts"),
    url(r'^o-kompanii/$', company, name="company"),
    url(r'^catalog/$', catalog, name="catalog"),
    url(r'^category/(?P<cat_slug>[\w-]+)/$', category, name='category'),
    url(r'^category/(?P<cat_slug>[\w-]+)/(?P<tov_slug>[\w-]+)/$', tovar),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
