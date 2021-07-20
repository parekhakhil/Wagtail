from re import template
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    '''Home page model '''
    template = 'home/home_page.html'

    #This doesnt allow admin to create child page of home
    # max_count = 1

    #Add the banner title field in home page datatable
    banner_title = models.CharField(max_length=200,null=True,blank=True)
    
    #grab a default content panel and add the recently added banner_title field to it for able to display banner title in editor
    content_panels = Page.content_panels + [
        FieldPanel('banner_title')
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
