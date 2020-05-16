from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import UserProfileCreationForm, UserProfile
from django.urls import reverse_lazy


class UserCreateView(SuccessMessageMixin, CreateView):
    model = UserProfile
    form_class = UserProfileCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def get_success_message(self, cleaned_data):
        return self.object.username + ' registration completed successfully'


class UserDetailView(DetailView):
    model = UserProfile
    context_object_name = 'user_profile'


