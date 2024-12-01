from django.urls import path

from . import views

app_name = "gestioncolloque"

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('gallery', views.gallery, name = 'gallery'),
    path('faq', views.faq, name = 'faq'),
    path('pricing', views.pricing, name = 'pricing'),
    path('sponsors', views.sponsors, name = 'sponsors'),
    path('venue', views.venue, name = 'venue'),
    path('speakers', views.speakers, name = 'speakers'),
    path('schedule', views.schedule, name = 'schedule'),
    path('blog', views.blog, name = 'blog'),
    path('blog-detail', views.blog_detail, name = 'blog_detail'),
    path('contact', views.contact, name = 'contact'),


]