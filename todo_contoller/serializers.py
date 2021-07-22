from rest_framework import serializers
from .models import Student,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','is_verified','roles','password']
        #The below line is to make password encrypted so that no one read it . It is the solution for 
        # below written comment.
        extra_kwargs = {
            'password':{'write_only':True}
        }

        #when we add user using json data , the password is added as it is i.e. we can see the paaword. It is not 
        # encrypted . Below function is to pop the password from the data and return rest of the data without password.
        def create(self,validated_data):
            password = validated_data.Meta.pop('password',None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll_no','city','state']

