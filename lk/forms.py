from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'forma',
                                                               'placeholder': 'Ваше имя'
                                                               })
                                 )
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class': 'forma',
                                                              'placeholder': 'Ваша фамилия'
                                                              })
                                )
    email = forms.EmailField(max_length=200,
                             widget=forms.TextInput(attrs={'class': 'forma',
                                                           'placeholder': 'Ваш email'
                                                           })
                             )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'forma', 'placeholder': 'Введите логин'}),
        }

        labels = {
            'username': False,
        }
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'forma'
        self.fields['password2'].widget.attrs['class'] = 'forma'

        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

        self.fields['first_name'].label = False
        self.fields['last_name'].label = False
        self.fields['email'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
