# users/forms.py
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "username": "Имя пользователя",
            "email": "Email",
            "password1": "Пароль",
            "password2": "Повторите пароль",
        }

        for name, field in self.fields.items():
            field.help_text = ""
            field.label = ""
            field.widget.attrs.update(
                {
                    "placeholder": placeholders.get(name, name.capitalize()),
                    "class": "form-control",
                }
            )

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = "post"
