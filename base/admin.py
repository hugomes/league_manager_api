from django.contrib import admin

# Register your models here.
from .models import Player, Position, Team

admin.site.register(Player)
admin.site.register(Position)
admin.site.register(Team)

