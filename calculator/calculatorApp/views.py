from django.shortcuts import render

def home(request):
    return render(request,"HomeScreen.html")

def calculator(request):
    return render(request,"Calculator.html")
    
def minesweeper(request):
    return render(request,"Minesweeper.html")