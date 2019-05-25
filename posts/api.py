from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .serializers import PostSerializer
from .models import Post


class PostViewAPI(GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = PostSerializer(qs, many=True)
        data = serializer.data
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        request_data = request.data.dict()
        request_data['user'] = request.user.id
        serializer = PostSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
