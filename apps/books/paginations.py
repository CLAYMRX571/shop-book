from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 5  
    ordering = '-created_at' 
    cursor_query_param = 'cursor'