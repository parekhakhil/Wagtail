from pyexpat import features
from re import template
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField

class HomePage(Page):
    '''Home page model '''
    template = 'home/home_page.html'

    #This doesnt allow admin to create child page of home
    # max_count = 1

    #Add the banner title field in home page datatable
    banner_title = models.CharField(max_length=200,null=True,blank=True)
    content = RichTextField(features=["bold",'italic',],null=True)
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=False,related_name='+',on_delete=models.SET_NULL)
    banner_cta = models.ForeignKey('wagtailcore.Page',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')

    #Anything outside wagtail is being added to the wagtail it needs to add in content_panel
    #grab a default content panel and add the recently added banner_title field to it for able to display banner title in editor
    content_panels = Page.content_panels + [
        FieldPanel('banner_title'), FieldPanel('content'), ImageChooserPanel('image'),PageChooserPanel('banner_cta')
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
