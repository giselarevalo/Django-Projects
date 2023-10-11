from django.shortcuts import render
from Blog.models import Posteo,Comentario
from Blog.forms import FormComentario

def blog_index(request):
    posteos = Posteo.objects.all().order_by('-created_on')

    context = {
        'posteos': posteos,
    }
    return render(request,'index.html',context)

def blog_detail(request,pk):

    posteo = Posteo.objects.get(pk=pk)

    formulario = FormComentario()
    if request.method == 'POST':
        formulario = FormComentario(request.POST)
        if formulario.is_valid():
            comentario = Comentario(
                autor = formulario.cleaned_data['autor'],
                body = formulario.cleaned_data['body'],
                posteo = posteo
            )
            comentario.save()
            formulario = FormComentario()
    comentarios = Comentario.objects.filter(posteo=posteo)

    context = {
        'posteo': posteo,
        'comentarios': comentarios,
        'formulario': formulario
    }

    return render(request,'detail.html',context)

