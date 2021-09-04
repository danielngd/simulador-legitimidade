from django.shortcuts import render
from .models import (Estado, Produto, Imposto)
import json


def dashboard(request):
    estados = Estado.objects.all()
    cliente = request.GET.get('cliente', "")
    estado = request.GET.get('estado')
    if estado:
        estado = int(estado)
    produtos = Produto.objects.all()

    produtos_selecionados = request.GET.getlist('ps[]')
    produtos_selecionados = [int(v) for v in produtos_selecionados]

    produtos_obj_selecionados = [Produto.objects.get(pk=v) for v in produtos_selecionados]

    calculadora = None
    impostos = None
    if estado:
        impostos = Imposto.objects.filter(estado=estado)

    if impostos:
        total = sum([p.cpv for p in produtos_obj_selecionados])
        total_impostos = sum([total * i.valor for i in impostos])
        calculadora = {
            "total": total,
            "total_impostos": total + total_impostos
        }

    return render(request, "orcamento/dashboard.html", {
        'estados': estados,
        'cliente': cliente,
        'estado_selecionado': estado,
        'produtos': produtos,
        'produtos_selecionados': produtos_selecionados,
        'produtos_obj_selecionados': produtos_obj_selecionados,
        'impostos': impostos,
        "calculadora": calculadora,
    })