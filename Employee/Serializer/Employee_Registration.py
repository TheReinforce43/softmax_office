from rest_framework import serializers
from Employee.models import User 


class EmployeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=User 
        fields = ['id','email', 'name', 'phone_number', 'role', 'password']
        extra_kwargs={'password':{'write_only':True}}

    
    def create(self,validated_data):

        try:
            user=User.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                phone_number=validated_data['phone_number'],
                role=validated_data['role'],
                password=validated_data['password'],
            )
            return user 
        except Exception as exception:
            raise serializers.ValidationError("An error occurred while creating the user: {}".format(str(exception)))

class EmployeeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['id','email', 'name', 'phone_number', 'role']

    