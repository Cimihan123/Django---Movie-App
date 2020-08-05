from django.db import models


GENRE_CHOICES = (

('action','action'),
('comedy','comedy'),
('romantic','romantic'),
('drama','drama'),
('sad','sad'),
('horror','horror'),

)


LANGUAGE_CHOICES = (                                                                                                                                                                          
                                                                                                                                                                                              
    ('english','english'),                                                                                                                                                                         
    ('spanish','spanish'),                                                                                                                                                                          
    ('nepali','nepali'),                                                                                                                                                                          
                                                                                                                                                                                              
)  



# Create your models here.
class Movie(models.Model):

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    genre = models.CharField(choices=GENRE_CHOICES ,max_length=20)
    casts = models.CharField(max_length=200)
    language = models.CharField(choices=LANGUAGE_CHOICES ,max_length=200)
    director = models.CharField(max_length=200)
    update_time = models.DateField(auto_now_add=True)
    release_date = models.DateField(null=True,blank=True)
    length = models.IntegerField()
    budget = models.IntegerField()
    image = models.ImageField(upload_to='movies')
    
    def __str__(self):
        return self.name


