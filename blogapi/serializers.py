from rest_framework import serializers
from core.models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields =('id', 'title', 'author', 'excerpt', 'content', 'status','image')