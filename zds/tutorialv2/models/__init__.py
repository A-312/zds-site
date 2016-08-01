# coding: utf-8

from django.utils.translation import ugettext_lazy as _


CONTENT_TYPES = (
    # Configuration of content names
    # name                : the ID of content (unique and uppercase)
    # verbose_name        : name of content
    # verbose_name_plural : plural name of content
    # parent_name         : the category name which contains this content
    # validation_before   : Boolean; whether this content has to be validated before publication
    # single_container    : True or False ; True if the content is a single container
    # beta                : True or False ; True if the content can be in beta
    {
        'name': 'TUTORIAL',
        'verbose_name': 'tutoriel',
        'verbose_name_plural': 'tutoriels',
        'parent_name': 'tutoriel',
        'validation_before': True,
        'single_container': False,
        'beta': True,
    },
    {
        'name': 'ARTICLE',
        'verbose_name': 'article',
        'verbose_name_plural': 'articles',
        'parent_name': 'article',
        'validation_before': True,
        'single_container': True,
        'beta': True,
    },
    {
        'name': 'OPINION',
        'verbose_name': 'billet',
        'verbose_name_plural': 'billets',
        'parent_name': 'tribune',
        'validation_before': False,
        'single_container': True,
        'beta': False,
    },
)

# a list of contents which have to be validated before publication
CONTENT_TYPES_VALIDATION_BEFORE = [content['name'] for content in CONTENT_TYPES if content['validation_before']]

# a list of contents which have one big container containing at least one small container
SINGLE_CONTAINER = [content['name'] for content in CONTENT_TYPES if content['single_container']]

# a list of contents which can be in beta
CONTENT_TYPES_BETA = [content['name'] for content in CONTENT_TYPES if content['beta']]


TYPE_CHOICES = (
    ('TUTORIAL', 'Tutoriel'),
    ('ARTICLE', 'Article'),
    ('OPINION', 'Billet'),
)

# a single list with all types
CONTENT_TYPE_LIST = [type_[0] for type_ in TYPE_CHOICES]

TYPE_CHOICES_DICT = dict(TYPE_CHOICES)

STATUS_CHOICES = (
    ('PENDING', _(u'En attente d\'un validateur')),
    ('PENDING_V', _(u'En cours de validation')),
    ('ACCEPT', _(u'Publié')),
    ('REJECT', _(u'Rejeté')),
    ('CANCEL', _(u'Annulé'))
)
