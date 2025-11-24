
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp3.views import SignUpView

urlpatterns = [
    # (We won't use the admin site in this assignment, but leaving it doesn’t hurt)
    path('admin/', admin.site.urls),

    # App URLs
    path('', include('myapp3.urls')),

    # Auth: login/logout using Django’s built-in views (no superuser needed)
    path('login/',  auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Signup (custom view)
    path('signup/', SignUpView.as_view(), name='signup'),
]


