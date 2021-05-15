# -*- coding: utf-8 -*-
'''from django import forms


class NewsIndividual(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        return data'''
import json
from json import JSONDecodeError

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UrlsTable
import re

DANGER_SYMBOLS = set('#')


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password:', widget=forms.PasswordInput, label_suffix='')
    password2 = forms.CharField(label='Repeat password:', widget=forms.PasswordInput, label_suffix='')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserTagsForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['user_tags']
        widgets = {
            'user_tags': forms.Textarea(),
        }

    def clean_user_tags(self):
        try:
            pd = json.loads(self.cleaned_data.get('user_tags'))
        except JSONDecodeError:
            raise forms.ValidationError('Нарушена структура данных')
        for item in pd:
            print(set(item))
            if re.search("[<>()^@&#]", item):
                raise forms.ValidationError('Ошибка ввода, присутсвуют недопустимые символы')
        return pd


class UserProfileForm(forms.Form):
    ordering = forms.CharField()
    '''all_urls = forms.ModelMultipleChoiceField(
        queryset=UrlsTable.objects.all().order_by('url'),
        widget=forms.CheckboxSelectMultiple,
        label="",
        label_suffix='',
    )'''
