from rest_framework.views import APIView
from rest_framework.response import Response
from .contract_loader import ContractLoader
from .serializers import build_dynamic_serializer

contract_loader = ContractLoader(source="local")  # Or "http"


class OrchestratorView(APIView):
    def post(self, request, service_name):
        schema = contract_loader.load(service_name)
        SerializerClass = build_dynamic_serializer(schema)
        serializer = SerializerClass(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Here, call downstream service, run saga steps, etc.
        # For now, just echo back validated data
        return Response({"validated_data": serializer.validated_data})
