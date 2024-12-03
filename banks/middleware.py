import logging

from constance import config
from django.http import JsonResponse

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(
            f"Request: {request.method} {request.path} - User: {request.user.username if request.user.is_authenticated else 'Anonymous'}"
        )

        response = self.get_response(request)
        logger.info(f"Response status: {response.status_code}")

        return response


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(config, 'MAINTENANCE_MODE', False):
            return JsonResponse(
                {'error': 'The system is currently under maintenance. Please try again later.'},
                status=503
            )

        return self.get_response(request)
