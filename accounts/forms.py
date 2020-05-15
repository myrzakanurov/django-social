from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password1', 'password2', 'phoneNumber', 'profile_pic')
