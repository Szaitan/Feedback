from django import forms
from .models import Review


class ReviewForm(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    review_text = forms.CharField(label="Your Feedback", max_length=200, widget=forms.Textarea)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)

# Other approach

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = '__all__' # informuje naszą klasę aby wykorzystała wszystkie pola
#         # exclude = ['username'] Daje znać które pola maja być wykluczone
#         labels = {
#             "username": "Your Name",
#             "review_text": "Your Feedback",
#             "rating": "Your Rating"
#         } # Możemy wpływać na nazwy naszych labelsów

#         error_messages = {
#             "username": {
#                 "required": "Your name must not be empty!",
#                 "max_length": "Please enter a shorter name!"
#             }
#         } # Możemy wpływać na treść error messages
