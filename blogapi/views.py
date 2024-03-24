from rest_framework import generics
from core.models import Posts,Category
from .serializers import PostSerializer, CategorySerializer



class PostList(generics.ListCreateAPIView): #all posts view
    queryset = Posts.postobjects.all() #return all the post objects that are flagged as published\
    serializer_class = PostSerializer
 

class PostDetail(generics.RetrieveDestroyAPIView): #single post view
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CategoryDetail(generics.RetrieveDestroyAPIView): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer