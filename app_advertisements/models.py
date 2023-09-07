from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь',
                             on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}title={self.title}, price={self.price})>'

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color: green">Сегодня в {}</span>', created_time
            )
        else:
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата обнавления')
    def update_date(self):
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color: red">Сегодня в {}</span>', update_time
            )
        else:
            return self.update_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Изображение')
    def get_html_img(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;">', url=self.image.url
            )


    class Meta:
        db_table = 'advertisements'


