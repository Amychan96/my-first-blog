from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.shortcuts import render

# views.py


def home(request):
    # Asegúrate de tener un archivo pagina.html en tu carpeta de plantillas
    return render(request, 'pagina.html')


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mi_pdf.pdf"'

    # Crear el PDF y enviar la respuesta
    pisa.CreatePDF(html, dest=response)

    return response


def generate_pdf(request):
    # Puedes pasar un contexto al PDF si lo necesitas
    context = {
        'variable': 'Este es un texto dinámico',
    }
    return render_to_pdf('blog/pagina.html', context)


# def generate_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, "Hello, this is a PDF document.")
    p.drawString(100, 700, "This is the second line.")
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="document.pdf"'
    return response
