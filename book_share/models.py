from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Post(models. Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='投稿者')
    image = models.ImageField(upload_to='post_image/', verbose_name='本の写真')
    content = models.TextField(max_length=1000, verbose_name='感想')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')
    book_title = models.CharField(max_length=255, verbose_name='本の題名')
    book_author = models.CharField(max_length=255, verbose_name='著者')

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿'
        ordering = ['-created_at']


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} follows {self.following}"

