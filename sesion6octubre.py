class Persona:
    def __init__(self, nombre, dni, edad):##Método constructur
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        
    def __str__(self): ## Método que imprime los atribiutos de la clase Persona
        cadena = 'Nombre: {0}\n'.format(self.nombre)
        cadena = cadena + 'Dni: {0}\n'.format(self.dni)
        cadena = cadena + 'Edad: {0}\n'.format(self.edad)
        return cadena


    def mayorEdad(self):##Método que imprime si la persona es mayor de edad
        if self.edad >= 18:
            return "es mayor de edad"
        else:
            return "no es mayor de edad"

    def iniciales(self):## Método que imprime las iniciales de la persona
        cadena = ""
        for caracter in self.nombre:
            if caracter >= 'A' and caracter <= 'Z':
                cadena = cadena + caracter + '. '
        return cadena   
