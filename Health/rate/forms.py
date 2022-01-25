from django.forms import ModelForm
from rate.models import Details

class HeartForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
        # ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes','ejection_fraction', 'high_blood_pressure', 'platelets','serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']