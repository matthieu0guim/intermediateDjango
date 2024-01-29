from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('logout/', authentication.views.logout_user, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("home/", blog.views.home, name="home"),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('change_password/', PasswordChangeView.as_view(
        template_name='blog/change_password.html',
        success_url="password_change_done",
    ), name="change-password"),
    path('change_password/password_change_done/', blog.views.password_change_done, name='password-change-done')
]
