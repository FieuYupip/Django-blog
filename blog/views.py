from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category
from .forms import PostForm


def post_list(request, category_slug=None):

	q = request.GET.get('q', None)

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		object_list = Post.objects.filter(category=category)
	
	elif q is None or q is "":
		object_list = Post.objects.all()
	else:
		object_list = Post.objects.filter(Q(title__contains=q) | Q(content__contains=q))

	paginator = Paginator(object_list, 1)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {
		'posts': posts,
		'section': 'blog',
	}

	return render(request,
				'blog/post/list.html',
				context)


def post_detail(request, post_slug):
	post = get_object_or_404(Post, slug=post_slug)
	session_key = f'viewed_post_{post.id}'
	if not request.session.get(session_key, False):
		post.views += 1
		post.save()
		request.session[session_key] = True


	context = {
		'post': post,
	}

	return render(request,
				'blog/post/detail.html',
				context)


def post_edit(request, post_id=None):
	post = get_object_or_404(Post, id=post_id)

	if request.method == 'POST':
		post_form = PostForm(request.POST, instance=post)

		if post_form.is_valid():
			post_form.save()
			messages.success(request, 'Cập nhật thành công!')
		else:
			messages.error(request, 'Error!')
	else:
		post_form = PostForm(instance=post)
	
	context = {
		'post': post,
		'post_form': post_form,
	}

	return render(request,
				'blog/post/edit.html',
				context)



