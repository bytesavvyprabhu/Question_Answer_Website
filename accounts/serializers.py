from rest_framework import serializers
from . models import User,question_model, answer_model
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import uuid
from django.utils import timezone

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk','email', 'full_name', 'contact_number','about',
        'date_of_birth','company_name','designation']
        read_only_fields = ('pk', 'email')



class question_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = question_model
        fields = '__all__'

class answer_serializer(serializers.ModelSerializer):
    a = question_serializer(many=True,read_only=True)
    class Meta:
        model = answer_model
        fields = '__all__'

class Questio_serializer(serializers.ModelSerializer):
    answer = question_serializer(many=True,read_only=True)
    class Meta:
        model = answer_model
        fields = ['question_title','question_description','technology_name',
        'user_question','answer']
        #read_only_fields = ('answer',)
        #depth =1

        
        
    
    

