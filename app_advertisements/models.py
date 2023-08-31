from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}title={self.title}, price={self.price})>'

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color: red">Сегодня в {}</span>', created_time
            )
        else:
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")


    class Meta:
        db_table = 'advertisements'


