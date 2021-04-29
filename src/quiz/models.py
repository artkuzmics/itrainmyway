from django.db import models
from django.utils import timezone

class Quize(models.Model):

    timestamp = models.DateTimeField(default=timezone.now)

    time = models.CharField(max_length=100)
    money = models.CharField(max_length=100)
    alone = models.BooleanField()
    group = models.BooleanField()
    family = models.BooleanField()

    contactsport = models.CharField(max_length=100)
    how = models.CharField(max_length=100)
    fitnesslevel = models.CharField(max_length=100)
    height = models.CharField(max_length=100)

    # Superpowers
    flexibility = models.BooleanField()
    focus = models.BooleanField()
    lower_body_strength = models.BooleanField()
    balance = models.BooleanField()
    endurance = models.BooleanField()

    #Weaknesses
    weak_speed = models.BooleanField()
    weak_hand_eye_coordination = models.BooleanField()
    weak_upper_body_stregth = models.BooleanField()
    weak_foot_eye_coordination = models.BooleanField()
    weak_being_in_water = models.BooleanField()

    #Characteristics
    perfectionist = models.BooleanField()
    patient = models.BooleanField()
    high_energy = models.BooleanField()
    competitive = models.BooleanField()
    thrive_under_pressure = models.BooleanField()

    #Workout Environments
    tried_and_tested = models.BooleanField()
    ever_changing = models.BooleanField()
    centre_of_attention = models.BooleanField()
    express_myself = models.BooleanField()
    adrenaline_fuelled = models.BooleanField()

    #Optional
    gender = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self):
        return f'Entry made on {self.timestamp}, by gender {self.gender}, of age {self.age}'

    class Meta:
        ordering = ('-timestamp',)



# Create your models here.
