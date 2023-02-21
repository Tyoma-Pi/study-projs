import string

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import AdditonalUserInfo


# Create your forms here.
class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя')
    email = forms.EmailField(label='Адрес почты', widget=forms.EmailInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                                validators=[
                                    RegexValidator(r'\d', 'Введите хотя бы одно число'),
                                    RegexValidator(r'[A-Z]', 'Введите хотя бы одну букву верхнего регистра'),
                                    RegexValidator(r'[' + string.punctuation + ']', 'Введите хотя бы один спецсимвол')
                                ])
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)


class ChangeAuthForm(forms.Form):
    username = forms.CharField(label='Новое имя пользователя')
    email = forms.EmailField(label='Новый адрес почты', widget=forms.EmailInput)
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput,
                                validators=[
                                    RegexValidator(r'\d', 'Введите хотя бы одно число'),
                                    RegexValidator(r'[A-Z]', 'Введите хотя бы одну букву верхнего регистра'),
                                    RegexValidator(r'[' + string.punctuation + ']', 'Введите хотя бы один спецсимвол')
                                ])
    new_password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)


class ChangeProfForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    photo = forms.FileField(label='Фотография')
    city = forms.CharField(label='Город')
    birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput)
    about = forms.CharField(label='О себе', widget=forms.Textarea)


class FilterForm(forms.Form):
    filterfield = forms.ChoiceField(label='Фильтрация по',
                                    choices=[
                                        ('name', 'Название'),
                                        ('author', 'Автор'),
                                        ('language', 'Язык'),
                                        ('genre', 'Жанр'),
                                        ('year', 'Год выпуска'),
                                        ('print', 'Издательство')])
    filter = forms.CharField(label='Введите информацию, по которой происходит фильтрация', required=False)
