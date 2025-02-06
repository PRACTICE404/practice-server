import re
from django import forms


def validate_phone(value):
    """
    Проверяет, что номер телефона соответствует формату +XX (XXX) XXX XX XX.
    """
    pattern = r"^\+\d{1,3} \(\d{2,4}\) \d{3}-\d{2}-\d{2}$"
    if not re.match(pattern, value):
        raise forms.ValidationError("Введите номер в формате: +XX (XXX) XXX XX XX")  # noqa


class WhatsAppForm(forms.Form):
    full_name = forms.CharField(
        label="ИФО",
        max_length=100,
        widget=forms.TextInput(attrs={
            "required": "required",
            "type": "text",
            "placeholder": "Samuel Rwebichard"
        })
    )
    phone = forms.CharField(
        label="Номер телефона",
        validators=[validate_phone],
        widget=forms.TextInput(attrs={
            "required": "required",
            "type": "text",
            "placeholder": "+XX (XXX) XXX XX XX"
        })
    )
    company_type = forms.ChoiceField(
        label="Кто ты?",
        choices=[
            ("Company", "Компания"),
            ("Freelancer", "Фрилансер / Работник компании"),
            ("Individual", "Обыватель"),
        ],
        widget=forms.Select()
    )
    budget = forms.CharField(
        label="Бюджет ($)",
        max_length=50,
        widget=forms.NumberInput(attrs={
            "type": "number",
            "placeholder": "~$"
        })
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={"placeholder": "..."})
    )
