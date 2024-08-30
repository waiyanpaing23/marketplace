from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item, Category

@login_required
def index(request):
    items = Item.objects.filter(created_by = request.user)
    categories = Category.objects.filter(items__in=items)

    return render(request, 'dashboard/index.html', {
        'items' : items,
        'categories' : categories
    } )
