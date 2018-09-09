from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'description',
            'image',
            'create_at',
            'update_at'
        ]