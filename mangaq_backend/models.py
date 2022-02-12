from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    manga = models.CharField(max_length=100)
    bio = models.TextField()
    character_image = models.ImageField(upload_to='images/', default='images/default.jpg')
    owner = models.ForeignKey(
        'users.User', related_name='characters', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = models.CharField(max_length=100)
    manga_volume = models.CharField(max_length=100)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='quotes')
    manga_image = models.ImageField(upload_to='images/', default='images/default.jpg')
    owner = models.ForeignKey(
        'users.User', related_name='quotes', on_delete=models.CASCADE)

    def __str__(self):
        return self.quote