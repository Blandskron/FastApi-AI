from elasticsearch import Elasticsearch, ConnectionError
from app.config import settings

# Conectar a Elasticsearch
es = Elasticsearch(settings.ELASTICSEARCH_URL)

def index_data():
    # Verificar si Elasticsearch está accesible
    if not es.ping():
        raise Exception("No se puede conectar a Elasticsearch")
    
        # Ejemplo de datos que quieres insertar en Elasticsearch
    documents = [
        {"content": "¿Cuál es tu nombre?"},
        {"content": "¿De dónde eres?"},
        {"content": "¿Qué haces?"},
        {"content": "¿Cuál es tu color favorito?"},
        {"content": "¿Qué te gusta hacer en tu tiempo libre?"},
        {"content": "¿Qué tipo de música prefieres?"},
        {"content": "¿Tienes alguna mascota?"},
        {"content": "¿Qué deportes practicas?"},
        {"content": "¿Cuáles son tus hobbies?"},
        {"content": "¿Te gusta viajar?"},
        {"content": "¿Cuál es tu película favorita?"},
        {"content": "¿Cuál es tu serie de televisión favorita?"},
        {"content": "¿Qué tipo de comida prefieres?"},
        {"content": "¿Tienes alguna alergia?"},
        {"content": "¿Cuál es tu lugar favorito para vacacionar?"},
        {"content": "¿Te gusta leer?"},
        {"content": "¿Cuál es tu libro favorito?"},
        {"content": "¿Qué idiomas hablas?"},
        {"content": "¿Cuál es tu trabajo ideal?"},
        {"content": "¿Cómo te describirías en tres palabras?"},
        {"content": "¿Qué cualidades valoras en una amistad?"},
        {"content": "¿Te consideras una persona extrovertida o introvertida?"},
        {"content": "¿Cuál es tu estación del año favorita?"},
        {"content": "¿Te gustan los videojuegos?"},
        {"content": "¿Cuál es tu videojuego favorito?"},
        {"content": "¿Qué te gustaría aprender en el futuro?"},
        {"content": "¿Tienes alguna meta a largo plazo?"},
        {"content": "¿Cuál es tu mayor logro hasta ahora?"},
        {"content": "¿Cuál es tu mayor miedo?"},
        {"content": "¿Qué opinas de las redes sociales?"},
        {"content": "¿Prefieres trabajar en equipo o solo?"},
        {"content": "¿Qué piensas sobre el cambio climático?"},
        {"content": "¿Tienes algún talento oculto?"},
        {"content": "¿Te gusta cocinar?"},
        {"content": "¿Qué te inspira a ser mejor cada día?"},
        {"content": "¿Tienes alguna tradición familiar?"},
        {"content": "¿Cómo te gustaría que fuera tu futuro?"},
        {"content": "¿Qué opinas de la inteligencia artificial?"},
        {"content": "¿Cuál es tu concepto de éxito?"},
        {"content": "¿Qué valores son más importantes para ti?"},
        {"content": "¿Qué harías si fueras invisible por un día?"},
        {"content": "¿Cuál es el mejor consejo que has recibido?"},
        {"content": "¿Qué harías si fueras presidente de tu país?"},
        {"content": "¿Te consideras una persona optimista o pesimista?"},
        {"content": "¿Qué significa la amistad para ti?"},
        {"content": "¿Cuál es el mejor regalo que has recibido?"},
        {"content": "¿Qué opinas sobre el arte moderno?"},
        {"content": "¿Prefieres las ciudades o el campo?"},
        {"content": "¿Te gustaría ser famoso?"},
        {"content": "¿Qué harías con un millón de dólares?"},
        {"content": "¿Cuál es el peor error que has cometido?"},
        {"content": "¿Te gustaría vivir en otro país?"},
        {"content": "¿Qué opinas sobre el futuro de la educación?"},
        {"content": "¿Qué opinas sobre la energía renovable?"},
        {"content": "¿Tienes alguna superstición?"},
        {"content": "¿Te gustaría aprender a tocar un instrumento musical?"},
        {"content": "¿Cuál es tu deporte favorito para ver?"},
        {"content": "¿Te gustaría hacer una carrera en el arte o la música?"},
        {"content": "¿Qué harías si pudieras cambiar el mundo?"},
        {"content": "¿Qué harías si pudieras hablar con los animales?"},
        {"content": "¿Cómo imaginas la vida en el año 2050?"},
        {"content": "¿Cuál es tu mayor sueño?"},
        {"content": "¿Te gustaría ser científico?"},
        {"content": "¿Cuál es tu mayor fuente de estrés?"},
        {"content": "¿Cómo te relajas después de un día estresante?"},
        {"content": "¿Te consideras una persona optimista?"},
        {"content": "¿Cuál es tu día favorito de la semana?"},
        {"content": "¿Qué es lo que más te molesta de las personas?"},
        {"content": "¿Qué opinas de la política actual?"},
        {"content": "¿Te gustaría tener tu propio negocio?"},
        {"content": "¿Cómo te gustaría que te recuerden?"},
        {"content": "¿Qué opinas sobre la igualdad de género?"},
        {"content": "¿Te gustaría cambiar algo en el sistema educativo?"},
        {"content": "¿Tienes algún miedo irracional?"},
        {"content": "¿Cuál es el objeto más importante para ti?"},
        {"content": "¿Te gustaría vivir en una ciudad futurista?"},
        {"content": "¿Qué piensas sobre la tecnología actual?"},
        {"content": "¿Te gustaría ser inventor?"},
        {"content": "¿Qué harías si fueras invisible por un día?"}
    ]

    
    # Verificar si el índice existe, y si no, crearlo
    if not es.indices.exists(index="your-index"):
        es.indices.create(index="your-index")
        print("Índice 'your-index' creado.")
    
    # Insertar documentos en Elasticsearch
    for i, doc in enumerate(documents, 1):
        try:
            response = es.index(index="your-index", id=i, document=doc)
            print(f"Documento {i} insertado: {response['_id']}")
        except ConnectionError:
            raise Exception("Failed to connect to Elasticsearch")
        except Exception as e:
            print(f"Error al insertar documento {i}: {e}")

if __name__ == "__main__":
    index_data()
