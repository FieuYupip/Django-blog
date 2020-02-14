from django.shortcuts import render


def home(request):
	context = {
		'section': 'home',
	}
	return render(request,
				'core/index.html',
				context)


def about(request):
	context = {
		'section': 'about',
	}

	return render(request,
				'core/about.html',
				context)


def contact(request):
	context = {
		'section': 'contact',
	}

	return render(request,
				'core/contact.html',
				context)