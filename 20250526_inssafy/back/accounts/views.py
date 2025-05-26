# accounts/views.py
from django.shortcuts       import get_object_or_404
from rest_framework         import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers       import MultiPartParser, FormParser
from django.contrib.auth    import get_user_model
from .serializers          import UserSerializer, ProfileSerializer

User = get_user_model()

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def user_info(request):
    """
    GET:   내 정보 조회 (id, username, date_joined, biography, profile_image)
    PATCH: biography / profile_image 부분 업데이트
    """
    user = request.user

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PATCH 처리
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        # 저장 후 전체 필드를 다시 보내 주려면 UserSerializer 사용
        full_serializer = UserSerializer(user)
        return Response(full_serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
