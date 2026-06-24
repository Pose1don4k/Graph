from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Graph

class GraphForm(forms.ModelForm):
    COLOR_CHOICES = [
        ('blue', 'Синий'),
        ('red', 'Красный'),
        ('green', 'Зелёный'),
        ('black', 'Чёрный'),
    ]

    GRAPH_TYPE_CHOICES = [
        ('exponent', 'Экспонента (y = eˣ)'),
        ('parabola', 'Парабола (y = x²)'),
        ('abs', 'Модуль (y = |x|)'),
    ]

    color = forms.ChoiceField(choices=COLOR_CHOICES, label='Цвет линии')
    graph_type = forms.ChoiceField(choices=GRAPH_TYPE_CHOICES, label='Тип графика')
    thickness = forms.IntegerField(
        label='Толщина линии',
        min_value=1,
        max_value=10,
        initial=2,
        widget=forms.NumberInput(attrs={'min': '1', 'max': '10'})
    )
    scale = forms.IntegerField(
        label='Масштаб',
        min_value=1,
        max_value=100,
        initial=10,
        widget=forms.NumberInput(attrs={'min': '1', 'max': '100'})
    )

    class Meta:
        model = Graph
        fields = ['title', 'color', 'thickness', 'scale', 'graph_type']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username",)
