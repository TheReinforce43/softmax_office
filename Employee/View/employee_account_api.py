from Employee.models import User
from Employee.Serializer.Employee_Registration import EmployeeCreateSerializer
from rest_framework.authtoken.views import ObtainAuthToken,APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout,authenticate
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import  Response
from rest_framework import status



class EmployeeRegistrationAPI(APIView):
    def post(self,request):
        serializer=EmployeeCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class EmployeeLoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email=request.data.get('email')
        password=request.data.get('password')

        user=authenticate(email=email, password=password)

        if user is not None:
            login(request,user)
            token,created=Token.objects.get_or_create(user=user)

            if created:
                token.delete()
                token=Token.objects.create(user=user)
            
            return Response(
            {
                'token':token.key,
                'email':user.email,
                'phone_number':user.phone_number,
                'role':user.role
            },
            status=status.HTTP_200_OK
            )
        else:
            return Response({"Message":"Invalid Email or Password"},status=status.HTTP_401_UNAUTHORIZED)
        


class LogOutAPI(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        token_key=request.auth.key 
        token=Token.objects.get(key=token_key)
        token.delete()

        return Response({"message":"User Logout Successfully"},status=status.HTTP_200_OK)    