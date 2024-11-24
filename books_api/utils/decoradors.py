from drf_spectacular.utils import extend_schema


def generate_schema(serializer, many=False, **kwargs):
    """
    Generate a reusable schema decorator based on the provided serializer.

    :param serializer: The serializer class to use for request/response.
    :param many: Whether the response should expect multiple objects.
    :return: A schema decorator.
    """
    return extend_schema(
        request=serializer,
        responses=serializer(many=many),
        *kwargs
    )
