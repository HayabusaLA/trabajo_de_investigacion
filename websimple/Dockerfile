# Usa la imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación (incluyendo app.py y el HTML)
COPY . /app

# Instala Flask
RUN pip install Flask

# Expone el puerto 8000 para Flask
EXPOSE 8000

# Comando para ejecutar la aplicación de Flask
CMD ["python", "app.py"]
