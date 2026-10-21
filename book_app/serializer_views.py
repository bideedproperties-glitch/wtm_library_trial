from django.shortcuts import get_object_or_404
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from drf_spectacular.utils import extend_schema

@extend_schema(request=BookSerializer,responses=BookSerializer)
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def book(request):
    all_book =Book.objects.all().order_by("-id")
    if request.method=="GET":
        book_serializer = BookSerializer(all_book,many=True)
        return Response(book_serializer.data,status=status.HTTP_200_OK)

    elif request.method=="POST":
        book_create_serializer=BookSerializer(data=request.data)
        if book_create_serializer.is_valid():
            book_create_serializer.save()
            return Response(book_create_serializer.data,status=status.HTTP_201_CREATED)
        return Response(book_create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=BookSerializer,responses=BookSerializer)
@api_view(["PUT","PATCH","DELETE"])
@permission_classes([IsAuthenticated])
def book_update(request,pk):
    try:
        get_book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(
            {
                "detail":"Book not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method=="PUT":
        update_book_serializer=BookSerializer(get_book,data=request.data)
        if update_book_serializer.is_valid():
            update_book_serializer.save()
            return Response(update_book_serializer.data,status=status.HTTP_200_OK)

    elif request.method=="PATCH":
        update_book_serializer=BookSerializer(get_book,data=request.data,partial=True)
        if update_book_serializer.is_valid():
            update_book_serializer.save()
            return Response(update_book_serializer.data,status=status.HTTP_200_OK)
        return Response(update_book_serializer.errors,status=status.HTTP_404_BAD_REQUEST)
    
    elif request.method=="DELETE":
        get_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    