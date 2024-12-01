from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Player(AbstractUser):
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

class GameData(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='game_data')
    best_score = models.IntegerField(default=0, verbose_name="Mejor Puntaje")
    last_score = models.IntegerField(default=0, verbose_name="Último Puntaje")
    played_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Última Partida")

    def __str__(self):
        return f"{self.player.username} - Mejor: {self.best_score}"

    class Meta:
        verbose_name = "Datos de Juego"
        verbose_name_plural = "Datos de Juegos"