from rest_framework import serializers
from server.models import Category, Server, Channel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"

class ServerSerializer(serializers.ModelSerializer):
    channel_server = ChannelSerializer(many=True)
    class Meta:
        model = Server
        fields = "__all__"
