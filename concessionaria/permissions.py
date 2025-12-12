from rest_framework import permissions

class IsFuncionario(permissions.BasePermission): #Lembrete - Apenas do grupo funcionarios ou adm
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return True
            return request.user.groups.filter(name__iexact='Funcionarios').exists()
        return False

class IsFuncionarioOrReadOnly(permissions.BasePermission): #Lembrete - Leitura para autenticdos
     def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return IsFuncionario().has_permission(request, view)

class IsOwnerOrFuncionario(permissions.BasePermission): # --perfil cliente
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        try:
            if hasattr(obj, 'user'):
                return obj.user == request.user
        except:
            pass
        return False
