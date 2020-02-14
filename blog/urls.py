from django.urls import path
from . import views


urlpatterns = [
	path('blog/', views.post_list, name='post_list'),
	path('blog/<slug:post_slug>/', views.post_detail, name='post_detail'),
	path('category/<slug:category_slug>/', views.post_list, name='post_list_by_category'),

	path('blog/edit/<int:post_id>/', views.post_edit, name='post_edit'),
]


