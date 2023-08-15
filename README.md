### streamlit-contacts

Aplicación de Contactos

 #### Ejecución de código ⚙️

1. Realizar un entorno virtual. En este caso se hace uso de pipenv.
    - <code>pipenv shell</code>
2. Instalar las librerias necesarias.
    - <code>pipenv install --ignore-pipfile</code>
3. Realizar archivo .env con lo siguiente:
    * USER='tu_user'
    * PASSWORD='tu_pass'
    * HOST='tu_host' --- *Si utilizas Docker, poner el host como nombraste el servicio de BD en docker-compose.yaml*
    * PORT='tu_puerto'
    * DATABASE='tu_base_datos'
5. Ejecutar el archivo python.
    - <code>pipenv run contacts</code>

#### Construido con 🛠️

* [Python](https://www.python.org/) - Lenguaje de programación
* [Streamlit](https://docs.streamlit.io/) - Libreria Streamlit

#### Autor ✒️

* **Víctor García** [vicogarcia16](https://github.com/vicogarcia16)
