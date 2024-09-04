# Usar una imagen base de Python 3
FROM python:3.11-slim

# Instalar utilidades adicionales que puedas necesitar
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crear y establecer el directorio de trabajo
WORKDIR /workspace

# Instalar las dependencias desde requirements.txt (si existe)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements found"
RUN pip install --upgrade pip

# Copiar el código fuente
COPY . .

# Comando para ejecutar la aplicación al iniciar el contenedor
CMD ["python", "main.py"]
