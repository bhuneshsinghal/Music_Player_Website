from rest_framework import serializers
from .models import CustomUser
import datetime
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','last_name','date_of_birth','gender']

    def validate(self,data):
        name_string = data['first_name'].join(data['last_name'])
        if data['first_name'] is not None or data['last_name'] is not None :
            for n in name_string:
                if n.isdigit():
                    return serializers.ValidationError({'error':'name cannot contains numeric digit'})
        if data['date_of_birth'] is not None:
            today = datetime.date.today()
            if data['date_of_birth']==today:
                return serializers.ValidationError({"error":"Today date cannot be your date of birth"})

class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'},write_only=True)


    def validate(self,data):
        new_password = data['new_password']
        confirmation_password = data['confirmation_password']
        if new_password!=confirmation_password:
            return serializers.ValidationError({'error':"Entered Password is not matching"})





# def check_date_of_birth(value):
#     today = datetime.date.today()
#     if value==today:
#         return serializers.ValidationError({'error':'Current Date cannot be your date of birth'})
    
            