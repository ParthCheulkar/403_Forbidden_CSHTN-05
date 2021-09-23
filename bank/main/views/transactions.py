from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from ..models import * 
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse("hey")



@csrf_exempt
def get_transactions(request):
    # user = request.user
    user = User.objects.get(username="Shyren@473793737284")
    if request.method == 'POST':
        acc_type=request.POST['acc_type']
        user_account = Account.objects.get(acc_for=CustomerProfile.objects.get(prof_for=user), acc_type=acc_type)
        transactions = Transaction.objects.filter(Q(sender=user_account) | Q(receiver=user_account))
        for transaction in transactions:
            if transaction.sender == user_account:
                print(f"red {transaction.amount}")
            else:
                print(f"green {transaction.amount}")