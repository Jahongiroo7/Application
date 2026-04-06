from django.db import models
from django.core.validators import RegexValidator

APPLICATION_STATUS = (
    ("qabul_qilingan","Qabul qilingan"),
    ("organib_chiqilmoqda","Organib chiqilmoqda"),
    ("rad_etilgan","Rad etilgan"),
    ("hal_qilingan","Hal qilingan"),
)

REGEX = RegexValidator(
    regex=r"^[+]998[0-9]{9}$",
    message="Raqam xato ! Namuna: +998991112233")

class Category(models.Model):
    """  """
    name = models.CharField(max_length=50, verbose_name="Nomi", unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Application(models.Model):
    """  """
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    body = models.TextField(verbose_name="Batafsil")
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    applicant = models.CharField(max_length=40, verbose_name="Arizachi")
    phone1 = models.CharField(max_length=15, validators=[REGEX], verbose_name="Tel. raqam 1")
    phone2 = models.CharField(max_length=15, validators=[REGEX], verbose_name="Tel. raqam 2", null=True, blank=True)
    status = models.CharField(max_length=50, choices=APPLICATION_STATUS, default='qabul_qilingan')
    created_on = models.DateTimeField()

    def __str__(self):
        return self.name

class Worker(models.Model):
    """  """
    full_name = models.CharField(max_length=100, verbose_name="Ism familiya")
    photo = models.ImageField(upload_to='worker_photo/')
    stage = models.CharField(max_length=100 ,verbose_name="Lavozim")
    phone1 = models.CharField(max_length=15, validators=[REGEX], verbose_name="Tel. raqam 1")
    phone2 = models.CharField(max_length=15, validators=[REGEX], verbose_name="Tel. raqam 2", null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
