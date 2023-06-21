from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view, OpenApiParameter
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from weather_app.apps.forecast import selectors as forecast_selectors
from weather_app.apps.forecast import tasks as forecast_tasks
from weather_app.apps.forecast.api.v1 import serializers as forecast_serializers
from weather_app.celery import celery_app as app


@extend_schema_view(
    get=extend_schema(summary="Forecast list", tags=["Forecast"]),
)
class ForecastListAPIView(ListAPIView):
    """
    API endpoint that retrieves a list of forecasts.
    """
    serializer_class = forecast_serializers.ForecastSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return forecast_selectors.get_all_forecasts().order_by("date")


class RefreshForecastAPIView(GenericAPIView):
    """
    API endpoint that triggers a manual forecast refresh.
    """
    serializer_class = forecast_serializers.RefreshForecastSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Manual forecast refresh", tags=["Forecast"], responses={status.HTTP_200_OK: OpenApiResponse()}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        period = int(serializer.validated_data.get("period", 6))
        forecast_tasks.get_weather_forecast.delay(period=period)
        return Response(status=status.HTTP_200_OK)


class CheckForecastRefreshStatusAPIView(GenericAPIView):
    """
    API endpoint that checks the status of a forecast refresh task by its UUID.
    """
    serializer_class = forecast_serializers.ForecastCheckStatusSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Check forecast refresh status",
        tags=["Forecast"],
        parameters=[
            OpenApiParameter("task_id", OpenApiTypes.UUID, OpenApiParameter.PATH, description="Task UUID"),
        ],
        responses={status.HTTP_200_OK: forecast_serializers.ForecastCheckStatusResponseSerializer},
    )
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        result = app.AsyncResult(str(serializer.validated_data.get("task_id")))
        return Response(data={"status": result.status}, status=status.HTTP_200_OK)
