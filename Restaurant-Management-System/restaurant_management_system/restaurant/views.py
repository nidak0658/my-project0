from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Table, Reservation, Order, OrderItem, Inventory
from django.db.models import Sum

def menu_items(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/menu_items.html', {'menu_items': menu_items})

def tables(request):
    tables = Table.objects.all()
    return render(request, 'restaurant/tables.html', {'tables': tables})

def reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'restaurant/reservations.html', {'reservations': reservations})

def create_reservation(request):
    if request.method == 'POST':
        table_id = request.POST.get('table')
        guest_name = request.POST.get('guest_name')
        guest_phone = request.POST.get('guest_phone')
        reservation_time = request.POST.get('reservation_time')

        table = get_object_or_404(Table, pk=table_id)

        reservation = Reservation(table=table, guest_name=guest_name, guest_phone=guest_phone, reservation_time=reservation_time)
        reservation.save()

        return redirect('reservations')

    tables = Table.objects.all()
    return render(request, 'restaurant/create_reservation.html', {'tables': tables})

def place_order(request, table_id):
    if request.method == 'POST':
        table = get_object_or_404(Table, pk=table_id)
        items = request.POST.getlist('items')

        order = Order(table=table)
        order.save()

        total_amount = 0

        for item_id in items:
            menu_item = get_object_or_404(MenuItem, pk=item_id)
            quantity = int(request.POST.get(f'quantity_{item_id}', 0))
            total_amount += menu_item.price * quantity

            OrderItem.objects.create(order=order, item=menu_item, quantity=quantity)

        order.total_amount = total_amount
        order.save()

        return redirect('tables')

    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/place_order.html', {'menu_items': menu_items})

def inventory(request):
    inventory_items = Inventory.objects.all()
    return render(request, 'restaurant/inventory.html', {'inventory_items': inventory_items})

def report(request):
    total_sales = Order.objects.aggregate(total_sales=Sum('total_amount'))['total_sales'] or 0
    total_orders = Order.objects.count()
    return render(request, 'restaurant/report.html', {'total_sales': total_sales, 'total_orders': total_orders})
