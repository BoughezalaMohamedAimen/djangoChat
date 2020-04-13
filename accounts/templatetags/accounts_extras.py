from django import template
from accounts.models import UserProfile


register = template.Library()



@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })


def htmlattributes(value, arg):
    attrs = value.field.widget.attrs


    data = arg.replace(' ', ' ')

    kvs = data.split(',')

    for string in kvs:
        kv = string.split(':')
        attrs[kv[0]] = kv[1]

    rendered = str(value)

    return rendered

register.filter('htmlattributes', htmlattributes)


@register.simple_tag
def get_unread(reciverr, senderr):
    return reciverr.count_unread(senderr)