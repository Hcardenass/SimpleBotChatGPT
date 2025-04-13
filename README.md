# SimpleBotChatGPT

SimpleBot es un chatbot inteligente que utiliza la tecnología ChatGPT-4 de OpenAI para interactuar de forma natural y personalizada. Diseñado para ofrecer productos y servicios siguiendo reglas específicas de interacción, este bot garantiza un trato amable y proporciona información útil basada en características cabe destacar que la arquitectura implementada es básica y sirve como punto de partida para futuras mejoras y adaptaciones.

# Descripción
Este proyecto presenta una arquitectura fundamental para desarrollar un chatbot personalizado con capacidades avanzadas de interpretación y generación de texto. A través de un conjunto de directrices predefinidas, SimpleBot responde a las consultas, orienta sobre productos y servicios, y mantiene diálogos dinámicos que simulan escenarios reales. Implementado en Python y apoyado en la API de OpenAI, el bot es capaz de gestionar conversaciones complejas, interpretar los requerimientos del usuario y cumplir con políticas de servicio, como la gestión de cobro de delivery y la atención respetuosa en todo momento.


# Requisitos Previos
Antes de comenzar, asegúrate de contar con:

Python 3.8 o superior.

Acceso a la API de OpenAI (necesitarás disponer de una clave API de OpenAI).


# Instalación y Configuración

1. Clonar el Repositorio:

```git clone https://github.com/Hcardenass/SimpleBotChatGPT.git```
```cd SimpleBotChatGPT```

2. Configurar la API:

Edita el archivo api_key.txt e introduce tu clave API de OpenAI.

Ejemplo:

```with open("api_key.txt") as archivo:```
    ```openai.api_key = archivo.readline().strip()```

3. Uso vía Consola:

  ``` python main_str.py```
   
   Sigue las instrucciones en la terminal para interactuar con SimpleBot.

5. Uso con Streamlit

```streamlit run main_str.py```

Este comando abrirá una interfaz gráfica en tu navegador para interactuar con el bot.
