from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    """
    Base model for all models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Departament(BaseModel):
    description = models.CharField(
        max_length=100, verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Derpatamento')
        verbose_name_plural = _('Departamentos')

    def __str__(self):
        return str(self.description)


class Employee(BaseModel):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_('Nome'),
    )

    email = models.EmailField(
        max_length=150,
        blank=False,
        null=False,
        unique=True,
        verbose_name=_('Email'),
    )

    departament = models.ForeignKey(
        Departament,
        on_delete=models.CASCADE,
        verbose_name=_('Departamento'),
    )

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return str(self.name)
