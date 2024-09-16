# Usa la imagen oficial de Node.js
FROM node:16-alpine

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo package.json e instala las dependencias
COPY package*.json ./
RUN npm install

# Copia el código de la aplicación
COPY . .

# Compila el código TypeScript a JavaScript
RUN npm run build

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["npm", "run", "start"]


