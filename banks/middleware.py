import logging


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
