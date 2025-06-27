from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    all_person = Person.objects.all() # แก้ไข: เพิ่มวงเล็บ () เพื่อเรียกใช้เมธอด
    return render(request, "index.html", {"all_person": all_person})
 
def about(request):
    return render(request, "about.html") 

def form(request):
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST["name"]   
        age = int(request.POST["age"]) # แก้ไข: แปลงค่า age เป็นจำนวนเต็ม
        #บันทึกข้อมูล
        person = Person.objects.create(name=name, age=age)
        person.save()
        messages.success(request, "บันทึกข้อมูลเรียบร้อย")
         # เพิ่ม: สร้างและบันทึกอ็อบเจกต์ Person ลงฐานข้อมูล
        return redirect("/") # แก้ไข: ย้ายมาอยู่ภายในบล็อก if เพื่อ redirect หลังจากบันทึกข้อมูลสำเร็จ
    else:    
        return render(request, "form.html") 
    
def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "อัพเดทข้อมูลเรียบร้อย")
        return redirect('/')
    else:     
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person": person})
    
def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อย")
    return redirect('/')