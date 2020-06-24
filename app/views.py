from django.shortcuts import get_object_or_404
from rest_framework import views, viewsets, status
from rest_framework.response import Response

from app.models import Post, Comment
from app.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpVoteView(views.APIView):
    """View for counting the number of upvotes"""

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        data = {"amount_of_upvotes": post.amount_of_upvotes + 1}
        serializer = PostSerializer(post, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
