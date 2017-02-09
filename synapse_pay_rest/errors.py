"""Custom errors for handling HTTP and API errors."""


class SynapsePayError(Exception):
    """Custom class for handling HTTP and API errors."""
    def __init__(self, message, code, response):
        # print('\nRESPONSE:\n\n', response.json())
        self.message = message
        self.code = code
        self.response = response

    def __repr__(self):
        return '{0}(code={1},message={2})'.format(self.__class__, self.code,
                                                  self.message)


class ClientError(SynapsePayError):
    pass


class BadRequestError(ClientError):
    """Raised on the HTTP status code 400 """
    pass


class UnauthorizedError(ClientError):
    """Raised on the HTTP status code 401 """
    pass


class RequestDeclinedError(ClientError):
    """Raised on the HTTP status code 402 """
    pass


class ForbiddenError(ClientError):
    """Raised on the HTTP status code 403 """
    pass


class NotFoundError(ClientError):
    """Raised on the HTTP status code 404 """
    pass


class NotAcceptableError(ClientError):
    """Raised on the HTTP status code 406 """
    pass


class ConflictError(ClientError):
    """Raised on the HTTP status code 409 """
    pass


class UnsupportedMediaTypeError(ClientError):
    """Raised on the HTTP status code 415 """
    pass


class UnprocessableEntityError(ClientError):
    """Raised on the HTTP status code 422 """
    pass


class TooManyRequestsError(ClientError):
    """Raised on the HTTP status code 429 """
    pass


class ServerError(SynapsePayError):
    """Raised on a 5xx HTTP status code """
    pass


class InternalServerError(ServerError):
    """Raised on the HTTP status code 500 """
    pass


class BadGatewayError(ServerError):
    """Raised on the HTTP status code 502 """
    pass


class ServiceUnavailableError(ServerError):
    """Raised on the HTTP status code 503 """
    pass


class GatewayTimeoutError(ServerError):
    """Raised on the HTTP status code 504 """
    pass


class ErrorFactory():
    """Determines which error to raise based on status code.
    """

    ERRORS = {
        400: BadRequestError,
        401: UnauthorizedError,
        402: RequestDeclinedError,
        403: ForbiddenError,
        404: NotFoundError,
        406: NotAcceptableError,
        409: ConflictError,
        415: UnsupportedMediaTypeError,
        422: UnprocessableEntityError,
        429: TooManyRequestsError,
        500: InternalServerError,
        502: BadGatewayError,
        503: ServiceUnavailableError,
        504: GatewayTimeoutError
    }

    @classmethod
    def from_response(cls, response):
        """Return the corresponding error from a response."""
        # import pdb; pdb.set_trace()
        message, error_code, http_code = cls.parse_error(response)
        klass = cls.ERRORS.get(http_code, SynapsePayError)
        return klass(message=message, code=error_code, response=response)

    @classmethod
    def parse_error(cls, response):
        """Determine error message and code from response body."""
        body = response.json()
        if type(body) is dict and type(body['error']) is dict:
            return [body['error']['en'], body['error_code'],
                    response.status_code]
        else:
            return ['', None, None]
