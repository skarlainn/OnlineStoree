from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserEditForm
from config import settings
from users.forms import UserRegisterForm
from users.models import User
from .models import User


class MyView(LoginRequiredMixin, TemplateView):
    template_name = 'my_template.html'
    login_url = reverse_lazy('custom_login')


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Подтверждение регистрации"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        recipient_list = [user_email]
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, from_email, recipient_list)

class UserProfileUpdateView(UpdateView):
    model = User
    form_class = CustomUserEditForm
    template_name = 'users/profile_edit.html'
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy('users:profile_detail')
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('users:profile_detail', kwargs={'pk': self.kwargs['pk']})

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile_detail.html'
    login_url = reverse_lazy("users:login")
    context_object_name = 'user'