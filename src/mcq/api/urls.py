from django.urls import path, include
from rest_framework import routers
from .views import ChoiceModelViewSets, QuestionModelViewSets


router = routers.DefaultRouter()
router.register('', ChoiceModelViewSets)

urlpatterns = [
    path('choice/', include(router.urls)),
    # path('question/', QuestionModelViewSets.as_view({'get': 'list', 'post': 'create'}))
]



