from django.shortcuts import render

# Create your views here.

class Member:
    
    def __init__(self, id, name, join_at, picture_path):
        self.id = id
        self.name = name
        self.join_at = join_at
        self.picture_path = picture_path

member_list = [
    Member(0, "Bob", "2021/2/1", "img/Bob.jpg"),
    Member(1, "Eric", "2020/2/4", "img/eric.jpg"),
    Member(2, "Alex", "2022/1/5", "img/alex.jpg"),
    Member(3, "Elton", "2021/12/10", "img/elton.jpg")
]

def home(request):
    return render(request, "home.html")

def members(request):
    return render(request, "members.html", context={
        "members": member_list
    })

def member(request, id):
    return render(request, "member_detail.html", context={
        "member": member_list[id]
    })