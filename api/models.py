from django.db import models

# Create your models here.

class Map(models.Model):
    name = models.CharField('Nome', max_length=255)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapas'


class Route(models.Model):
    map_name = models.ForeignKey(Map, verbose_name='Mapa', related_name='routes')
    origin = models.CharField('Origem', max_length=255)
    destiny = models.CharField('Destino', max_length=255)
    distance = models.PositiveSmallIntegerField('Distancia em km')

    def __str__(self):
        return '{} x {} - {}KM'.format(self.origin, self.destiny, self.distance)

    class Meta:
        ordering = ['map_name']
        verbose_name = 'Rota'
        verbose_name_plural = 'Rotas'