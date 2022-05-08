import imp


import logging
from django.utils.deprecation import MiddlewareMixin

application_logger = logging.getLogger("application-logger")

class MyMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass