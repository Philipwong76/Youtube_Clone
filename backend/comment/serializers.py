from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class meta:
        model = Comment
        fields = ['id', 'user', 'video_id', 'text', 'likes', 'dislikes']
        depth = 1