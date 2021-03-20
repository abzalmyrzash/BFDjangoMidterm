from django.urls import path
from .views import BookViewSet, JournalViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookViewSet, basename='main')
router.register('journals', JournalViewSet, basename='main')

urlpatterns = [

]

urlpatterns += router.urls
