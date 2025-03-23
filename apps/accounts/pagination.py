from rest_framework.pagination import PageNumberPagination

class UserPagination(PageNumberPagination):
    page_size = 10 

class ListUsersView(APIView):
    permission_classes = [IsAdminUser]
    pagination_class = UserPagination

    def get(self, request):
        users = User.objects.all()
        paginator = UserPagination()
        paginated_users = paginator.paginate_queryset(users, request)
        usernames = [user.username for user in paginated_users]
        return paginator.get_paginated_response(usernames)