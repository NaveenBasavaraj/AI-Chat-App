from django.shortcuts import render
from rest_framework import viewsets
from server.models import Server
# Create your views here.
class ServerListViewset(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        if category:
            self.queryset.filter(category=category)