from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action=='list' or self.action=='retrieve':
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Book.objects.all()


class JournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalSerializer

    def get_permissions(self):
        if self.action=='list' or self.action=='retrieve':
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Journal.objects.all()
