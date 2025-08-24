from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from server.models import Server
from server.api.serializers import ServerSerializer
from rest_framework.exceptions import ValidationError, AuthenticationFailed
# Create your views here.
class ServerListViewset(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        user_id = request.query_params.get("user_id")
        server_id = request.query_params.get("server_id")
        if category:
            self.queryset=self.queryset.filter(category=category)
        if user_id:
            if not request.user.is_authenticated:
                raise AuthenticationFailed()
            user_id = request.user.id
            self.queryset=self.queryset.filter(member=user_id)
        if server_id:
            try:
                self.queryset=self.queryset.filter(id=server_id)
                if not self.queryset.exists():
                    raise ValueError
            except ValueError:
                raise ValidationError(detail=f"server_id {server_id} not found")
        
        if qty:
            self.queryset=self.queryset[:int(qty)]
        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)