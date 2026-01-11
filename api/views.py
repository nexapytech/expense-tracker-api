from datetime import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework  import status
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey
# Create your views here.
from rest_framework_api_key.permissions import HasAPIKey
from .models import AppSetting, AddTransaction
from .serializers import AppSettingsSerializer, AddtransactionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.db.models import Sum
def homepage(request):
    return render(request, 'index.html')

@api_view(['POST'])
def generate_api(request):
    try:
        username= request.POST.get('username')
        print(username)
        if not username:
            return Response({"error": "Username is required"})
            # Prevent duplicate keys for same username
        if APIKey.objects.filter(name=username).exists():
            return Response({"error": "Username already taken cannot generate api key"})

        api_key, key = APIKey.objects.create_key(name=username)

        return Response({
            'success':True,
            "username": username,
            "api_key": key
        })
    except Exception as e:
        print(e)
@api_view(['GET', 'POST'])
@permission_classes([HasAPIKey])
def login_with_api_key(request):
    key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
    # Use the provided helper to get the object
    api_key_obj = APIKey.objects.get_from_key(key)
    if request.method == 'POST':
        if api_key_obj:
            return Response({'success': 'api key key exist login in', 'api_key':key})
        else:
            return Response('invalid API Key provided', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([HasAPIKey])
def settings_view(request):
    key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
    # Use the provided helper to get the object
    api_key_obj = APIKey.objects.get_from_key(key)
    # Try to get or create settings for this API key
    settings, _ = AppSetting.objects.get_or_create(api_key=api_key_obj)

    if request.method == 'GET':
        serializer = AppSettingsSerializer(settings)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppSettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([HasAPIKey])
def get_currency(request):
    key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
    # Use the provided helper to get the object
    api_key_obj = APIKey.objects.get_from_key(key)
    # Try to get or create settings for this API key
    settings, _ = AppSetting.objects.get_or_create(api_key=api_key_obj)

    if request.method == 'GET':
        serializer = AppSettingsSerializer(settings)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([HasAPIKey])
def add_transaction(request):
    key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
    # Use the provided helper to get the object
    api_key_obj = APIKey.objects.get_from_key(key)
    # Try to get or create settings for this API key
    transaction_type = request.data.get("type")
    amount = float(request.data.get("amount", 0))
    # Calculate current balance: income - expense
    total_income = AddTransaction.objects.filter(api_key=api_key_obj, type="income").aggregate(total=Sum("amount"))[
                       "total"] or 0
    total_expense = AddTransaction.objects.filter(api_key=api_key_obj, type="expense").aggregate(total=Sum("amount"))[
                        "total"] or 0
    balance = total_income - total_expense

    if transaction_type == "expense" and amount > balance:
        return Response(
            {"error": "Insufficient balance to add this expense."},
            status=status.HTTP_400_BAD_REQUEST
        )
    add_transaction= AddTransaction.objects.create(api_key=api_key_obj)
    if request.method == 'POST':
        serializer = AddtransactionSerializer(add_transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([HasAPIKey])
def get_transactions(request):
    try:
        key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
        # Use the provided helper to get the object
        api_key_obj = APIKey.objects.get_from_key(key)
        # Try to get or create settings for this API key

        transactions = AddTransaction.objects.filter(api_key=api_key_obj).order_by('-date', '-created_at')

    except Exception as e:
        print('something went wrong', e)
    if request.method == 'GET':
        limit = int(request.query_params.get('limit', 10))
        gettransaction = transactions[:limit]
        serializer = AddtransactionSerializer(gettransaction, many=True)
        return Response(serializer.data)
@api_view(['GET'])
@permission_classes([HasAPIKey])
def filter_by_date_transactions(request):
    try:
        key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
        api_key_obj = APIKey.objects.get_from_key(key)
        transactions = AddTransaction.objects.filter(api_key=api_key_obj).order_by('-date')

        # Optional date filtering
        start_date = request.query_params.get('start')
        end_date = request.query_params.get('end')
        if start_date and end_date:
            try:
                start = datetime.strptime(start_date, '%Y-%m-%d').date()
                end = datetime.strptime(end_date, '%Y-%m-%d').date()
                transactions = transactions.filter(date__range=(start, end))
            except ValueError:
                return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)



        serializer = AddtransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    except Exception as e:
        print('Error:', e)
        return Response({"error": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
@permission_classes([HasAPIKey])
def get_total_income(request):
    key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
    # Use the provided helper to get the object
    api_key_obj = APIKey.objects.get_from_key(key)

    total = AddTransaction.objects.filter(api_key=api_key_obj, type="income").aggregate(Sum("amount"))["amount__sum"] or 0
    total = "{:.2f}".format(float(total))
    return Response({"total_income": total})
@api_view(['GET'])
@permission_classes([HasAPIKey])
def get_total_expense(request):
    key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
    # Use the provided helper to get the object
    api_key_obj = APIKey.objects.get_from_key(key)

    total = AddTransaction.objects.filter(api_key=api_key_obj, type="expense").aggregate(Sum("amount"))["amount__sum"] or 0
    total = "{:.2f}".format(float(total))
    return Response({"total_expense": total})


@api_view(['GET'])
@permission_classes([HasAPIKey])
def get_balance(request):
    key = request.headers.get("Authorization", "").replace("Api-Key ", "").strip()
    # Use the provided helper to get the object
    api_key_obj = APIKey.objects.get_from_key(key)

    total_income = AddTransaction.objects.filter(api_key=api_key_obj, type="income").aggregate(Sum("amount"))[
                "amount__sum"] or 0
    total_income = "{:.2f}".format(float(total_income))

    total_expense = AddTransaction.objects.filter(api_key=api_key_obj, type="expense").aggregate(Sum("amount"))["amount__sum"] or 0
    total_expense = "{:.2f}".format(float(total_expense))

    balance = float(total_income) - float(total_expense)
    balance = "{:.2f}".format(balance)
    return Response({"total_expense": total_expense ,'total_income':total_income , 'total_balance':balance})


@api_view(['GET'])
def get_app_version(request):
        data = {
            "latest_version": "1.2.0",
            "update_message": "A new version of Nexapy Expense Tracker is available. Please update!",
            "update_url": "https://nexpenz.nexapytechnologies.com/app"
        }
        return Response(data)




def landing_page(request):
    return render(request, 'download_page.html')


import os
from django.conf import settings
from django.http import FileResponse, Http404

def download_apk(request):
    apk_path = os.path.join(settings.BASE_DIR, 'media', 'nexpenz-1.0.0.apk')
    if os.path.exists(apk_path):
        return FileResponse(open(apk_path, 'rb'), as_attachment=True, filename='nexpenz-v1.0.0.apk')
    else:
        raise Http404("APK file not found")