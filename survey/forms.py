#from users.models import Profile 
from .models import Question 
from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

class SurveyForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['owner']
    
    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
