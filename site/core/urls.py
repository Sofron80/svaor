"""core URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from company.views import index, contact, company, catalog, category


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^contacts/$', contact, name="contacts"),
    url(r'^o-kompanii/$', company, name="company"),
    url(r'^catalog/$', catalog, name="catalog"),
    # url(r'^category/$', catalog, name="category" ),
    url(r'^category/(?P<cat_slug>[\w-]+)/$', category, name='category'),

   # url(r'^category/(?P<cat_slug>[\w-]+)/(?P<tov_slug>[\w-]+)/$', tovar),
]
#handler500 = custom_500

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
