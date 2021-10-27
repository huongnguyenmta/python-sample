from rest_framework import serializers
from userpost.models import Post

from datetime import datetime


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     content = serializers.CharField(allow_blank=True)
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     user = serializers.IntegerField()

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.user_id = validated_data.get("user_id", instance.user_id)
#         instance.updated_at = datetime.today()

#         instance.save()
#         return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "updated_at", "user"]
