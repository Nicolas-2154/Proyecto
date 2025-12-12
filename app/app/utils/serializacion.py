import json
from openpyxl import Workbook
from reportlab.pdfgen import canvas

def exportar_json(nombre_archivo, datos):
    try:
        with open(nombre_archivo,"w",encoding="utf*8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        return True
    
    except Exception as e:
        print(f"[Error] No se pudo exportar JSON: {e}")
        return False
    
def importar_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8")as f:
            return json.load(f)
    except Exception as e:
        print(f"[Error] No se pudo leer JSON: {e}")


def exportar_excel(nombre_archivo,encabezados,datos):
    try:
        wb = Workbook()
        ws = wb.active

        if isinstance(encabezados, dict):
            ws.append(list(encabezados.values())) 
        else:
            ws.append(list(encabezados))

        for fila in datos:
            if isinstance(fila, dict):
                ws.append(list(fila.values())) 
            else:
                ws.append(list(fila)) 

        wb.save(nombre_archivo)
        return True

    except Exception as e:
        print(f"[Error] No se pudo exportar Excel: {e}")


def exportar_pdf(nombre_archivo,titulo,encabezados,datos):
    try:
        c = canvas.Canvas(nombre_archivo)

        c.setFont("Helvetica-Bold",14)
        c.drawString(50,800,titulo)

        y=770
        c.setFont("Helvetica-Bold",10)
        encabezado_texto = " | ".join(encabezados)
        c.drawString(50, y, encabezado_texto)

        y -=30
        c.setFont("Helvetica", 10)
        for fila in datos:
            linea = " | ".join(str(x) for x in fila)
            c.drawString(50, y, linea)
            y -= 20 

            if y < 50:
                c.showPage()
                y = 800

        c.save()
        return True
    except Exception as e:
        print(f"[Error] No se pudo exportar PDF: {e}")
        return False


