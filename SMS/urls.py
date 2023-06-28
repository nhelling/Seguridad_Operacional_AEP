from django.urls import path
from SMS.views import SmsCreateView,list_sms,SmsDeleteView, sms_update

urlpatterns = [
    path('create_sms/', SmsCreateView.as_view(), ),
    path('list_sms/',list_sms),
    path('delete_sms/<int:pk>/',SmsDeleteView.as_view(), name = 'delete_sms' ),
    path('update_sms/<int:pk>/',sms_update, name = 'sms_update' ),
]