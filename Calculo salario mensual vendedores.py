"""
Realice un programa que lea el nombre de un vendedor y su tipo, 
y el monto que vendió por cada tipo de producto. 
Al final deberá mostrar el nombre del vendedor y 
el monto total a pagar por salario base, salario de comisiones y salario bruto (base + comisiones)
"""


print("Calculo salario mensual vendedores")

nombre=input("Nombre del vendedor: ")
tipo= input("Tipo de vendedor: (J) Junior, (S) Senior: ")
ventaPktes=float(input("Ventas realizadas en paquetes: "))
ventaSfwMed=float(input("Ventas realizadas por software a la medida: "))
ventaAsesoria=float(input("Ventas realizadas en Servicios: "))

if tipo=="J" or tipo=="j":
    base = 750
else:
    base = 500

comisiones = ventaPktes * 0.03 + ventaSfwMed * 0.05 + ventaAsesoria * 0.75

salarioBruto = base + comisiones

print("Vendedor= " , nombre)
print("Salario base = ", base )
print("Comisiones = " , comisiones)
print("Salario bruto = " , salarioBruto)

