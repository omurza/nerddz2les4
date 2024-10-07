from django.db import models

# Create your models here.
class Setmodel(models.Model):
    name=models.CharField(
        verbose_name='Имя сотрудника',
        max_length=100
        
    )
    positions=models.CharField(
        verbose_name='Должность',
        max_length=100
        
    )
    description=models.TextField(
        verbose_name='Описание'        
    )
    logo = models.ImageField(
        upload_to='logo_image/'
    )
    URL=models.URLField(
        verbose_name="ccылак и контакты (эщкере)"
    )