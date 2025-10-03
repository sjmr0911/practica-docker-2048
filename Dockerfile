# Imagen base: última versión estable de Ubuntu
FROM ubuntu:latest

# Evitar prompts interactivos de apt
ENV DEBIAN_FRONTEND=noninteractive

# Actualiza índice, instala Nginx y Git (y utilidades mínimas)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        nginx git ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Limpia contenido por defecto y clona la web estática 2048 en /var/www/html
RUN rm -rf /var/www/html/* && \
    git clone --depth=1 https://github.com/josejuansanchez/2048 /var/www/html

# Nginx escucha en 80
EXPOSE 80

# Ejecutar Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
