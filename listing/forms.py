from django import forms


class ListingUploadForm(forms.Form):
    file = forms.FileField()
