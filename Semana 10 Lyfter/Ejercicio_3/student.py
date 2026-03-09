class Student:
    def __init__(self, name, section, spanish, english, socials, science):
        self.name = name
        self.section = section
        # Convertimos a float para asegurar que las operaciones matemáticas funcionen
        self.spanish = float(spanish)
        self.english = float(english)
        self.socials = float(socials)
        self.science = float(science)

    def get_average(self):
        """Calcula el promedio de las 4 materias del objeto actual."""
        total = self.spanish + self.english + self.socials + self.science
        return total / 4

    def to_dict(self):
        """Convierte los atributos del objeto a un diccionario para el CSV."""
        return {
            'name': self.name,
            'section': self.section,
            'spanish': self.spanish,
            'english': self.english,
            'socials': self.socials,
            'science': self.science
        }