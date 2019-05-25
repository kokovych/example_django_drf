from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        error_detail = response.data
        current_detail = error_detail.get('detail')
        new_response = {
            "error": current_detail
        }
        response = Response(data=new_response)

    return response
