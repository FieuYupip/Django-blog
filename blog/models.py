from django.urls import reverse
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60,
                            blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list_by_category', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='posts')
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 related_name='posts')
    slug = models.SlugField(max_length=100,
                            blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(
        upload_to='posts/%Y/%m/%d/',
        blank=True)
    views = models.PositiveIntegerField(default=0)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='posts_liked', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
