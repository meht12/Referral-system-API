from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# -----FOR USER REGISTERATION-------
@api_view(['POST'])
def user_registration(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        referral_code = serializer.validated_data.get('referral_code')
        if referral_code:
            referred_by_user = User.objects.filter(referral_code=referral_code).first()
            if referred_by_user:
                referred_by_user.points += 1
                referred_by_user.save()
        serializer.save()
        return Response({'message': 'User registered successfully', 'user_id': serializer.data['id']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# -------FOR USER'S DETAILS---------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    User = request.user
    serializer = UserSerializer(User)
    return Response(serializer.data)

# ---------FOR REFERALLS--------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def referrals(request):
    user = request.user
    referrals = User.objects.filter(referral_code=user.referral_code)
    paginator = Paginator(referrals, 20)  
    page = request.query_params.get('page')
    try:
        referrals_page = paginator.page(page)
    except PageNotAnInteger:
        referrals_page = paginator.page(1)
    except EmptyPage:
        referrals_page = paginator.page(paginator.num_pages)
    serializer = UserSerializer(referrals_page, many=True)
    return Response(serializer.data)



                    # ---------THANK YOU-----------