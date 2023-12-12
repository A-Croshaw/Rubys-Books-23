
from django import forms
from .widgets import MyClearableFileInput
from .models import Book, Category


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=MyClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        view_names = [(c.id, c.get_View_name()) for c in categories]

        self.fields['category'].choices = view_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'