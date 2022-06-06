
from django.views.generic import (FormView, UpdateView, TemplateView, DeleteView, 
CreateView, ListView)
from django.contrib.auth.mixins import LoginRequiredMixin
import csv
from multiprocessing.spawn import import_main_path
from tkinter.tix import Tree
from tokenize import String
from unittest import result
import xlwt
from django.shortcuts import render, redirect
from .models import Project, Test
from .forms import ProjectForm, Profile, UserUpdate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from datetime import datetime
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login, logout



def Input(request, pk):
    strtempstring = pk
    temp = strtempstring.split("=")
    print(temp)
    if (strtempstring == ''):
        print("S1")
    elif (temp[1] == ''):
        dateandtime = datetime.now().strftime('%Y%m%d%H%M%S')
        query_results = Test.objects.filter().order_by("-CreatedAt")[:1].values("mac_id", "Device", "Key")
        strTemp = str(query_results[0])
        strTempList = strTemp.split("'")
        mac = str(strTempList[3])
        key = str(strTempList[5])
        return HttpResponse('RIS=*' + dateandtime + "<'. " + dateandtime + mac + "&" + key + ".'>")
    elif (temp[1] == ''):
        print("S2")
        dateandtime = datetime.now().strftime('%Y%m%d%H%M%S')
        query_results = Test.objects.filter().order_by("-CreatedAt")[:1].values("mac_id", "Device", "Key")
        strTemp = str(query_results[0])
        print(strTemp)
        strTempList = strTemp.split("'")
        print(strTempList)
        mac = str(strTempList[3])
        data = str(strTempList[7])
        return HttpResponse('RIS=*' + dateandtime + "<'. " + dateandtime + mac + "&" + data + ".'>")
    elif (len(temp) == 2 ):
        print("S5")
        dateandtime = datetime.now().strftime('%Y%m%d%H%M%S')
        query_results = Test.objects.filter().order_by("-CreatedAt")[:1].values("mac_id", "Device", "Key")
        strTemp = str(query_results[0])
        print(strTemp)
        strTempList = strTemp.split("'")
        print(strTempList)
        mac = str(strTempList[3])
        data = str(strTempList[11])
        return HttpResponse('RIS=*' + dateandtime + "<'. " + dateandtime + mac + "&" + data + ".'>")
    else:
        print("S4")
        temp = strtempstring.split("=", 2)
        if (len(temp) > 2 and temp[2] != ''):
            print("S3")
            strdata = "1=" + temp[0] + "2=" + temp[1] + "6=" + temp[2]
            temp2 = temp[1]
            Temp1 = temp2.split("@", 2)
            dateandtime = datetime.now().strftime('%Y%m%d%H%M%S')
            Temp3 = "3=" + Temp1[0] + "4=" + Temp1[1] + "5=" + Temp1[2]
            temp3 = temp[2]
            Temp4 = temp3.split("&")
            Temp5 = "7=" + Temp4[0] + "8=" + Temp4[1] + "9=" + Temp4[2] + "10" + Temp4[3] + "11=" + Temp4[4] + "12=" + \
                    Temp4[5] + "13=" + Temp4[6] + "14=" + Temp4[7] + "15=" + Temp4[8] + "16=" + Temp4[9] + "17=" +\
                    Temp4[10]+ "18=" + Temp4[11] + "19=" + Temp4[12] + "20=" + Temp4[13] + "21=" + Temp4[14]
            Test.objects.create(Device=Temp1[0], mac_id=Temp1[1], Key=Temp1[2], Username=Temp4[0], UsageDateAndTime=Temp4[1],
            Temperature=Temp4[2], pHin=Temp4[3], TDSin=Temp4[4], pHout=Temp4[5], TDSout=Temp4[6], MotorONInSeconds=Temp4[7],
            VolumeSampled=Temp4[8], NoOfHourUsed=Temp4[9], CartridgeLifeLeft=Temp4[10],OutputTankDown=Temp4[14],
                                OutputTankUp=Temp4[13],InputTankUp=Temp4[12],InputTankDown=Temp4[11], OperationStatus=Temp4[15])
            return HttpResponse('RIS=*' + dateandtime + "<'. " + dateandtime + str(pk) + strdata + Temp3 + ".'>")
        else:
            temp2 = temp[1]
            Temp1 = temp2.split("@", 2)
            dateandtime = datetime.now().strftime('%Y%m%d%H%M%S')
            query_results = Test.objects.filter(mac_id=Temp1[1]).order_by("-CreatedAt")[:1].values("mac_id", "Key",
                                                                                                   "Device")
            strTemp = str(query_results[0])
            strTempList = strTemp.split("'")
            mac = str(strTempList[3])
            data = str(strTempList[7])
            return HttpResponse('RIS=*' + dateandtime + "<'. " + dateandtime + mac + "&" + data + ".'>")


# def loginenter(request):
   
#     return render(request, 'home/login.html')


def register(request):
    form = ProjectForm

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("EtBr-login")
    context = {'form': form}
    return render(request, 'home/registration.html', context)



 
# messages.debug,info, success, warning, error

@login_required
def index(request):

    query_results = Test.objects.all().order_by("-CreatedAt")[:10]
    query_result = Test.objects.all().order_by("-CreatedAt")[:1]
    context = {'query_results_json': serializers.serialize('json', query_results),
               "query_results": query_results,
               "query_result": query_result}
    return render(request, 'home/index.html', context)

@login_required
def maps(request):
    return render(request, 'home/maps.html')

@login_required
def reports(request):
    query_results = Test.objects.all().order_by("-CreatedAt")
    query_result = Test.objects.all().order_by("-CreatedAt")[:10]
    context = {'query_results_json': serializers.serialize('json', query_results), "query_result": query_result,
    'query_result_json': serializers.serialize('json', query_result) }
    return render(request, "home/reports.html", context)


@login_required
def sort(request):
    query_result = Test.objects.all().order_by("-CreatedAt")[:10]
    context = {"query_result": query_result}
    return render(request, "home/reports.html", context)

@login_required
def profile(request):
    query_result = Project.objects.all().order_by("-created")[:1]
   

    if request.method == "POST":
        U_form = UserUpdate(request.POST,instance=request.user)
        P_form = Profile(request.POST, request.FILES,instance=request.user.project)
        if U_form.is_valid and P_form.is_valid():
            U_form.save()
            P_form.save()
            
            messages.success(request, f'Account updated successfull!!')
            return redirect("EtBr-profile")
    else:
        P_form = Profile(instance=request.user.project)
        U_form = UserUpdate(instance=request.user)


        

    context = {'U_form': U_form, "P_form": P_form, "query_result": query_result}
    return render(request, 'home/profile.html', context)

@login_required
def help(request):
    return render(request, 'home/faq.html')

@login_required
def CSV(request):
    response=HttpResponse(content_type="test/csv")
    response["Content-Disposition"] = "attachment; filename=ORSS" + str(datetime.now())+".csv"
    writer=csv.writer(response)
    writer.writerow(["Date Time","Temperature","pHin","TDSin","pHout","TDSout","Motor ON Time",
         "Volume Sampled","No Of Hour Used","Operational Status","Cartridge Life Left"])

    ORSS = Test.objects.all()
      

    for orss in ORSS:
        writer.writerow([orss.CreatedAt,orss.Temperature,orss.pHin,orss.TDSin,orss.pHout,orss.TDSout,
                        orss.MotorONInSeconds,orss.VolumeSampled,orss.NoOfHourUsed,orss.OperationStatus,
                        orss.CartridgeLifeLeft])
    return response


def XLSX(request):
    
    response= HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = "attachment; filename=ORSS" + str(datetime.now())+".xls"
    wb = xlwt.Workbook(encoding = "utf-8")
    ws = wb.add_sheet('ORSS')
    row_num =0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["Date Time","Temperature","pHin","TDSin","pHout","TDSout","Motor ON Time",
         "Volume Sampled","No Of Hour Used","Operational Status","Cartridge Life Left"]
    
    for col_num in range(len(columns)):

        ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle() 
        rows = Test.objects.all().values_list("CreatedAt","Temperature","pHin","TDSin","pHout","TDSout",
        "MotorONInSeconds","VolumeSampled","NoOfHourUsed","OperationStatus","CartridgeLifeLeft")

    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response
         

# class PDF(LoginRequiredMixin, ListView):

#     template_name = 'calendar.html'
#     model = Test
#     paginate_by = 10

#     def get_queryset(self, **kwargs):
#         appointments = Test.objects.filter(date__gte = date.today()).order_by('date', 'time')
#         return appointments

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         appointments = Test.objects.filter(doctor = self.request.user)
#         appointment_data = []
#         for i in appointments:
#             appointment_details = {}
#             appointment_details["title"] = i.Test.MotorONInSeconds
#             appointment_details['start'] = i.Test.OperationalStatus + ' ' + i.Test.CartridgeLifeLeft
#             appointment_data.append(appointment_details)
#         context['appointments'] = appointment_data
#         context['page_title'] = _('View test')
#         return context
