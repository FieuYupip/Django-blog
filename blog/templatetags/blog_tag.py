from django import template 
from ..models import Post, Category


# https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/#inclusion-tags

register = template.Library()


@register.inclusion_tag('includes/category_header.html')
def category_header():
	return { 'categories': Category.objects.all() }


@register.inclusion_tag('blog/includes/category_aside.html')
def category_aside():
	return { 'categories': Category.objects.all() }


@register.inclusion_tag('blog/includes/recent_posts.html')
def recent_posts():
	posts = Post.objects.all()[:3]
	return { 'posts': posts }


