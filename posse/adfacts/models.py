from django.db import models

# Create your models here.

class Donor(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    full_name = models.CharField(max_length=256)
    email = models.CharField(max_length=128)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=15)
    country = models.CharField(max_length=32)
    notes = models.TextField()
       
class Org(models.Model):
    ORG_TYPES = ( 
           ('501c4', '501c4'),
           ('PAC', 'PAC'),
           ('other', 'Other')
    )
    LOC_CHOICES = (
           ('arizona', 'Arizona'),
           ('out_of_state', 'Out Of State'),
           ('unknown', 'Unknown')
    )
    YN_CHOICES = (
            ('y', 'Y'),
            ('n', 'N'))
    name = models.CharField(max_length=256)
    org_type =  models.CharField(max_length=64, choices=ORG_TYPES, null=True)
    location = models.CharField(max_length=64, choices = LOC_CHOICES, null=True)
    dark_money = models.CharField(max_length=1, choices = YN_CHOICES, null=True)
    sos_link = models.CharField(max_length=256, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    donors = models.ManyToManyField(Donor)

class Ad(models.Model):
    GOV = 'gov'
    SoS = 'sec_of_state'
    AG = 'atty_gen'
    TRES = 'treasurer'
    CORP_COMM = 'corp_comm'
    STATE_HOUSE = 'state_house'
    STATE_SENATE = 'state_senate'
    INIT = 'ballot_init'
    OTHER = 'other'
    RACE_CHOICES = (
             ( '', ''),
             ( GOV, 'Governor'),
             ( SoS, 'Secretary of State'),
             ( AG, 'Attorney General'),
             ( TRES, 'Treasurer'),
             ( CORP_COMM, 'Corporation Commissioner'),
             ( STATE_HOUSE, 'State House'),
             ( STATE_SENATE, 'State Senate'),
             ( INIT, 'Ballot Initiative'),
             ( OTHER, 'Other'),
            )
    FORMAT_CHOICES = (
             ( 'mailer', 'Mailer'),
             ( 'tv', 'TV'),
             ( 'radio', 'Radio'),
             ( 'youtube', 'Youtube'),
             ( 'fb', 'Facebook'),
             ( 'email', 'Email'),
             ( 'yard_sign', 'Yard Sign'),
             ( 'large_sign', 'Large Sign'),
             ( 'other', 'Other'),
          )
    FOR_AGAINST = (
              ('for', 'For'),
              ('against', 'Against')) 
    title = models.CharField(max_length=256)
    desc = models.TextField(blank=True, null=True)
    paid_by = models.ForeignKey(Org, on_delete=models.PROTECT, blank=True, null=True)
    race = models.CharField(max_length = 64, choices = RACE_CHOICES, blank=True, null=True)
    district = models.IntegerField(null=True)
    candidate_or_initiative = models.CharField(max_length=256)
    support_oppose = models.CharField(max_length=32, choices=FOR_AGAINST, default='for')
    format = models.CharField(max_length=32, choices=FORMAT_CHOICES, null=True, blank=True)
    first_seen = models.DateTimeField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

