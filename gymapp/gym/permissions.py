from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Разрешает только администраторам изменять данные.
    Всем остальным разрешён только доступ на чтение.
    """
    def has_permission(self, request, view):
        # SAFE_METHODS включает 'GET', 'HEAD' и 'OPTIONS'
        if request.method in SAFE_METHODS:
            return True
        # Разрешить доступ только администраторам для других методов
        return request.user and request.user.is_staff
