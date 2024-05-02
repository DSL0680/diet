from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('date', 'content', 'image')
    date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD 날짜 형식으로 입력'}),
    )
