from django import template
from django.template import Context
from django.template.loader import get_template
from django.utils.translation import ugettext as _
import itertools

register = template.Library()

@register.filter
def as_bootstrap(form):
    template = get_template('bootstrap_form/form.html')

    c = Context({
        'form': form
    })

    return template.render(c)

@register.simple_tag()
def buttons(submit_label=_('Submit'), cancel_label=_('Cancel'), class_name='col-sm-offset-3 col-lg-offset-2 col-sm-8 col-lg-4'):

    template = get_template('bootstrap_form/buttons.html')

    c = Context({
        'submit_label': submit_label,
        'cancel_label': cancel_label,
        'class_name': class_name,
    })

    return template.render(c)

@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })

@register.filter
def klass(ob):
    return ob.__class__.__name__.lower()


@register.filter
def chunks(value, chunk_length):
    """
    Breaks a list up into a list of lists of size <chunk_length>
    """
    clen = int(chunk_length)
    i = iter(value)
    while True:
        chunk = list(itertools.islice(i, clen))
        if chunk:
            yield chunk
        else:
            break

@register.filter
def abbreviate(name, pretty=False):
    names = name.split()
    if len(names) == 2:
        return name
    result = [names[0]]
    tiny_name = False
    for surname in names[1:-1]:
        if len(surname) <= 3:
            result.append(surname)
            tiny_name = True
        else:
            if pretty and tiny_name:
                result.append(surname)
            else:
                result.append(surname[0] + '.')
            tiny_name = False
    result.append(names[-1])
    return ' '.join(result)