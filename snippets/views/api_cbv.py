__author__ = 'peter'

from rest_framework.views import APIView
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status


class SnippetList(APIView):

    """
    Class based view list or create a new snippet
    """


    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True) # create our Snippet serializer
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


