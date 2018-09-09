from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet
from .views import all_post, single_post, BlogAIPView, BlogDetailAPIView, PostGenericMixinAPIView

router = routers.DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    path('post-list/', all_post, name='all_post'),
    path('post-list/<int:id>/', single_post, name='single_post'),
    path('post-generic-mixin-view/', PostGenericMixinAPIView.as_view()),
    path('post-generic-mixin-view/<int:id>/', PostGenericMixinAPIView.as_view()),
    path('post-class-view/', BlogAIPView.as_view()),
    path('post-class-view/<int:id>/', BlogDetailAPIView.as_view()),
    path('post/', include(router.urls)),
]
