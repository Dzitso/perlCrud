from django.shortcuts import render, redirect, get_object_or_404
from .models import  Item
# Create your views here.

# create item
def create_item(request):
    if request.method =='POST':
        name =request.POST.get('name')
        description=request.POST.get('description')
        Item.objects.create(name=name, description=description)
        return  redirect('item_list')
    return  render(request, 'item_form.html')
# read item
def read_item(request):
    items=Item.objects.all()
    return render(request, 'item_list.html',{'items':items})
# update item
def update_item (request,pk):
    item=get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.name=request.POST.get('name')
        item.description=request.POST.get('description')
        item.save()
        return  redirect('item_list')
    return  render(request, 'item_form.html', {'item':item})
# delete item
def delete_item(request, pk):
    item=get_object_or_404(Item, pk=pk)
    if request.method=="POST":
        item.delete()
        return  redirect('item_list')
    return  render(request, 'item_confirm_delete.html', {'item':item})
