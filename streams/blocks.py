'''Streamfield live in here'''
from pyexpat import features
from re import template
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True,help_text="Add your title")
    text = blocks.TextBlock(required=True,help_text="Add additional text")

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = 'edit'
        label = "Title & Text"

class RichTextBlock(blocks.RichTextBlock):
    '''Richtext with all the features'''
    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'edit'
        label = 'Full Richtext'


class CardBlock(blocks.StructBlock):
    """Cards with image and text as well as button"""
    title = blocks.TextBlock(required=True,help_text='Insert card title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image',ImageChooserBlock(required=True)),
                ('title',blocks.CharBlock(required=True,max_length=40)),
                ('description',blocks.CharBlock(required=True,max_length=150)),
                ('button_page',blocks.PageChooserBlock(required=False)),
                ('button_url',blocks.URLBlock(required=False,help_text='Add the link you wants to redirect on click')),
                ('button_text',blocks.CharBlock(
                    required=True, default='Learn more', max_length=40)),
            ]
        )
    )

    class Meta:
        template = 'streams/cards_block.html'
        icon='edit'
        label = 'Add Card'


class CTABlock(blocks.StructBlock):
    """A simple call to action section"""
    title = blocks.CharBlock(required=True,max_length=50)
    text = blocks.RichTextBlock(required=True,features=['bold','italic','link'])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=True)
    button_text =blocks.CharBlock(required=True,default='Learn more',max_length=40)

    class Meta:
        template = 'streams/cta_block.html'
        icon='placeholder'
        label = "Call To Action"
