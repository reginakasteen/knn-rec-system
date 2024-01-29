from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Your review..."}))
    class Meta:
        model = Review
        fields = ['rating_value', 'review_text']

