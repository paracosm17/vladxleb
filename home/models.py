import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.core.mail import send_mail

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.search import index

from .blocks import ExpeditionBlock

from django.contrib.auth import get_user_model


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['routes'] = RoutePage.objects.filter(driver=request.user)[::-1]
        return context
    
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'
    
    parent_page_types = []
    subpage_types = ['home.RouteIndexPage']
    

class RouteIndexPage(Page):    
    class Meta:
        """Meta information."""

        verbose_name = "Главная страница Рейсов"
        verbose_name_plural = "Главная страница Рейсов"
    
    parent_page_types = ['home.HomePage']
    subpage_types = ['home.RoutePage']
    
    
class RoutePage(Page):
    date = models.DateTimeField("Время создания рейса")
    driver = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=False, blank=False)
    expeditions = StreamField(block_types=[
        ('expedition', ExpeditionBlock()),
    ], null=False, blank=False, use_json_field=True)
    finished = models.BooleanField(verbose_name="Рейс завершён", default=False)
    
    search_fields = Page.search_fields + [
        index.SearchField('driver'),
        index.SearchField('expeditions'),
    ]
    
    content_panels = [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Информация о рейсе"),
        FieldPanel('driver'),
        FieldPanel('expeditions'),
        FieldPanel('finished')
    ]
        
    parent_page_types = ['home.RouteIndexPage']
    subpage_types = []
    
    def clean(self):
        super(RoutePage, self).clean()
        expedition_blocks = [block for block in self.expeditions if block.block_type == 'expedition']
        if len(expedition_blocks) > 4:
            raise ValidationError("Максимальное количество экспедиций - 4.")
    
    def save(self, *args, **kwargs):
        self.title = self.driver.email + " " + str(self.date)
        send_mail(
            "НОВЫЙ РЕЙС",
            "У вас новый рейс. Посмотрите на сайте.",
            "from@example.com",
            [self.driver.email],
            fail_silently=False,
        )
        
        super(RoutePage, self).save(*args, **kwargs)

    class Meta:
        """Meta information."""

        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"