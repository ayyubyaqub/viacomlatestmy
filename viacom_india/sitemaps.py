from django.contrib.sitemaps import Sitemap
from categories.models import Categories, SuperCategory
from django.urls import reverse
from home.models import SubCategories


class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['homepage', 'create_video', 'about-us', 'works', 'marketplace', 'contactus', 'contact-us', 'all-industry', 'categories', 'creators', 'subscription', 'all-terms-and-condition']

    def location(self, item):
        return reverse(item)


class Super_Categories_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return SuperCategory.objects.all()

    def location(self, obj):
        return "/"+obj.slug


class Categories_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.1

    def items(self):
        return Categories.objects.all()

    def location(self, obj):
        return "/"+obj.slug


class Sub_Categories_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.4

    def items(self):
        return SubCategories.objects.all()

    def location(self, obj):
        return "/"+obj.slug
