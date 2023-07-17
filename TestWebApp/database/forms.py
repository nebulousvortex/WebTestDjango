from .models import Notes, Category
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ModelChoiceField, Select


class NoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

    class Meta:
        model = Notes

        category = ModelChoiceField(
            queryset=Category.objects.all(),
            widget=Select(attrs={'class': 'form-control'})
        )

        fields = ['title', 'anons', 'full_text', 'category']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            # "date": DateTimeInput(attrs={
            #     'placeholder': 'Дата',
            #     'class': 'form-control',
            # }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
        }
