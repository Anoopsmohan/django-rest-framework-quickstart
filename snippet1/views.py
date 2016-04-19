from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from snippet1.models import Snippet
from snippet1.serializers import SnippetSerializer


class JSONResnponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, *args, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResnponse, self).__init__(content, **kwargs)


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResnponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResnponse(serializer.data, status=201)
        return JSONResnponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    snippet = get_object_or_404(Snippet, id=pk)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResnponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResnponse(serializer.data)
        return JSONResnponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
