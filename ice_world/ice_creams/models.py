from django.db import models

# Create your models here.
class Ice_market(models.Model):

    name = models.CharField(verbose_name='Название киоска', max_length=50)
    ice_cream = models.ForeignKey('Ice_cream', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Киоск'
        verbose_name_plural = 'Киоски'
        ordering = ['name',]

class Ice_cream(models.Model):
    ICE_CREAMS = [
        ('Шоколад', 'Шоколад'),
        ('Клубника', 'Клубника'),
        ('Ваниль', 'Ваниль'),

    ]

    name = models.CharField(verbose_name='Мороженное', max_length=50)
    taste = models.CharField(verbose_name='Вкус', max_length=100, choices=ICE_CREAMS)
   # market = models.ForeignKey(Ice_market, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мороженное'
        verbose_name_plural = 'Мороженные'
        ordering = ['name',]