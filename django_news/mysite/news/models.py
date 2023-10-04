from django.db import models

class Articles(models.Model):
    title = models.CharField('Titlr', max_length=200)
    anons = models.CharField('Anons', max_length=250)
    body = models.TextField('Body')
    data = models.DateTimeField('Data')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'