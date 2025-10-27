ingreso_mensual = 80000
gasto_mensual = 99000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 3000:
     print("estas bien en cualquier parte del mundo")
    elif ingreso_mensual - gasto_mensual < 0:
        print('estas en deficit pa')
    else: 
     print('estas gastando una banda pa')

elif ingreso_mensual > 1000:
    print("estas bien en latam")

elif ingreso_mensual > 500:
    print("estas bien en argentina")

elif ingreso_mensual > 200:
    print("estas bien en venezuela")

else:
    print("sos pobre")