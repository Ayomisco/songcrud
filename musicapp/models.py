from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.

class Artiste(models.Model):
        first_name = models.CharField(
                max_length=50, null=True, blank=True, verbose_name='First Name')
        last_name = models.CharField(
                max_length=50, null=True, blank=True, verbose_name='Last Name')
        age = models.IntegerField(default=20, blank=True, verbose_name="Age")
        create_at = models.DateField(auto_now_add=True)

        class Meta:
            ordering = ['created_at']
            verbose_name = "Artiste"
            verbose_name_plural = "Artistes"
        
        def __str__(self) -> str:
              return f"{self.first_name}"

class Song(models.Model):
    title = models.TextField(max_length=150, blank=True, verbose_name="Title")
    date_released = models.DateField()
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, verbose_name="Artiste ID")
    create_at = models.DateField(auto_now_add=True)


    class Meta:
            ordering = ['created_at']
            verbose_name = "Song"
            verbose_name_plural = "Songs"
        
    def __str__(self) -> str:
            return f"{self.title}"

class Lyric(models.Model):
    content = models.TextField(verbose_name="Content")
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateField(auto_add_now=True)

    class Meta:
            ordering = ['created_at']
            verbose_name = "Lyric"
            verbose_name_plural = "Lyrics"
        
    def __str__(self) -> str:
            return f"{self.content}"