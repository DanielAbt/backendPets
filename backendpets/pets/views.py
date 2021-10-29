
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

# Create your views here.
class login(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        print(user)
        # If user is registed, return seccion user information.
        if user is not None and user.is_active:
            #login(request, user)
            dataUser = dict(user=UserSerializer(user).data)
            print(user.is_authenticated)
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
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class petsList(generics.GenericAPIView):
    #permission_classes = [IsAuthenticated]

    queryset = Pets.objects.all()
    serializer_class = PetsSerializer

    def filter_queryset(self):
        petsNameFilter = self.request.GET.get('name', None)
        petsMinAge = self.request.GET.get('min_birth_date', None)
        petsMaxAge = self.request.GET.get('max_birth_date', None)
        petsList = self.get_queryset()
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
        ### check user is admin
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