from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','name','email','password','refferal_code']
        extra_kwargs = {'password':{'write_only': True}}
        