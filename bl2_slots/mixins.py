from django.http import HttpResponse
from django.utils import simplejson as json


class JSONResponseMixin(object):
    """
    A mixin that allows you to easily serialize simple data such as a dict or
    Django models.

    Copied from django-braces (https://github.com/brack3t/django-braces/) and
    modified to allow an optional status code to be specified.
    """
    content_type = "application/json"
    status = 200

    def get_content_type(self):
        if self.content_type is None:
            raise ImproperlyConfigured(u"%(cls)s is missing a content type. "
                u"Define %(cls)s.content_type, or override "
                u"%(cls)s.get_content_type()." % {
                "cls": self.__class__.__name__
            })
        return self.content_type

    def get_status(self):
        if self.status is None:
            raise ImproperlyConfigured(u"%(cls)s is missing a status. "
                u"Define %(cls)s.status, or override "
                u"%(cls)s.get_status()." % {
                "cls": self.__class__.__name__
            })
        return self.status

    def render_json_response(self, context_dict, status=None):
        """
        Limited serialization for shipping plain data. Do not use for models
        or other complex or custom objects.
        """
        json_context = json.dumps(context_dict)
        if status is None:
            status = self.get_status()
        return HttpResponse(json_context, content_type=self.get_content_type(),
            status=status)
