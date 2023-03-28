num_boletas = int(input('cuantas entradas desea adquirir?: '))
tipo_sala = '3D'
hora = 'tarde'
medio_pago = 'tarjeta'
reserva = False


def calcular_precio_boletas(num_boletas, tipo_sala, hora, medio_pago, reserva):
    tarifa = 0
    
    if tipo_sala == 'Dinamix':
        tarifa = 18800
    elif tipo_sala == '3D':
        tarifa = 15500
    elif tipo_sala == '2D':
        tarifa = 11300
        
    if hora in ['mañana', 'tarde'] or hora == 'noche' and tipo_sala != 'Dinamix':
        tarifa *= 0.9
        
        if num_boletas >= 3:
            descuento_adicional = 500 * num_boletas
            tarifa -= descuento_adicional
            
    if medio_pago == 'tarjeta':
        descuento_tarjeta = tarifa * 0.05
        tarifa -= descuento_tarjeta
        
    if reserva:
        recargo_reserva = 2000 * num_boletas
        tarifa += recargo_reserva
        
    if hora == 'pico':
        if tipo_sala == '2D' or tipo_sala == '3D':
            tarifa *= 1.25
        elif tipo_sala == 'Dinamix':
            tarifa *= 1.5
            
    precio_total = tarifa * num_boletas
    
    return precio_total

precio_total = calcular_precio_boletas(num_boletas, tipo_sala, hora, medio_pago, reserva)

print(f'El precio total de las {num_boletas} boletas es de {precio_total} pesos.')
