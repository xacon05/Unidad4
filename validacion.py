import json
from jsonschema import validate, ValidationError

# Definir el esquema JSON
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "nombre": {
            "type": "string",
            "minLength": 1
        },
        "edad": {
            "type": "integer",
            "minimum": 0
        },
        "hobbies": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["nombre", "edad"]  # Asegurarse de que estas propiedades estén presentes
}

# Archivo JSON de ejemplo para validar
archivo_json = '''
{
  "nombre": "Juan",
  "edad": 25,
  "hobbies": ["lectura", "ciclismo"]
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Intentar validar el archivo JSON contra el esquema
try:
    validate(instance=datos_json, schema=schema)
    print("El archivo JSON es válido.")
except ValidationError as e:
    print(f"El archivo JSON no es válido. Error: {e.message}")
