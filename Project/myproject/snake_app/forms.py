from django import forms
from snake_app.models import snake

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = snake # Corrected model name
        fields = ("image","date")     # Specify the fields you want to include
        
    


   
