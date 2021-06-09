import io
import os
import pdfrw
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm,mm

def split(path, page, output):
    pdf_obj = pdfrw.PdfReader(path)
    
    writer = pdfrw.PdfWriter()
    writer.addpage(pdf_obj.pages[page-1])
    writer.write(output)

def transform(id,resp,pdf_name,name,parameters):
    space,space_q,max_h,w,h,start_id,start_q,error,x_name,y_name,y_name = parameters
    canvas_data = fill_ID(id,start_id,space,w,h,error)
    form = merge(canvas_data, template_path='./'+pdf_name+'.pdf')
    save(form, filename=pdf_name+'.pdf')
    canvas_data = fill_questions(resp.lower(),start_q,space_q,error,w,h)
    form = merge(canvas_data, template_path='./'+pdf_name+'.pdf')
    save(form, filename=pdf_name+'.pdf')
    canvas_data = fill_name(name,x_name,y_name,max_h)
    form = merge(canvas_data, template_path='./'+pdf_name+'.pdf')
    save(form, filename=pdf_name+'.pdf')

def fill_ID(id_str,start_id,space,w,h,error):
    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    for i,j in enumerate(id_str):
        pdf.rect(start_id[0]+(w+space)*i-error, -error+start_id[1]-(space+0.4*mm+h)*int(j), w+2*error, 2*error+h, stroke=1, fill=1)
    pdf.save()
    data.seek(0)
    return data

def fill_questions(q_str,start_q,space_q,error,w,h):
    keys = {'a':0,'b':1,'c':2,'d':3,'e':4}
    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    for i,j in enumerate(q_str):
        try:
            j = keys[j]
            if i>=9:
                pdf.rect(start_q[0]+space_q[0]+(w+0.3*mm+space_q[0])*j-error, -error+start_q[1]-(space_q[1]+0.4*mm+h)*i, w+2*error, 2*error+h, stroke=1, fill=1)
            else:
                pdf.rect(start_q[0]+(w+0.3*mm+space_q[0])*j-error, -error+start_q[1]-(space_q[1]+0.4*mm+h)*i, w+2*error, 2*error+h, stroke=1, fill=1)
        except KeyError:
            continue
    pdf.save()
    data.seek(0)
    return data

def fill_name(name,x_name,y_name,max_h) -> io.BytesIO:
    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    pdf.drawString(x=x_name, y=max_h-y_name, text=name)
    pdf.save()
    data.seek(0)
    return data

def merge(overlay_canvas: io.BytesIO, template_path: str) -> io.BytesIO:
    template_pdf = pdfrw.PdfReader(template_path)
    overlay_pdf = pdfrw.PdfReader(overlay_canvas)
    for page, data in zip(template_pdf.pages, overlay_pdf.pages):
        overlay = pdfrw.PageMerge().add(data)[0]
        pdfrw.PageMerge(page).add(overlay).render()
    form = io.BytesIO()
    pdfrw.PdfWriter().write(form, template_pdf)
    form.seek(0)
    return form

def save(form: io.BytesIO, filename: str):
    with open(filename, 'wb') as f:
        f.write(form.read())