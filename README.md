## Proyecto para la Hackaton de Infojobs ###

Este proyecto se ha hecho con mucha ilusión para participar en la hackaton de infojobs, promocionada por [@midu](https://github.com/midudev).

La aplicación intenta resumir las ofertas de trabajo obtenidas con la API de Infojobs y juntar toda la información en no más de 100 palabras. 
Además, existe la opción de TTS del resumen realizado previamente.

El objetivo era practicar un poco con la API de [OpenAI](https://platform.openai.com/docs/api-reference) (ChatGPT) y la API de [ElevenLabs](https://beta.elevenlabs.io). 
El backend se ha hecho con FastAPI y el frontend con React (copiando un poco los estilos de Midu, ya que no es mi campo).

![](https://github.com/Rafitis/infojobs-hackaton/blob/main/infojobs-hackaton.jpg)

Para hacerlo funcionar es necesario tener cuenta en OpenAI y ElevenLabs (para la parte de TTS). Se debe añadir un fichero .env con las API-KEYS de cada plataforma.
