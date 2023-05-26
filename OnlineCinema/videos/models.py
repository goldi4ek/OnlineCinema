from django.db import models
from django.core.validators import FileExtensionValidator


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Чоловік'),
        (FEMALE, 'Жінка')
    ]

    name = models.CharField(max_length=50)
    photo = models.ImageField(
                              upload_to='actors_photos/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])

    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    sequence = models.ImageField(
        upload_to='film_sequence/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])

    description = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    video_file_link = models.TextField()

    def __str__(self):
        return self.title