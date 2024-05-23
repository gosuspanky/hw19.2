from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price_per_purchase', "category")

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция",
                           "радар"]

        if cleaned_data.lower() in forbidden_words:
            raise forms.ValidationError('В названии применено некорректное слово')

        return cleaned_data
