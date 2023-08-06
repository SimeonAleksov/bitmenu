from django_tenants.utils import get_tenant
from django_tenants.utils import tenant_context
from rest_framework.response import Response
from rest_framework.views import APIView


class UserList(APIView):
    def get(self, request, format=None):
        tenant = get_tenant(request=request)
        with tenant_context(tenant):
            return Response({'tenant': tenant.name})
