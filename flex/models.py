'''Flexible page'''
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.

class FlexPage(Page):
    '''Flexible page class'''
    templates = 'flex/flex_page.html'

    # content = StreamFields
    subtitle = models.CharField(max_length=100,blank=True,null=True)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True,related_name='+',on_delete=models.SET_NULL)
    content = RichTextField(features=["bold", 'italic', ], null=True)

    content_panels = Page.content_panels+[
        FieldPanel('subtitle'),FieldPanel('content'),ImageChooserPanel('image')
    ]

    class Meta:
        verbose_name="Flex Page"
        verbose_name_plural = "Flex Pages"
