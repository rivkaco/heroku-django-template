from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^post_new/', views.post_new, name="post_new"),
    url(r'^register/', views.register, name="register"),

    url(r'^login/', authviews.login, name='login'),
    # url(r'^accounts/auth/$', 'views.auth_view'),
    url(r'^logout/', authviews.logout, {'next_page': '/billboard'},  name='logout'),
    # url(r'^registered/', views.registered, name = 'registered'),
    # url(r'^accounts/invalid/$', 'django_text.views.invalid_login'),

]