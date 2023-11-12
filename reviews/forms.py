from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    review_text = forms.CharField(label="Your Feedback", max_length=200, widget=forms.Textarea)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)
