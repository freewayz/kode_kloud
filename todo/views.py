from django.shortcuts import render, redirect
from serializer import TodoSerializer
from django.http import HttpResponse
from models import Todo
# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, HTMLFormRenderer


class TodoList(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



def kamba_view(request):
    context_info = {}
    return render(request, template_name='todo/todo_list.html', context=context_info)

class TodoApiViewGetPost(APIView):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
    template_name = 'todo/todo_list.html'


    def get(self, request, format='html'):

        todos = Todo.objects.all()
        context = {
            'todos': todos
        }

        serializer = TodoSerializer()
        if format == 'html':
            return Response(context)
        else : 
            serializer = TodoSerializer(data=todos)
            return Response(serializer.data)

    def post(self, request):
        print "Creating new Todo " 
        print request.data
        serializer = TodoSerializer(data=request.data)
        print serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


