from django import forms

OPTIONS = (
    ('plasma', 'Plasma'),
    ('oxygen', 'Oxygen'),
    ('remdesivir', 'Remdesivir'),
    ('ventilators', 'Ventilators'),
    ('counseling', 'Counseling')
)

class CityForm(forms.Form):
    city_name = forms.CharField(label='Name of your city', max_length=100)
    required_help = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.layout = Layout(
    #         Field('conta', id="form-conto", css_class="form-control", title="Conto")
    #     )