from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='expense_tracker_api'),
    path('api/signup', views.generate_api, name='expense_api_generator'),
    path('api/settings', views.settings_view, name='api-settings'),
    path('api/get_currency', views.get_currency, name='api-currency'),
    path('api/add_transaction', views.add_transaction, name='api-add_transaction'),
    path('api/get_transaction', views.get_transactions, name='api-get_transaction'),
    path('api/get_balance', views.get_balance, name='api-get_balance'),
    path('api/filter_by_date_transaction', views.filter_by_date_transactions, name='api-filter_by_date_transaction'),
    path('api/login_securely', views.login_with_api_key, name='api-login-security'),
    path('api/version_control', views.get_app_version, name='api-get_app_version'),
    path('downoad_nexpenz', views.landing_page, name='downoad_nexpenz'),
     path('download_apk', views.download_apk, name='download_apk')


]