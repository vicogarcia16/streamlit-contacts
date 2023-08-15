# Usa la imagen oficial de Python
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY Pipfile Pipfile.lock ./

# Instala las dependencias con pipenv
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copia el resto de tus archivos al contenedor
COPY . .

# Comando por defecto para ejecutar la aplicación Streamlit
CMD ["pipenv", "run", "streamlit", "run", "app.py"]
