from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='Администратор',
        help_text='Является ли пользователь администратором?'
    )
    is_rso_user = models.BooleanField(
        default=False,
        verbose_name='Пользователь РСО',
        help_text='Относится ли пользователь к РСО?'
    )
    is_dispatcher = models.BooleanField(
        default=False,
        verbose_name='Диспетчер',
        help_text='Является ли пользователь диспетчером?'
    )

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CommunicationsType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Тип объекта коммуникаций'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тип объекта коммуникаций'
        verbose_name_plural = 'типы объектов коммуникаций'


class Communications(models.Model):
    # Заменить на отдельную таблицу
    type = models.ForeignKey(
        CommunicationsType,
        on_delete=models.PROTECT,
        verbose_name='Тип объекта коммуникаций'
    )
    parameters = models.CharField(
        max_length=250,
        blank=True,
        verbose_name='Параметры объекта'
    )

    def __str__(self):
        if self.parameters:
            return f"{self.type} ({self.parameters})"
        return f"{self.type} (параметры не указаны)"

    class Meta:
        verbose_name = 'объект коммуникаций'
        verbose_name_plural = 'объекты коммуникаций'


class IncidentType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Тип инцидента'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тип инцидента'
        verbose_name_plural = 'типы инцидентов'


class Incident(models.Model):
    communications_object = models.ForeignKey(
        Communications,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Объект коммуникаций, для которого вводится инцидент'
    )

    start_date = models.DateTimeField(
        default=datetime.datetime.now(),
        verbose_name='Дата и время начала'
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата и время завершения'
    )

    type = models.ForeignKey(
        IncidentType,
        on_delete=models.PROTECT,
        verbose_name='Тип инцидента'
    )
    additional_info = models.CharField(
        max_length=250,
        blank=True,
        verbose_name='Дополнительная информация'
    )

    # def __str__(self):
    #     if str(self.communications_object) is None:
    #         on = 'объект удален из базы'
    #     else:
    #         on = str(self.communications_object)
    #

    class Meta:
        verbose_name = 'инцидент'
        verbose_name_plural = 'инциденты'
