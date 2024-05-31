from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price_per_purchase', "category", "owner")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words_list = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                                "радар"]

        if cleaned_data.lower() in forbidden_words_list:
            raise forms.ValidationError('В названии применено некорректное слово')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("description", "category")
