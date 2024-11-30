from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=50, unique=True, verbose_name="Nombre de Usuario")
    password = models.CharField(max_length=128, verbose_name="Contraseña")

    def __str__(self):
        return self.username


class GameData(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="game_data", verbose_name="Jugador")
    best_score = models.IntegerField(default=0, verbose_name="Mejor Puntaje")
    last_score = models.IntegerField(default=0, verbose_name="Último Puntaje")

    def __str__(self):
        return f"{self.player.username} - Mejor: {self.best_score}, Último: {self.last_score}"