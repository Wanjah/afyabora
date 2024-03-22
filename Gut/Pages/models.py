from django.db import models
from django.forms import ModelForm

# Create your models here.
#model to take in prompts
class prompts(models.Model):
    Age = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False)
    gender_choices = (
        ("Female", "Female"),
        ("Male", "Male")
    )
    Gender = models.CharField(max_length=10, choices=gender_choices)
    Allergies = models.CharField(max_length=20, null=False, blank= False)
    Medical_Condition = models.CharField(max_length=20, null=False, blank= False)
    Dietary_Restrictions = models.CharField(max_length=20, null=True, blank=False)
    Food_Preferences = models.CharField(max_length=20, null=False, blank= False)

#create model form
class AssessementForm(ModelForm):
    class Meta:
        model = prompts
        fields = '__all__'