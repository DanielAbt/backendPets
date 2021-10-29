
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions
from .serializers import PetsSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from .models import Pets
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

class loginUser(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        # If user is registed, return seccion user information.
        if user is not None and user.is_active:
            login(request, user)
            dataUser = dict(user=UserSerializer(user).data)
            return JsonResponse(dataUser)
        
        # If user isn't registed, return 401 "UNAUTHORIZED".
        return HttpResponse(status=401)

class signin(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(dict(user=serializer.data), status=201)
        return JsonResponse(serializer.errors, status=400)


class petsList(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = Pets.objects.all().order_by('name', '-birth_date')
    serializer_class = PetsSerializer

    def filter_queryset(self):
        petsNameFilter = self.request.GET.get('name', None)
        petsMinAge = self.request.GET.get('min_birth_date', None)
        petsMaxAge = self.request.GET.get('max_birth_date', None)
        petsList = self.queryset
        if petsNameFilter:
            petsList = petsList.filter(name__contains=petsNameFilter)
        if petsMinAge:
            petsList = petsList.filter(birth_date__gte=petsMinAge)    
        if petsMaxAge:
            petsList = petsList.filter(birth_date__lte=petsMaxAge)        
        return petsList

    def get(self, request, *args, **kwargs):
        print('list: ', request.user)
        queryset = self.filter_queryset()
        page = request.GET.get('page')
        try: 
            page = self.paginate_queryset(queryset)
        except Exception as e:
            page = []
            data = page
            return HttpResponse(status=404)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = PetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self,*args, **kwargs):
        ### check if user is admin
        # if request.user.is_superuser:
        try:
            pet = Pets.objects.get(id=kwargs.get('id'))
            pet.delete()
            return HttpResponse(status=200)
        except pet.DoesNotExist:
            return HttpResponse(status=404)
        ##
        # else:
        #   return HttpResponse(status=401)