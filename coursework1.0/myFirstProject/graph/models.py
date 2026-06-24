from django.db import models
from django.contrib.auth.models import User

class Graph(models.Model):
    GRAPH_TYPE_CHOICES = [
        ('exponent', 'Экспонента (y = eˣ)'),
        ('parabola', 'Парабола (y = x²)'),
        ('abs', 'Модуль (y = |x|)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=20, default='blue')
    thickness = models.IntegerField(default=2)
    scale = models.IntegerField(default=10)
    graph_type = models.CharField(
        max_length=20,
        choices=GRAPH_TYPE_CHOICES,
        default='parabola'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
