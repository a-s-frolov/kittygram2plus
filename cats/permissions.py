from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # print(request.get_url_args())
        return (
            request.method in permissions.SAFE_METHODS  # and
            # (request.GET.get('pk') is None or request.GET.get('pk') > 0)
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
