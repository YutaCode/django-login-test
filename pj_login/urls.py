from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetConfirmView

index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(index_view), name="index"),
    path('password_reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name="registration/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('', include("django.contrib.auth.urls")),
]
