# AI Search with Elasticsearch

Este proyecto proporciona una API que permite realizar búsquedas inteligentes en Elasticsearch utilizando un modelo de lenguaje de aprendizaje automático para reformular preguntas antes de ejecutarlas en Elasticsearch. La API está construida usando FastAPI, y se integra con Elasticsearch y un modelo de lenguaje basado en la librería `transformers`.

## Funcionalidades

- **Reformulación de preguntas**: Antes de realizar la búsqueda en Elasticsearch, la pregunta proporcionada por el usuario es reformulada utilizando un modelo de lenguaje.
- **Búsqueda en Elasticsearch**: La pregunta reformulada se utiliza para realizar una búsqueda en un índice de Elasticsearch.
- **Resultados personalizados**: Los resultados devueltos por Elasticsearch se presentan junto con la pregunta original y la reformulada.

## Tecnologías

- **FastAPI**: Framework moderno para construir APIs rápidas con Python.
- **Elasticsearch**: Motor de búsqueda y análisis en tiempo real.
- **Transformers**: Librería de Hugging Face para usar modelos preentrenados en tareas de NLP (Natural Language Processing).
- **LangChain**: Librería que facilita la interacción con modelos de lenguaje.

## Requisitos

1. **Python 3.8+**
2. **FastAPI**: Para ejecutar la API.
3. **Elasticsearch**: Debe estar ejecutándose localmente o en un servidor accesible.
4. **Transformers y Hugging Face**: Para cargar y usar modelos preentrenados.

## Instalación

### 1. Clonar el repositorio:

```bash
git clone https://github.com/tuusuario/ai-search-elasticsearch.git
cd ai-search-elasticsearch
```

### 2. Crear un entorno virtual e instalar las dependencias:

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
pip install -r requirements.txt
```

### 3. Configurar los archivos de entorno (`.env`):

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de configuración:

```env
LLM_MODEL_PATH=EleutherAI/gpt-neo-1.3B  # Ruta del modelo de Hugging Face
ELASTICSEARCH_URL=http://localhost:9200  # URL de Elasticsearch
```

### 4. Iniciar Elasticsearch:

Si no tienes Elasticsearch instalado, puedes ejecutarlo usando Docker:

```bash
docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 docker.elastic.co/elasticsearch/elasticsearch:8.10.2
```

### 5. Ejecutar la aplicación:

```bash
uvicorn main:app --reload
```

La API estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Endpoints

### `/api/v1/ai-search/`

#### Descripción

Permite realizar una búsqueda inteligente en Elasticsearch. La pregunta proporcionada por el usuario se reformula antes de ejecutarse en Elasticsearch.

#### Parámetros de la solicitud (body):

- **question**: La pregunta que se quiere hacer (tipo `str`).
- **size**: El número de resultados que se desean (opcional, por defecto es 10).

#### Ejemplo de solicitud:

```json
{
  "question": "¿Cómo estás?",
  "size": 5
}
```

#### Ejemplo de respuesta:

```json
{
  "original_question": "¿Cómo estás?",
  "reformulated_query": "¿Cómo me siento?",
  "results": [
    {
      "_id": "1",
      "_score": 1.0,
      "_source": {
        "content": "¿Cuál es tu nombre?"
      }
    },
    {
      "_id": "2",
      "_score": 1.0,
      "_source": {
        "content": "¿De dónde eres?"
      }
    }
    // Otros resultados...
  ]
}
```

## Estructura del Proyecto

```plaintext
.
├── app
│   ├── config.py            # Configuración del proyecto
│   ├── models
│   │   └── search.py        # Modelo para la consulta de búsqueda
│   ├── routes
│   │   └── search.py        # Rutas de la API
│   ├── services
│   │   ├── ai.py            # Función para reformular la consulta
│   │   └── elastic.py       # Funciones para interactuar con Elasticsearch
│   ├── main.py              # Punto de entrada de la API
├── requirements.txt         # Dependencias del proyecto
├── .env                     # Variables de configuración del entorno
└── README.md                # Este archivo
```

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el proyecto, por favor abre un issue o crea un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
