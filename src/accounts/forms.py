from django import forms

'''
class CustomSignupForm(forms.Form):

    nickname = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': ('Nickname')}))


    def signup(self, request, user):
        user.nickname = self.cleaned_data['username']


        user.save()
    '''