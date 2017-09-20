from django import forms
from .models import Predict


class PredictForm(forms.ModelForm):
    class Meta:
        model = Predict
        fields = ['naver_url', 'distributor_effect']
