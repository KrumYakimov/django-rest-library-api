from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


def get_object(model_class, pk):
    return get_object_or_404(model_class, pk=pk)


def serializer_valid(serializer):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



