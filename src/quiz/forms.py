from .models import Quize
from django import forms





class QuizForm(forms.ModelForm):



    time = forms.ChoiceField(choices=[
                                ('minutes','Minutes'),
                                ('hours','Hours'),
                                ('days','Days')],
                            widget=forms.RadioSelect(attrs={'class': 't-radio js-tilda-rule','data-tilda-req':'1'}))

    money = forms.ChoiceField(choices=[
                                ('as little as possible','As little as possible'),
                                ('reasonable amount','A reasonable amount'),
                                ('show me what you got','Show me what you got')],
                            widget=forms.RadioSelect(attrs={'class': 't-radio js-tilda-rule', 'data-tilda-req':'1'}))

    contactsport = forms.ChoiceField(choices=[
                                ('no','Rather not'),
                                ('maybe','Maybe'),
                                ('yes','Bring it on!')],
                            widget=forms.RadioSelect(attrs={'class': 't-radio js-tilda-rule', 'data-tilda-req':'1'}))

    how = forms.ChoiceField(choices=[
                                ('on my own','Working on my own'),
                                ('in a team','Working in a team'),
                                ('either is good','Either is good')],
                            widget=forms.RadioSelect(attrs={'class': 't-radio js-tilda-rule', 'data-tilda-req':'1'}))

    fitnesslevel = forms.ChoiceField(choices=[
                                ('start me gently','Start me gently...'),
                                ('ready','Ready to go'),
                                ('unbeatable','Unbeatable!')],
                            widget=forms.RadioSelect(attrs={'class': 't-radio js-tilda-rule', 'data-tilda-req':'1'}))

    height = forms.ChoiceField(choices=[
                                ('short','Pretty short'),
                                ('average','Average height'),
                                ('tall','Fairly tall')],
                            widget=forms.RadioSelect(attrs={'class': 't-radio js-tilda-rule', 'data-tilda-req':'1'}))

    gender = forms.ChoiceField(choices=[
                                ('male','Male'),
                                ('female','Female'),
                                ('other','Other'),
                                ('na','Prefer not to say')],
                            widget=forms.RadioSelect(attrs={'class': 't-radio js-tilda-rule'}))


    class Meta:
        model = Quize
        fields = ('time', 'money', 'alone', 'group', 'family','contactsport','how','fitnesslevel','height',
                    'flexibility','focus','lower_body_strength','balance','endurance',
                    'weak_speed','weak_hand_eye_coordination','weak_upper_body_stregth','weak_foot_eye_coordination','weak_being_in_water',
                    'perfectionist','patient','high_energy','competitive','thrive_under_pressure',
                    'tried_and_tested','ever_changing','centre_of_attention','express_myself','adrenaline_fuelled',
                    'gender','age')

# Create your tests here.
