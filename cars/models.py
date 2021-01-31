from django.db import models
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.
class FeaturedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_featured=True).order_by('-created_date')

class Car(models.Model):
    condition_choice= (('new','new'),('used','used'))
    country_choice= (
        ('af','Afghanistan'),
        ('al','Albania'),
        ('dz','Algeria'),
        ('ad','Andorra'),
        ('ao','Angola'),
        ('ai','Anguilla'),
        ('ag','Antigua and Barbuda'),
        ('ar','Argentina'),
        ('am','Armenia'),
        ('aw','Aruba'),
        ('au','Australia'),
        ('at','Austria'),
        ('az','Azerbaijan'),
        ('bs','Bahamas'),
        ('bh','Bahrain'),
        ('bd','Bangladesh'),
        ('bb','Barbados'),
        ('by','Belarus'),
        ('be','Belgium'),
        ('bz','Belize'),
        ('bj','Benin'),
        ('bm','Bermuda'),
        ('bt','Bhutan'),
        ('bo','Bolivia'),
        ('ba','Bosnia and Herzegovina'),
        ('bw','Botswana'),
        ('br','Brazil'),
        ('bn','Brunei Darussalam'),
        ('bg','Bulgaria'),
        ('bf','Burkina Faso'),
        ('bi','Burundi'),
        ('kh','Cambodia'),
        ('cm','Cameroon'),
        ('ca','Canada'),
        ('cv','Cape Verde'),
        ('ky','Cayman Islands'),
        ('cf','Central African Republic'),
        ('td','Chad'),
        ('cl','Chile'),
        ('cn','China'),
        ('cx','Christmas Island'),
        ('cc','Cocos (Keeling) Islands'),
        ('co','Colombia'),
        ('km','Comoros'),
        ('cg','Congo'),
        ('ck','Cook Islands'),
        ('cr','Costa Rica'),
        ('ci','Cote D\'Ivoire (Ivory Coast)'),
        ('hr','Croatia (Hrvatska)'),
        ('cu','Cuba'),
        ('cy','Cyprus'),
        ('cz','Czech Republic'),
        ('cd','Democratic Republic of the Congo'),
        ('dk','Denmark'),
        ('dj','Djibouti'),
        ('dm','Dominica'),
        ('do','Dominican Republic'),
        ('ec','Ecuador'),
        ('eg','Egypt'),
        ('sv','El Salvador'),
        ('gq','Equatorial Guinea'),
        ('er','Eritrea'),
        ('ee','Estonia'),
        ('et','Ethiopia'),
        ('fk','Falkland Islands (Malvinas)'),
        ('fo','Faroe Islands'),
        ('fm','Federated States of Micronesia'),
        ('fj','Fiji'),
        ('fi','Finland'),
        ('fr','France'),
        ('gf','French Guiana'),
        ('pf','French Polynesia'),
        ('tf','French Southern Territories'),
        ('ga','Gabon'),
        ('gm','Gambia'),
        ('ge','Georgia'),
        ('de','Germany'),
        ('gh','Ghana'),
        ('gi','Gibraltar'),
        ('gb','Great Britain (UK)'),
        ('gr','Greece'),
        ('gl','Greenland'),
        ('gd','Grenada'),
        ('gp','Guadeloupe'),
        ('gt','Guatemala'),
        ('gn','Guinea'),
        ('gw','Guinea-Bissau'),
        ('gy','Guyana'),
        ('ht','Haiti'),
        ('hn','Honduras'),
        ('hk','Hong Kong'),
        ('hu','Hungary'),
        ('is','Iceland'),
        ('in','India'),
        ('id','Indonesia'),
        ('ir','Iran'),
        ('iq','Iraq'),
        ('ie','Ireland'),
        ('il','Israel'),
        ('it','Italy'),
        ('jm','Jamaica'),
        ('jp','Japan'),
        ('jo','Jordan'),
        ('kz','Kazakhstan'),
        ('ke','Kenya'),
        ('ki','Kiribati'),
        ('kp','Korea (North)'),
        ('kr','Korea (South)'),
        ('kw','Kuwait'),
        ('kg','Kyrgyzstan'),
        ('la','Laos'),
        ('lv','Latvia'),
        ('lb','Lebanon'),
        ('ls','Lesotho'),
        ('lr','Liberia'),
        ('ly','Libya'),
        ('li','Liechtenstein'),
        ('lt','Lithuania'),
        ('lu','Luxembourg'),
        ('mo','Macao'),
        ('mk','Macedonia'),
        ('mg','Madagascar'),
        ('mw','Malawi'),
        ('my','Malaysia'),
        ('mv','Maldives'),
        ('ml','Mali'),
        ('mt','Malta'),
        ('mh','Marshall Islands'),
        ('mq','Martinique'),
        ('mr','Mauritania'),
        ('mu','Mauritius'),
        ('yt','Mayotte'),
        ('mx','Mexico'),
        ('md','Moldova'),
        ('mc','Monaco'),
        ('mn','Mongolia'),
        ('ms','Montserrat'),
        ('ma','Morocco'),
        ('mz','Mozambique'),
        ('mm','Myanmar'),
        ('na','Namibia'),
        ('nr','Nauru'),
        ('np','Nepal'),
        ('nl','Netherlands'),
        ('an','Netherlands Antilles'),
        ('nc','New Caledonia'),
        ('nz','New Zealand (Aotearoa)'),
        ('ni','Nicaragua'),
        ('ne','Niger'),
        ('ng','Nigeria'),
        ('nu','Niue'),
        ('nf','Norfolk Island'),
        ('mp','Northern Mariana Islands'),
        ('no','Norway'),
        ('om','Oman'),
        ('pk','Pakistan'),
        ('pw','Palau'),
        ('ps','Palestinian Territory'),
        ('pa','Panama'),
        ('pg','Papua New Guinea'),
        ('py','Paraguay'),
        ('pe','Peru'),
        ('ph','Philippines'),
        ('pn','Pitcairn'),
        ('pl','Poland'),
        ('pt','Portugal'),
        ('qa','Qatar'),
        ('re','Reunion'),
        ('ro','Romania'),
        ('ru','Russian Federation'),
        ('rw','Rwanda'),
        ('gs','S. Georgia and S. Sandwich Islands'),
        ('sh','Saint Helena'),
        ('kn','Saint Kitts and Nevis'),
        ('lc','Saint Lucia'),
        ('pm','Saint Pierre and Miquelon'),
        ('vc','Saint Vincent and the Grenadines'),
        ('ws','Samoa'),
        ('sm','San Marino'),
        ('st','Sao Tome and Principe'),
        ('sa','Saudi Arabia'),
        ('sn','Senegal'),
        ('sc','Seychelles'),
        ('sl','Sierra Leone'),
        ('sg','Singapore'),
        ('sk','Slovakia'),
        ('si','Slovenia'),
        ('sb','Solomon Islands'),
        ('so','Somalia'),
        ('za','South Africa'),
        ('es','Spain'),
        ('lk','Sri Lanka'),
        ('sd','Sudan'),
        ('sr','Suriname'),
        ('sj','Svalbard and Jan Mayen'),
        ('sz','Swaziland'),
        ('se','Sweden'),
        ('ch','Switzerland'),
        ('sy','Syria'),
        ('tw','Taiwan'),
        ('tj','Tajikistan'),
        ('tz','Tanzania'),
        ('th','Thailand'),
        ('tg','Togo'),
        ('tk','Tokelau'),
        ('to','Tonga'),
        ('tt','Trinidad and Tobago'),
        ('tn','Tunisia'),
        ('tr','Turkey'),
        ('tm','Turkmenistan'),
        ('tc','Turks and Caicos Islands'),
        ('tv','Tuvalu'),
        ('ug','Uganda'),
        ('ua','Ukraine'),
        ('ae','United Arab Emirates'),
        ('us','United States of America'),
        ('uy','Uruguay'),
        ('uz','Uzbekistan'),
        ('vu','Vanuatu'),
        ('ve','Venezuela'),
        ('vn','Viet Nam'),
        ('vg','Virgin Islands (British)'),
        ('vi','Virgin Islands (U.S.)'),
        ('wf','Wallis and Futuna'),
        ('eh','Western Sahara'),
        ('ye','Yemen'),
        ('zr','Zaire (former)'),
        ('zm','Zambia'),
        ('zw','Zimbabwe'),
        )
    year_choice =  []
    for r in range(1900, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choice = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Haating'),
        ('Alarm System', 'Alarm System'),
        ('Park Assist', 'Park Assist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choice = (
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    car_title = models.CharField(max_length=255)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    country = models.CharField(choices=country_choice, max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    condition = models.CharField(choices=condition_choice ,max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo_1 = models.ImageField(upload_to="photo/%Y/%m/%d/")
    car_photo_2 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    car_photo_3 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    car_photo_4 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    car_photo_5 = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    features = MultiSelectField(choices= features_choice)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choice, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    #declare objects
    objects = models.Manager()
    featured = FeaturedManager()


    def __str__(self):
        return self.car_title

    def get_absolute_url(self):
        return reverse('cars:car_detail', args=[self.id])
