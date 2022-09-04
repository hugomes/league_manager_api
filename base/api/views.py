from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Player
from .serializes import PlayerSerializaer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/players',
        'GET /api/players/:id'
        ]
    return Response(routes)


@api_view(['GET'])
def getPlayers(request):
    players = Player.objects.all()
    serialize = PlayerSerializaer(players, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def getPlayer(request,pk):
    player = Player.objects.get(id=pk)
    serialize = PlayerSerializaer(player, many=False)
    return Response(serialize.data)

