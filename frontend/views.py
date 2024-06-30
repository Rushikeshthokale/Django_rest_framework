from django.shortcuts import render,HttpResponse,redirect
import requests
import json
# Create your views here.
def showEmp(request):
    # 1.fetch the data from rest api
    # 2.received data is in json so convert it in dictionary
    # 3.Send the data to template
    resp=requests.get("http://localhost:8000/employees")
    #print ("GET response code:",resp.status_code)
    #resp.content has binary received from api
    data=json.loads(resp.content)
    context={}
    context['employees']=data
    return render(request,'emplist.html',context)

def addemp(request):
    if request.method=="GET":
        return render(request,'addemp.html')
    else:
        #form data fetchinig
        n=request.POST['name']
        d=request.POST['dept']
        s=request.POST['salary']
        #create dict
        data={}
        data['name']=n
        data['dept']=d
        data['salary']=s
        print(data)
        #converting data to json
        data_json=json.dumps(data)
        #sending post request to api
        resp=requests.post("http://localhost:8000/employees",data_json)
        print(resp.status_code)
        return redirect('/fe/list')

def delete(request,empid):
    #url --> http://localhost:8000/employees/__
    resp=requests.delete('http://localhost:8000/employees/'+ empid)
    return redirect('/fe/list')

def update(request,empid):
    if request.method=="GET":
    #send api request "GET" http://localhost:8000/employees/3 to fetch the employee details
        resp=requests.get("http://localhost:8000/employees/"+empid)
        data=json.loads(resp.content)
        context={}
        context['emp']=data
        return render(request,'updateemp.html',context)
    else:
        
        #1.get the form data
        n=request.POST["name"]
        d=request.POST["dept"]
        s=request.POST['salary']
        #2.Dict of emp object
        data={}
        data['name']=n
        data['dept']=d
        data['salary']=s
        data['id']=empid
        #3.Convert the dict to json
        data_json=json.dumps(data)

        #4.Send PUT request to api
        resp=requests.put("http://localhost:8000/employees/"+empid,data_json)
        #resp.content / resp.status_code
        return redirect('/fe/list')