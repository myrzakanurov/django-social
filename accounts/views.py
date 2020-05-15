from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import UserProfileCreationForm, UserProfile
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

