# -*- coding: utf-8 -*-
from classytags.arguments import StringArgument, Argument
from classytags.core import Options
from classytags.helpers import AsTag
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='simple_csspath')
@stringfilter
def convert_path_to_css_classes(val, separator='-'):
    """
    Allows using the request URL path component to paint pages based on
    specific CSS classes.

    Usage::
        {% load csspath %}
        <body class="{{ request.path|simple_csspath }}">

    Given a path of /a/b/c/d/e, yields::
        <body class="a a-b a-b-c a-b-c-d a-b-c-d-e">

    Given a path of /a/b/c, yields::
        <body class="a a-b a-b-c">

    Also accepts a custom separator (using /a/b/c)::
        <body class="{{ request.path|simple_csspath:"__" }}">
        {# becomes #}
        <body class="a a__b a__b__c">

    Based on original gist I threw up https://gist.github.com/kezabelle/7789258
    """
    # tidy up given path ...
    parts = list(val.strip('/').split('/'))
    results = []
    while len(parts):
        # reduce the existing parts by 1
        lastpart = parts.pop()
        if len(parts):
            # if there are still parts, join them all together and then add
            # our last part.
            previous_parts = separator.join(parts)
            results.append('{prev}{sep}{new}'.format(prev=previous_parts,
                                                     sep=separator, new=lastpart))  # noqa
        else:
            # no other parts remain, so just put our last one on the stack.
            results.append(lastpart)
    # reverse from least-specific to most-specific
    return ' '.join(reversed(results))


class ComplexCssPath(AsTag):
    """
    When the `simple_csspath` filter just won't cut it, because you need
    prefixes or suffixes, the `{% csspath %}` template tag may be used.

    Usage::
        {% load csspath %}
        <body class="{% csspath request.path '-' 'prefix--' '__suffix' %}">

    May also be used like so::
        {% csspath request.path '-' 'prefix--' '__suffix' as classes %}
        {% for class in classes %}
        {# do something #}
        {{ class }}
        {% endfor %}
    """
    name = 'csspath'
    options = Options(
        Argument('input', resolve=True, required=True),
        StringArgument('separator', resolve=True, required=False, default='-'),
        StringArgument('prefix', resolve=True, required=False, default='path-'),
        StringArgument('suffix', resolve=True, required=False, default=''),
        'as',
        Argument('varname', resolve=False, required=False),
    )

    def iterator(self, input, separator, prefix, suffix):
        basic = convert_path_to_css_classes(input, separator=separator)
        for part in basic.split(' '):
            if not part.strip():
                part = 'root'
            yield '{prefix}{part}{suffix}'.format(
                prefix=prefix if not part.startswith(prefix) else '',
                suffix=suffix if not part.endswith(suffix) else '',
                part=part,
            )

    def get_value(self, context, input, separator, prefix, suffix, **kwargs):
        return tuple(self.iterator(input=input, separator=separator,
                                   prefix=prefix, suffix=suffix))

    def render_tag(self, context, **kwargs):
        result = super(ComplexCssPath, self).render_tag(context, **kwargs)
        # will turn the tuple into a string, or if used as an AsTag, will remain
        # as ''
        return ' '.join(result)

register.tag(ComplexCssPath)
