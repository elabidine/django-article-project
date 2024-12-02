import uuid
from django.db import models
from django.shortcuts import reverse

from conduit.articles.utils import slug_uuid_generator
# Create your models here.
class Article(models.Model):
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False)          
    slug = models.SlugField(max_length=68,editable=False,unique=True)
    title = models.CharField(db_index=True,max_length=255)
    description = models.TextField(max_length=2000)
    body = models.TextField()
    author = models.ForeignKey("users.Profile",related_name="articles",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
  
class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        to_field="slug",
    )
    body = models.TextField()
    author = models.ForeignKey(
        "users.Profile",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:60] + "..."

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.article.slug})