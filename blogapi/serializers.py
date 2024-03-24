from rest_framework import serializers
from core.models import Posts, Category

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields =('id', 'title', 'author', 'excerpt', 'content', 'status','image')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=('id','name','thumbnails','description')