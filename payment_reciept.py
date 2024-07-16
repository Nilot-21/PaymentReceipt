from reportlab.platypus import SimpleDocTemplate,Table,paragraph,TableStyle,Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

data=[
    ["Date","Time","subscription","Price (Rs.)"],
    [
        "16/03/202", "Python and django", "Lifetime", "10,999.00/-", 
    ],
    [ "16/11/2020", "GCP", "6 months", "9,999.00/-"],
    ["subtotal","","","20,998.00/-"],
    ["Discount","","","-3000.00/-"],
    ["Total","","","17998.00/-"]
]

pdf=SimpleDocTemplate("receipt.pdf",pagesize=A4)
styles=getSampleStyleSheet()
title_style=styles["Heading1"]
title_style.alignment=1
title = Paragraph ( "Fee Receipt" , title_style )
style=TableStyle([ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
    ] )
table=Table(data,style=style)
pdf.build([title,table])