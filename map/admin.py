from django.contrib import admin
from .models import Point, Opinion_about_Point, Coordinates, NewsletterEmail, Galery, News, AdvertisementNews, Country

admin.site.register(Point)
admin.site.register(Opinion_about_Point)
admin.site.register(Coordinates)
admin.site.register(NewsletterEmail)
admin.site.register(Galery)
admin.site.register(News)
admin.site.register(AdvertisementNews)
admin.site.register(Country)