from django import forms
from .models import Session, Review
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        hall = cleaned_data.get('hall')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if hall and date and start_time and end_time:
            # Перевірка на перетин
            overlaps = Session.objects.filter(
                hall=hall,
                date=date,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            if self.instance.pk:
                overlaps = overlaps.exclude(pk=self.instance.pk)

            if overlaps.exists():
                raise forms.ValidationError("⚠️ Сеанс у цьому залі перетинається з іншим!")

        return cleaned_data


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Ім’я")
    last_name = forms.CharField(max_length=30, required=True, label="Прізвище")
    email = forms.EmailField(max_length=254, required=True, label="Електронна пошта")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Напишіть свій відгук...',
                'rows': 4,
                'class': 'form-control review-textarea'
            }),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Ім’я',
            'last_name': 'Прізвище',
            'email': 'Email',
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старий пароль', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
    new_password1 = forms.CharField(label='Новий пароль', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    new_password2 = forms.CharField(label='Підтвердження паролю', widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))