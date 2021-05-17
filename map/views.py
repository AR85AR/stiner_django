from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from rest_framework import viewsets, request
from rest_framework.response import Response

# from account.models import UserRole
from account.models import UserRole
from map.api.serializers import PointSerializer, LocationMapSerializer
from map.forms import FormularzRejestracji
from map.models import Point, Coordinates, NewsletterEmail, News
from shop.models import Category
from trails.models import Trail
from trails.views import MethodTrail
from user_trails.models import UserTrail


class Map(View, MethodTrail):
    template_name = 'map/map_index.html'
    category = Category.objects.all()
    coordinates = Coordinates.objects.all()
    points = Point.objects.all()
    trails = Trail.objects.all()
    news = News.objects.all()
    country = [value for key, value in Trail.get_country_trail(Trail)]

    def get(self, request):
        # ---------------------------------------
        # if (str(request.user) != 'AnonymousUser'):
        #     self.userRole = UserRole.objects.filter(user=request.user).first()
        # ---------------------------------------
        return render(request, self.template_name, {'category': self.category, 'coordinates': self.coordinates,
                                                    'coordinatesLength': len(self.coordinates), 'news': self.news[:3],
                                                    'newsBig': self.news[3:5], 'pointLength': len(self.points),
                                                    'trailLength': len(self.trails), 'countryLength': len(self.country),
                                                    'country': self.country})

    def add_to_Newsletter(self, request):
        if (len(NewsletterEmail.objects.filter(email=request.POST.get('email'))) == 0):
            NewsletterEmail.objects.create(email=request.POST.get('email'))

    def post(self, request, *args, **kwargs):
        """Obsługa formularzy na stronie głównej."""
        if request.POST.get('email'):
            self.add_to_Newsletter(request)
            return render(request, self.template_name, )
        else:
            search = self.search_trail(request, 'all_trail')
            return render(request, 'trails/all_trails/all_trails.html',
                          {'search': search, 'city': self.get_city(), 'top_rate': self.get_top_rate_trails(),
                           'popular_trail': self.get_wached_trails(),
                           'type_trail': self.get_type_trail(), 'region_trail': self.get_region_trail(),
                           'country_trail': self.get_country_trail()})


class PointViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        points = Point.objects.filter(type=params['pk'])
        serializer = PointSerializer(points, many=True)
        return Response(serializer.data)


class MapCenterViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = LocationMapSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        location = Coordinates.objects.filter(name=params['pk'])
        serializer = LocationMapSerializer(location, many=True)
        return Response(serializer.data)


class UserFormView(View):
    """Rejestracja użytkownika"""
    form_class = FormularzRejestracji
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('../')

        return render(request, self.template_name, {'form': form})


class MapFullScreen(View):
    template_name = 'map/map.html'
    coordinates = Coordinates.objects.all()
    country = [value for key, value in Trail.get_country_trail(Trail)]

    def get(self, request):
        # ---------------------------------------
        # if (str(request.user) != 'AnonymousUser'):
        #     self.userRole = UserRole.objects.filter(user=request.user).first()
        # ---------------------------------------
        return render(request, self.template_name,
                      {'coordinates': self.coordinates, 'countryLength': len(self.country), 'country': self.country})


class FavoriteList(ListView):
    template_name = 'favorite/favorite.html'
    model = Trail


class FavoritePoint(ListView):
    template_name = 'favorite/favorite_point.html'
    model = Point


class FavoriteTrail(ListView):
    template_name = 'favorite/favorite_trail.html'
    model = Trail


class FavoriteYourTrail(ListView):
    template_name = 'favorite/favorite_your_trail.html'
    model = UserTrail

class DoneList(ListView):
    template_name = 'done/done.html'
    model = Trail
