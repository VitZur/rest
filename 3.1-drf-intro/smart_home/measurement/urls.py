from django.urls import path
from .views import SensorListCreate, SensorDetail, MeasurementCreateView

urlpatterns = [

    path('sensors/', SensorListCreate.as_view(), name='sensor-list-create'),

    path('sensors/<int:pk>/', SensorDetail.as_view(), name='sensor-detail'),

    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]
