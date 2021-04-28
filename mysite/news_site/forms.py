'''from django import forms


class NewsIndividual(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        return data'''

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, PriorityForUser, UrlsTable


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', )


class UserProfileForm(forms.Form):
    all_urls = forms.ModelMultipleChoiceField(
        queryset=UrlsTable.objects.all().order_by('url'),
        widget=forms.CheckboxSelectMultiple,
        label="",
        label_suffix='',
    )
