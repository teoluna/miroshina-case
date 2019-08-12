from rest_framework.response import Response
from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'last_page': self.page.paginator.num_pages,
            'results': data
        })