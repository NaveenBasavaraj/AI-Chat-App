from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from server.models import Server
from server.api.serializers import ServerSerializer
# Create your views here.
class ServerListViewset(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        if category:
            self.queryset.filter(category=category)
        
        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)