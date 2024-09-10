from django.contrib import sitemaps
from django.urls import reverse
from course.models import Courses


class RootStaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            "root:home",
            "root:contact",
            "root:about",
            "root:events",
            "course:courses",
            "course:trainers",
            "accounts:login",
            ]

    def location(self, item):
        return reverse(item)
    

class RootDynamicViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Courses.objects.filter(status=True)

    def location(self, item):
        return f"/course/detail/{item.id}"