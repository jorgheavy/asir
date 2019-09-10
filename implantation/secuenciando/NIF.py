import sys

dni = int(input("Introduzca su DNI: "))
secuenciaLetrasNIF = "TRWAGMYFPDXBNJZSQVHLCKE"

letra = dni % 23
codigoControl = secuenciaLetrasNIF[letra]
print("Su NIF es: " + (f"{dni}{codigoControl}"))
