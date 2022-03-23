from django.shortcuts import render, redirect
from .models import Items
from django.http import Http404

# Create your views here.
def item_list(request):
    items = Items.objects.all()
    return render(request, "store/item_list.html", context={
        "items": items
    })

def item_detail(request, id):
    if id == 0:
        raise Http404
    item = Items.objects.filter(pk=id).first()
    if item is None:
        return redirect("store:item_list")
    return render(request, "store/item_detail.html", context={
        "item": item
    })

def to_google(request):
    return redirect("https://www.google.com")

def one_item(request):
    return redirect("store:item_detail", id=1)

def page_not_found(request, exception):
    return render(request, "store/404.html", status=404)
    # return redirect("store:item_list")
