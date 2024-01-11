from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .serializers import UserProfileSerializer

# Create your views here.

@api_view(['POST'])
def signup(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    # if username is None or password is None:
        # return Response({'error': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
    # user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error':'invalid credentials'},status=status.HTTP_404_NOT_FOUND)


def home(request):
    return render(request,'home.html')




@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    request.auth.delete()
    logout(request)
    return Response({'success': 'Successfully logged out'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_account(request):
    user = request.user
    user.delete()
    return Response({'success': 'Account deleted successfully'}, status=status.HTTP_204_NO_CONTENT)











# @api_view(['get'])
# def home(request):
#     student_obj=student.objects.all()#query set
#     seriailzer=studentserializer(student_obj,many=True)#many objects so true
#     return Response({'status':200,"payload":seriailzer.data})


# @api_view(['post'])
# def post_student(request):
#     data=request.data
#     print(data)
#     return Response({'status':200,"payload":data})




                                                                                                                                                                                                                                                                                                    