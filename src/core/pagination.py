from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class Pagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'page_size': settings.REST_FRAMEWORK['PAGE_SIZE'],
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })
