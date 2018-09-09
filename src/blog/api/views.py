from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from blog.models import Post
from .serializers import PostSerializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


@csrf_exempt
def all_post(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        json_parser = JSONParser()
        posts = json_parser.parse(request)
        serializer = PostSerializers(data=posts)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def single_post(request, id=None):
    post = get_object_or_404(Post, id=id)
    if request.method == "GET":
        serializer = PostSerializers(post)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "PUT":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = PostSerializers(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=204)


class BlogAIPView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = PostSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BlogDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist as e:
            return Response({'error': 'Employee information not found'}, status=404)

    def get(self, request, id=None):
        post = self.get_object(id=id)
        serializer = PostSerializers(post)
        return Response(serializer.data)

    def put(self, request, id=None):
        post = self.get_object(id=id)
        data = request.data
        serializer = PostSerializers(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        post = self.get_object(id=id)
        post.delete()
        return HttpResponse(status=204)

