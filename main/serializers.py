from rest_framework import serializers
from .models import Book, Journal


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = "__all__"


class JournalSerializer(serializers.Serializer):
    class Meta:
        model = Journal
        fields = "__all__"
