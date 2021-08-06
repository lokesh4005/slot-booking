from django.forms import ModelForm
from .models import booking
class wishlist(ModelForm):
    class Meta:
        model = booking
        fields = '__all__'