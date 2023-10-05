from django.shortcuts import render

# Create your views here.
def MiPrimerFuncion(request):
    datos = {
        'nombre':'Pablo'
    }
    return render(request,'mi_primer_pagina.html',datos)