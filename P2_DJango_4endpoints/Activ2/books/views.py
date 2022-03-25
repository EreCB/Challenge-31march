from functools import partial
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from numpy import allclose

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from books.models import Book, Author
from books.serializers import AuthorSerializer, BookSerializer

# Create your views here.

class RetrieveBooks(APIView):
    permission_classes = (AllowAny,)


    def get(self, request):
        books_list = Book.objects.filter(status=True)
        serializer = BookSerializer(books_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveAuthors(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        authors_list = Author.objects.filter(status=True)
        serializer = AuthorSerializer(authors_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateAuthor(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateBook(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveAuthorAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, author_id):
        author_obj = get_object_or_404(Author, pk=author_id)
        serializer = AuthorSerializer(author_obj)

        return Response(serializer.data)
    
    def put(self, request, author_id):
        author_obj = get_object_or_404(Author, pk=author_id)
        serializer = AuthorSerializer(instance=author_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, author_id):
        author_obj = get_object_or_404(Author, pk=author_id)
        author_obj.status = False
        author_obj.save()

        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)


class RetrieveBookAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, book_id):
        book_obj = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book_obj)

        return Response(serializer.data)
    
    def put(self, request, book_id):
        book_obj = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(instance=book_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, book_id):
        book_obj = get_object_or_404(Book, pk=book_id)
        book_obj.status = False
        book_obj.save()

        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)