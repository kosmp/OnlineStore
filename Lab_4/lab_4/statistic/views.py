from django.shortcuts import render, get_object_or_404
from order.models import Order, OrderItem
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from store.models import Product, ModelType, ProductType
from .forms import StatisticForm
import os
from django.conf import settings
import pandas
import datetime
from django.core.exceptions import PermissionDenied
from typing import Dict
from django.db.models import Sum

def statistic_show(request) :
    if not request.user.is_superuser:
        raise PermissionDenied("You do not have access to this page.")
    
    form = StatisticForm()
    pt = dict()

    x = []
    y = []

    for ord in Order.objects.all():
        pt[str(ord.created.year) + '.'+str(ord.created.month)+'.'+str(ord.created.day)] = 0

    for ord in Order.objects.all():
        pt[str(ord.created.year) + '.'+str(ord.created.month)+'.'+str(ord.created.day)] += 1

    for tmp in pt:
        x.append(tmp)
        y.append(pt[tmp])

    plt.plot(x,y, 'ro')

    if(request.method == "GET"):

        plt.savefig(os.path.join(settings.MEDIA_ROOT, 'schedule.jpg'), format='jpg')
        plt.clf()
        return render(request, 'statistic/statistic.html')

def tables_show(request):
    if not request.user.is_superuser:
        raise PermissionDenied("You do not have access to this page.")
    
    #таблица товар - ордер
    product_list = list(Product.objects.all())
    product_list.sort(key = lambda x:x.purchase_count, reverse=True)

    greatest_demand=product_list[0]
    least_demand=product_list[-1]

    #сводная таблица по количеству
    ords = list(OrderItem.objects.all())

    dates_arr = set()

    for tmp in ords:
        dates_arr.add(tmp.order.created.date().strftime("%Y-%m-%d"))

    dates_arr = list(dates_arr)
    out_dict:Dict[str,Dict[str, int]]
    out_dict = dict()
    total = dict()

    for tmp in ords:
        out_dict[tmp.product.type.name] = dict()

    for tmp in ords:
        out_dict[tmp.product.type.name][tmp.order.created.date().strftime("%Y-%m-%d")] = 0
        total[tmp.order.created.date().strftime("%Y-%m-%d")] = 0

    for tmp in ords:
        out_dict[tmp.product.type.name][tmp.order.created.date().strftime("%Y-%m-%d")] += tmp.quantity
        total[tmp.order.created.date().strftime("%Y-%m-%d")] += tmp.quantity

    out_dict['total'] = total
    print(out_dict)
    row = list()
    row.append('Product type')
    for tmp in total:
        row.append(tmp)

    out_list = list()
    out_list.append(row)
    for tmp in out_dict:
        row = list()
        row.append(tmp)
        for tmp1 in out_dict[tmp]:
            row.append(out_dict[tmp][tmp1])

        out_list.append(row)

    product_table = out_list

    ################################
    #Сводная по ценам
    

    ords = list(OrderItem.objects.all())

    dates_arr = set()

    for tmp in ords:
        dates_arr.add(tmp.order.created.date().strftime("%Y-%m-%d"))

    dates_arr = list(dates_arr)
    out_dict:Dict[str,Dict[str, int]]
    out_dict = dict()
    total = dict()

    for tmp in ords:
        out_dict[tmp.product.type.name] = dict()

    for tmp in ords:
        out_dict[tmp.product.type.name][tmp.order.created.date().strftime("%Y-%m-%d")] = 0
        total[tmp.order.created.date().strftime("%Y-%m-%d")] = 0

    for tmp in ords:
        out_dict[tmp.product.type.name][tmp.order.created.date().strftime("%Y-%m-%d")] += tmp.quantity * tmp.price
        total[tmp.order.created.date().strftime("%Y-%m-%d")] += tmp.quantity * tmp.price

    out_dict['total'] = total

    row = list()
    row.append('Product type')
    for tmp in total:
        row.append(tmp)

    out_list = list()
    out_list.append(row)
    for tmp in out_dict:
        row = list()
        row.append(tmp)
        for tmp1 in out_dict[tmp]:
            row.append(out_dict[tmp][tmp1])

        out_list.append(row)

    profit_table=out_list

    ################################
    #Сводная по количеству за месяц

    ords = list(OrderItem.objects.all())

    dates_arr = set()

    for tmp in ords:
        dates_arr.add(tmp.order.created.date().strftime("%Y-%m"))

    dates_arr = list(dates_arr)
    out_dict:Dict[str,Dict[str, int]]
    out_dict = dict()
    total = dict()

    for tmp in ords:
        out_dict[tmp.product.type.name] = dict()

    for tmp in ords:
        out_dict[tmp.product.type.name][tmp.order.created.date().strftime("%Y-%m")] = 0
        total[tmp.order.created.date().strftime("%Y-%m")] = 0

    for tmp in ords:
        out_dict[tmp.product.type.name][tmp.order.created.date().strftime("%Y-%m")] += tmp.quantity
        total[tmp.order.created.date().strftime("%Y-%m")] += tmp.quantity

    out_dict['total'] = total

    row = list()
    row.append('Product type')
    for tmp in total:
        row.append(tmp)

    out_list = list()
    out_list.append(row)
    for tmp in out_dict:
        row = list()
        row.append(tmp)
        for tmp1 in out_dict[tmp]:
            row.append(out_dict[tmp][tmp1])

        out_list.append(row)

    sales_per_month_table=out_list

    ################################
    #Сводная по количеству за год

    ords = list(OrderItem.objects.all())

    dates_arr = set()

    for tmp in ords:
        dates_arr.add(tmp.order.created.date().strftime("%Y"))

    dates_arr = list(dates_arr)
    out_dict:Dict[str,Dict[str, int]]
    out_dict = dict()
    total = dict()

    for tmp in ords:
        out_dict[tmp.product.type.name] = dict()

    for tmp in ords:
        out_dict[tmp.product.type.name][tmp.order.created.date().strftime("%Y")] = 0
        total[tmp.order.created.date().strftime("%Y")] = 0

    for tmp in ords:
        out_dict[tmp.product.type.name][tmp.order.created.date().strftime("%Y")] += tmp.quantity * tmp.price
        total[tmp.order.created.date().strftime("%Y")] += tmp.quantity * tmp.price

    out_dict['total'] = total
  
    row = list()
    row.append('Product type')
    for tmp in total:
        row.append(tmp)

    out_list = list()
    out_list.append(row)
    for tmp in out_dict:
        row = list()
        row.append(tmp)
        for tmp1 in out_dict[tmp]:
            row.append(out_dict[tmp][tmp1])

        out_list.append(row)

    return render(request, 'statistic/tables.html', context={'product_table' : product_list, 'pivot_table' : product_table,
                                                              'profit_table' : profit_table, 'sales_per_month_table' : sales_per_month_table,
                                                              'profit_per_year_table' : out_list , 'least_demand' : least_demand, 
                                                              'greatest_demand' : greatest_demand})

def predict_show(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied("You do not have access to this page.")

    name = Product.objects.get(id=id).name
    
    ords = list(OrderItem.objects.all())
    date_arr = list()
    for tmp in ords:
        if tmp.product.name == name:
            print(tmp.order.created)
            date_arr.append(tmp.order.created)

    if (len(date_arr) == 0):
        return render(request, 'statistic/zero_orders.html')

    min_date = min(date_arr)
    max_count = 0
    min_count = 10000
    sum = 0
    max_date = max(date_arr)

    dates_for_plot = pandas.date_range(min_date, max_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d").to_list()
    print(dates_for_plot)

    dict_for_plot = dict()

    for tmp in dates_for_plot:
        dict_for_plot[tmp] = 0

    for tmp in dates_for_plot:
        for tmp_ord in OrderItem.objects.all():
            if (tmp_ord.order.created.strftime("%Y-%m-%d") == tmp):
                dict_for_plot[tmp] += tmp_ord.quantity
                max_count = max(max_count,tmp_ord.quantity)
                min_count = min(min_count, tmp_ord.quantity)
                sum += tmp_ord.quantity

    avg = (max_count+min_count)/2
    coef = sum/len(dict_for_plot)
    coef = avg/coef
    coef -= 1 #coef evyj;fnm
    if (coef < 0):
        coef *= -1
    max_date += datetime.timedelta(days=1)
    print(pandas.date_range(max_date, periods = 1, freq ='d',).strftime("%Y-%m-%d").to_list())
    sz = len(dict_for_plot)
    
    for i in range(sz):
        print(max_date)
        dt = pandas.date_range(max_date, periods = 2, freq ='d',).strftime("%Y-%m-%d").to_list()[0]
        val = dict_for_plot[dates_for_plot[-(i-1)]]*coef
        dict_for_plot[dt]=round((val + avg)/2)
        max_date += datetime.timedelta(days=1)
        
    x_list = list()
    y_list = list()

    for tmp in dict_for_plot:
        x_list.append(tmp)
        y_list.append(dict_for_plot[tmp])
    
    plt.figure().set_figwidth(len(x_list)//1.5);
    plt.plot(x_list,y_list)
    plt.xticks(rotation=340)
    plt.savefig(os.path.join(settings.MEDIA_ROOT, 'predict.jpg'), format='jpg')
    plt.close()

    return render(request, 'statistic/predict.html')