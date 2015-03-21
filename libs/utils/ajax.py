# encoding: utf-8
from __future__ import unicode_literals, absolute_import


def serialize_form_errors(forms):
    if not isinstance(forms, (list, tuple)):
        forms = [forms]

    errors = {}
    errors["details"] = {}

    for form in forms:
        prefix = ''
        if form.prefix:
            prefix = '%s-' % form.prefix

        for field in form.errors:
            if field == '__all__':
                errors["messages"] = form.errors[field]
            else:
                errors["details"]["%s%s" % (prefix, field)] = form.errors[field]

    return errors