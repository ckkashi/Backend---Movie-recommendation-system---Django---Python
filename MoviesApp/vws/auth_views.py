from rest_framework.decorators import api_view
from rest_framework.response import Response

from MoviesApp.models import User
from MoviesApp.serializers import UserSerializer

# api to register new user
@api_view(['POST'])
def register_user(Request):
    data = Request.data
    username = data['username']
    email = data['email']
    password = data['password']
    check_exist = User.objects.filter(email=email)
    if check_exist:
        return Response({"message": "User already exists"})
    else:
        newUser = UserSerializer(data=data)
        if newUser.is_valid():
            newUser.save()
            return Response({"status":"Success","message":"User registered successfully.","data":newUser.data})
        else:
            return Response({"message": "Wrong credentials."})
        
# api to login user
@api_view(['POST'])
def login_user(Request):
    data = Request.data
    email = data['email']
    password = data['password']
    check_exist = User.objects.filter(email=email,password=password).first()
    if check_exist:
        serialized_data = UserSerializer(check_exist)
        return Response({"status":"Success","message":"User loggedin successfully.","data":serialized_data.data})
    else:
        return Response({"message": "Wrong credentials."})

# api to get user by id
@api_view(['GET'])
def get_user_by_id(Request):
    try:
        user_id = Request.GET.get('user_id')
        if user_id != None:  
            check_exist = User.objects.get(id=user_id)
            serialized_data = UserSerializer(check_exist)
            return Response({"status":"Success","message":"User fetched successfully.","data":serialized_data.data})
        else:
            return Response({"status":"Error","message": "Parameter user_id is required."},status=400)
    except:
        return Response({"status":"Error","message": "User not found."},status=404)