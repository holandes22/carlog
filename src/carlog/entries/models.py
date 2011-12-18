import datetime

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

DATE_FORMAT = '%m/%d/%Y'

def make_custom_datefield(field):
    """Adds a custom class to the field so it can be identified by Jquery UI datepicker in the template"""
    formfield = field.formfield()
    if isinstance(field, models.DateField):
        formfield.widget.format = DATE_FORMAT
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield

class Action(object):
    
    def __init__(self, action_url, action_name):
        self.action_url = action_url
        self.action_name = action_name
        
class IEntry(object):
    """
    Interface to unite some common methods.
    """
    
    class_verbose_name = None
    """
    Must be set by the Entry model to work out the urls.
    """
    actions = None
    
        
    def get_model_attrs(self, filter = 'id'):
        for field in self._meta.fields:
            if filter not in field.name:
                if field.choices:
                    yield field.name, getattr(self, 'get_%s_display' % field.name)
                else:
                    yield field.name, getattr(self, field.name)
    
    def get_full_name(self):
        return self.__unicode__()
        
    def get_absolute_url(self):
        return '/entries/%s/%s' % (self.class_verbose_name, self.id)
        
    def get_absolute_editor_url(self):
        return '%s/editor/' % (self.get_absolute_url())
    
    def get_delete_entry_url(self):
        return '/none'
    
    def get_entry_name(self):
        return self.class_verbose_name
    
    def get_entry_name_plural(self):
        return self.entry_name_plural
    
    @classmethod
    def get_model_editor_url(cls):
        return '/entries/%s/editor/' % (cls.class_verbose_name, )
    
    @classmethod
    def get_add_action(cls):
        return [Action(cls.get_model_editor_url(), 'Add %s' % cls.class_verbose_name)]
    
    def get_common_actions(self):
        if self.actions is not None:
            return self.actions 
        self.actions = self.get_add_action()
        self.actions.append(Action(self.get_absolute_editor_url(), 'Edit %s' % self.class_verbose_name))
        self.actions.append(Action(self.get_delete_entry_url(), 'Delete %s' % self.class_verbose_name))
        return self.actions


class Car(models.Model, IEntry):
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
    
    YEARS = [year for year in xrange(1920, datetime.datetime.now().year + 2)]
    YEAR_CHOICES = zip(YEARS, map(lambda x: str(x), YEARS))

    brand = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    type = models.IntegerField(choices = TYPE_CHOICES, default = SEDAN_TYPE)
    is_automatic = models.BooleanField(default = True)
    gears = models.IntegerField(default = 5)
    hand = models.IntegerField(default = 0, help_text = 'Number of previous owners when purchased')
    year = models.IntegerField(choices = YEAR_CHOICES, default = str(datetime.datetime.now().year))
    purchase_date = models.DateField(default = datetime.datetime.now, help_text = 'Purchase date')
    kilometrage = models.IntegerField(help_text = 'Kilometrage when purchased')
    color = models.CharField(max_length = 100)
    
    class_verbose_name = 'car'
    entry_name_plural = 'cars'
    
    def __unicode__(self):
        return '%s %s %s' % (self.brand, self.model, self.year)
    
    def was_new_when_bought(self):
        return self.hand == 0
    
class CarForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Car
        readonly_fields = ['user']
        exclude = ['user']

    def save(self, commit = True, user = None):
        model = super(CarForm, self).save(commit = False)
        model.user = user
 
        if commit:
            model.save()
        return model
    
class CarMechanic(models.Model, IEntry):
    """
    Contains information about a mechanic.
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    telephone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 150)
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    email = models.EmailField(blank = True)
    specialization = models.CharField(max_length = 100, default = 'General', help_text = 'Comma separated if several')

    class_verbose_name = 'mechanic'
    entry_name_plural = 'mechanics'
    
    def __unicode__(self):
        return "%s %s" % (self.name, self.lastname)
    
class CarMechanicForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = CarMechanic
        readonly_fields = ['user']
        exclude = ['user']
    
    def save(self, commit = True, user = None):
        model = super(CarMechanicForm, self).save(commit = False)
        model.user = user
 
        if commit:
            model.save()
        return model
    
   
    
class CarTreatmentEntry(models.Model, IEntry):
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
    date = models.DateField(default = datetime.datetime.now, 
                            help_text = 'If a future treatment, then the planned date to take the car for treatment')
    reason = models.IntegerField(choices = TREATMENT_REASONS, default = BROKEN_REASON)
    parts_replaced = models.CharField(max_length = 300, default = 'None', 
                                      help_text = 'Replaced parts during treatment, comma separated')
    description = models.TextField()
    category = models.IntegerField(choices = TREATMENT_CATS, default = BODYWORK_CAT)
    kilometrage = models.IntegerField(help_text = 'If a future treatment, then the planned kilometrage to take the car to the mechanic')
    cost = models.IntegerField()
    
    class_verbose_name = 'treatment'
    entry_name_plural = 'treatments'
    
    class Meta:
        verbose_name_plural = 'Car treatment entries'
        
    def __unicode__(self):
        return '%s %s' % (self.formatted_date(), self.car)
    
    def formatted_date(self):
        return self.date.strftime('%b/%d/%Y')
    
class CarTreatmentEntryForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = CarTreatmentEntry
        readonly_fields = ['user']
        exclude = ['user']
        
    def __init__(self, user, *args, **kwargs):
        super(CarTreatmentEntryForm, self).__init__(*args, **kwargs)
        #Only show the fields related to this user
        self.fields['car'].queryset = Car.objects.filter(user = user)
        self.fields['mechanic'].queryset = CarMechanic.objects.filter(user = user)
