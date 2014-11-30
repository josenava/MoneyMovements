from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Csv File')


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=20)
    related_words = forms.CharField(max_length=150)

    def clean_related_words(self):
        related_words = self.cleaned_data['related_words'].split(';')
        msg = ""
        error = False
        if 0 == len(related_words):
            msg = "Empty field"
            error = True
        elif '' != related_words[-1]:
            msg = "You forgot last ;"
            error = True
        elif len([i for i in related_words[:-1] if '' == i]) > 0:
            msg = "Check the list, you are missing some words"
            error = True

        if error:
            raise forms.ValidationError(msg, code='invalid')

        return self.cleaned_data['related_words']
