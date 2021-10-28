from rest_framework import serializers
#from django.contrib.auth.models import User
from pets.models import CustomUser, Pets
from datetime import date

class UserSerializer(serializers.ModelSerializer):

    is_admin = serializers.ReadOnlyField(source='is_superuser', required=False)
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data, *args, **kwargs):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        return user 

    class Meta:
        model = CustomUser
        fields = ['is_admin', 'username', 'email', 'first_name', 'last_name', 'password']
        write_only_fields = ('password')
        read_only_fiels = ('id')

class PetsSerializer(serializers.ModelSerializer):
    
    age = serializers.SerializerMethodField(required=False)
    birth_date = serializers.DateField(write_only=True, required=True)

    def get_age(self, obj):
        if obj.birth_date:
            try: 
                today = date.today()
                return (today.year - obj.birth_date.year)
            except:
                return None
        else:
            return None

    def validate_name(self, name: str):
        if name.isalpha():
            return name
        raise serializers.ValidationError("must be alphabetic")

    class Meta:
        model = Pets
        fields = ['name', 'is_birth_approximate', 'age', 'id', 'birth_date']
        write_only_fields = ('birth_date')
