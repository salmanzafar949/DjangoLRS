from rest_framework import generics
from .seriallizers import BlogSeriallizer
from .models import Blog

class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSeriallizer
