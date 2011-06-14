import datetime
from django.db import models
from django.contrib.auth.models import User



class Car(models.Model):
    """
    Contains all the car details. The date fields refer to the purchase date.
    """
    SEDAN_TYPE = 1
    HATCHBACK_TYPE = 2
    COUPE_TYPE = 3
    WAGON_TYPE = 4
    SPORT_TYPE = 5
    TYPE_CHOICES = (
                  (SEDAN_TYPE, 'Sedan'),
                  (HATCHBACK_TYPE, 'Hatchback'),
                  (COUPE_TYPE, 'Coupe'),
                  (WAGON_TYPE, 'Station wagon'),
                  (SPORT_TYPE, 'Sport'),
                  )
    
    car_id = models.CharField(max_length = 7)
    brand = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    type = models.IntegerField(choices = TYPE_CHOICES, default = SEDAN_TYPE)
    is_automatic = models.BooleanField(default = True)
    gears = models.IntegerField(default = 5)
    hand = models.IntegerField(default = 0, help_text = 'Number of previous owners when purchased')
    year = models.DateField(help_text = 'Production year')
    purchase_date = models.DateField(default = datetime.datetime.now, help_text = 'Purchase date')
    kilometrage = models.IntegerField(help_text = 'Kilometrage when purchased')
    color = models.CharField(max_length = 100)
    
    class Meta:
        unique_together = ('car_id', 'brand')
    
    def __unicode__(self):
        return '%s %s %s' % (self.brand, self.model, self.year.strftime('%Y'))
    
    def was_new_when_bought(self):
        return self.hand == 0
    
    def get_full_name(self):
        return '%s %s %s' % (self.brand, self.model, self.year.strftime('%Y'))
    
    def get_absolute_url(self):
        return '/carlog/car/%s' % (self.id)


class CarMechanic(models.Model):
    """
    Contains information about a mechanic.
    """
    name = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    telephone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 150)
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    email = models.EmailField()
    specialization = models.CharField(max_length = 100, default = 'General', help_text = 'Comma separated if several')

    def __unicode__(self):
        return "%s %s" % (self.name, self.lastname)
    
    def get_absolute_url(self):
        return '/carlog/car/mechanic/%s' % (self.id)
    
    
class CarTreatmentEntry(models.Model):
    """
    Contains the information regarding a treatment that took place or is planned for the future.
    """
    BODYWORK_CAT = 1
    ELECTRIC_CAT = 2
    ENGINE_CAT = 3
    WHEELS_CAT = 4
    CHASIS_CAT = 5
    TREATMENT_CATS = (
                      (BODYWORK_CAT, 'Body work'),
                      (ELECTRIC_CAT, 'Electricity'),
                      (ENGINE_CAT, 'Engine'),
                      (WHEELS_CAT, 'Wheels'),
                      (CHASIS_CAT, 'Chasis'),
                      )
    
    BROKEN_REASON = 1
    SERVICE_REASON = 2
    AESTHETIC_REASON = 3
    NO_REASON = 4
    TREATMENT_REASONS = (
                         (BROKEN_REASON, 'Failing component'),
                         (SERVICE_REASON, 'Service'),
                         (AESTHETIC_REASON, 'Aesthetic'),
                         (NO_REASON, 'No reason'),
                         )
    
    car = models.ForeignKey(Car)
    mechanic = models.ForeignKey(CarMechanic)
    planned = models.BooleanField(default = False, help_text = 'Is this a treatment planned for the future?')
    date = models.DateField(default = datetime.datetime.now, help_text = 'If a future treatment, then the planned date to take the car for treatment')
    reason = models.IntegerField(choices = TREATMENT_REASONS, default = BROKEN_REASON)
    parts_replaced = models.CharField(max_length = 300, default = 'None', help_text = 'Replaced parts during treatment, comma separated')
    description = models.TextField()
    category = models.IntegerField(choices = TREATMENT_CATS, default = BODYWORK_CAT)
    kilometrage = models.IntegerField(help_text = 'If a future treatment, then the planned kilometrage to take the car for treatment')
    cost = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Car treatment entries'
        
    def __unicode__(self):
        return '%s %s' % (self.formatted_date(), self.car)
    
    def formatted_date(self):
        return self.date.strftime('%b/%d/%Y')

