#Módulo de programación, taller 1
#Script funciones.py para la realización de la parte 1 actividad 10 

print("¡Bienvenida programadora!")
print("\t*******Alianzas entre mujeres*******")
print("\t1. Alianzas entre mujeres")
print("\t2. Sororidad")
print("\t3. Derechos humanos de las mujeres")
print("\t4. Igualdad de género")
print("\t*************************************")
opcion = int(input("Elige una opción del menú y conoce más sobre los terminos: "))


while True:
	if(opcion == 1):
		print("\nLas alianzas entre mujeres se forman a través de la sororidad con el fin de buscar una solución\n a los problemas de genero que acontecen en su vida diaria.")
		respuesta = input("¿Quieres conocer más?")
		respuesta = respuesta.lower()
		if(respuesta == "si"):
			print("\n\t*******Alianzas entre mujeres*******")
			print("\t1. Alianzas entre mujeres")
			print("\t2. Sororidad")
			print("\t3. Derechos humanos de las mujeres")
			print("\t4. Igualdad de género")
			print("\t*************************************")
			opcion = int(input("Elige una opción del menú y conoce más sobre los terminos"))
		else:
			print("Hasta luego")
			break
			
	elif(opcion == 2):
		print("\nLa palabra “sororidad” significa hermandad entre mujeres y sirve para que ellas se identifiquen\n y formen aliarse para el logro de un fin común en su beneficio, sin necesidad de tener un pensamiento uniforme en todos los aspectos de su vida.")
		respuesta = input("¿Quieres conocer más?")
		respuesta = respuesta.lower()
		if(respuesta == "si"):
			print("\n\t*******Alianzas entre mujeres*******")
			print("\t1. Alianzas entre mujeres")
			print("\t2. Sororidad")
			print("\t3. Derechos humanos de las mujeres")
			print("\t4. Igualdad de género")
			print("\t*************************************")
			opcion = int(input("Elige una opción del menú y conoce más sobre los terminos"))
		else:
			print("Hasta luego")
			break
			
	elif(opcion == 3):
		print("\nLos derechos humanos de las mujeres SON DERECHOS HUMANOS. Las mujeres y las niñas tienen derecho al disfrute\n pleno y en condiciones de igualdad de todos sus derechos humanos y a vivir libres de todas las formas de discriminación")
		respuesta = input("¿Quieres conocer más?")
		respuesta = respuesta.lower()
		if(respuesta == "si"):
			print("\n\t*******Alianzas entre mujeres*******")
			print("\t1. Alianzas entre mujeres")
			print("\t2. Sororidad")
			print("\t3. Derechos humanos de las mujeres")
			print("\t4. Igualdad de género")
			print("\t*************************************")
			opcion = int(input("Elige una opción del menú y conoce más sobre los terminos"))
		else:
			print("Hasta luego")
			break
			
	elif(opcion == 4):
		print("\nLa igualdad de género hace referencia al reconocimiento por igual ante las leyes de los derechos\n humanos sin importar el genero de las personas.")
		respuesta = input("¿Quieres conocer más?")
		respuesta = respuesta.lower()
		if(respuesta == "si"):
			print("\n\t*******Alianzas entre mujeres*******")
			print("\t1. Alianzas entre mujeres")
			print("\t2. Sororidad")
			print("\t3. Derechos humanos de las mujeres")
			print("\t4. Igualdad de género")
			print("\t*************************************")
			opcion = int(input("Elige una opción del menú y conoce más sobre los terminos"))
		else:
			print("Hasta luego")
			break
			
	else:
		print("\nOpción inválida, intenta de nuevo")
		print("\n\t*******Alianzas entre mujeres*******")
		print("\t1. Alianzas entre mujeres")
		print("\t2. Sororidad")
		print("\t3. Derechos humanos")
		print("\t4. ")
		print("\t*************************************")
		opcion = int(input("Elige una opción del menú y conoce más sobre los terminos"))

