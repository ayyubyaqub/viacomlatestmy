from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from viacom_india.sitemaps import Static_Sitemap, Categories_Sitemap, Sub_Categories_Sitemap, Super_Categories_Sitemap

sitemaps = {
    'super_categories': Super_Categories_Sitemap(),
    'categories': Categories_Sitemap(),
    'sub_categories': Sub_Categories_Sitemap(),
    'static': Static_Sitemap()
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
