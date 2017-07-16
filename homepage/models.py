from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Register(models.Model):
    YEAR_IN_SCHOOL = (
        (0,'Elige tu año escolar'),
        (1,'1ro'),
        (2,'2do'),
        (3,'3ro'),
        (4,'4to'),
        (5,'5to')
    )

    """CITIES = (
        (0,'Elige una ciudad Sede'),
        (1,'Arequipa'),
        (2,'Cusco')
    )"""

    created_on = models.DateTimeField(
        auto_now_add=True)  # parametro que activa el date time en el momento de la creacion del objeto
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dni = models.CharField(max_length=8,
                           validators=[RegexValidator(r"^\d{8}$")])
    school_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,
                             validators=[RegexValidator(
                                 r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")])
    year_in_school = models.IntegerField(choices=YEAR_IN_SCHOOL,
                                         default=0  )
    #cities = models.IntegerField(choices=CITIES, default=0)

    def __str__(self):  # representacion en string del objeto
        return self.name

