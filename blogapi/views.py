from rest_framework import generics
from core.models import Posts
from .serializers import PostSerializer



class PostList(generics.ListCreateAPIView): #all posts view
    queryset = Posts.postobjects.all() #return all the post objects that are flagged as published\
    serializer_class = PostSerializer
 

class PostDetail(generics.RetrieveDestroyAPIView): #single post view
    queryset = Posts.objects.all()
    serializer_class = PostSerializer