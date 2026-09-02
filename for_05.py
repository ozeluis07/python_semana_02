def evaluacion_de_revision ():

    # CASO EMPRESARIAL 05: Evaluación del servicio
    suma_calificaciones = 0
    valoraciones_altas = 0

    print("=== EVALUACIÓN DEL SERVICIO (10 CALIFICACIONES) ===")
    for i in range(1, 11):
        calificacion = float(input(f"Calificación {i} (1 al 5): "))
        
        # Validar que esté entre 1 y 5 por si acaso
        while calificacion < 1 or calificacion > 5:
            print("❌ Opción inválida. Debe ser entre 1 y 5.")
            calificacion = float(input(f"Calificación {i} (1 al 5): "))
            
        suma_calificaciones += calificacion
        
        if calificacion >= 4:
            valoraciones_altas += 1

    promedio = suma_calificaciones / 10

    print("\n--- RESUMEN DE EVALUACIONES ---")
    print(f"Promedio general del servicio: {promedio:.2f}")
    print(f"Cantidad de valoraciones altas (4 o 5): {valoraciones_altas}")

if __name__ == "__main__":
    evaluacion_de_revision()