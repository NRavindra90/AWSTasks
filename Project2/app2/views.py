from django.shortcuts import render,redirect
from app2.models import Product_model

def showindex(request):
    return render(request,"index.html",{"Product_data":Product_model.objects.all()})
def saveproduct(request):
    productid=request.POST.get("t1")
    ProductName=request.POST.get("t2")
    ProductPrice=request.POST.get("t3")
    ProductImage=request.FILES['t4']
    Product_model(Product_id=productid,Product_Name=ProductName,Product_Price=ProductPrice,Product_Image=ProductImage).save()
    return redirect('main')
def delete_product(request):
    id=request.GET.get("id")
    res=Product_model.objects.get(Product_id=id)
    res.delete()
    return redirect('main')