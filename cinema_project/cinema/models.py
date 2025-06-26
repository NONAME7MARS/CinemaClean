# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()  # в хвилинах
    rating = models.FloatField()
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')  # Фото
    release_year = models.PositiveIntegerField(null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class Hall(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'Зал {self.number}'

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.movie.title} - {self.date} {self.start_time}'

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Куплений', 'Куплений'),
        ('Заброньований', 'Заброньований'),
    ]
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="Заброньований")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="tickets")

    def __str__(self):
        return f"Місце {self.seat_number} ({self.status})"

class Dashboard(models.Model):
    class Meta:
        verbose_name_plural = "📊 Аналітика"
        managed = False  # ❗ не створює таблицю в БД

    def __str__(self):
        return "Аналітика"

class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'movie')

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField("Відгук")
    rating = models.PositiveSmallIntegerField("Рейтинг", choices=[(i, f"{i} ⭐") for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} – {self.movie.title} ({self.rating})"


class BonusTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    amount = models.IntegerField()  # + чи -
    balance_after = models.IntegerField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username}: {self.amount} балів ({self.balance_after})"
