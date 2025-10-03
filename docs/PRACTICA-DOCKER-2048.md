# Práctica Docker 2048 – Despliegue en AWS EC2 con CI/CD

## 1. URL del repositorio de GitHub
Repositorio: [https://github.com/smateo09/practica-docker-2048](https://github.com/smateo09/practica-docker-2048)

Este repositorio contiene:
- `Dockerfile`
- `docker-compose.yml`
- `.github/workflows/docker-publish.yml`
- `docs/PRACTICA-DOCKER-2048.md` (este documento técnico)

---

## 2. Diseño de la imagen (Dockerfile)
La imagen se diseñó con los siguientes criterios:
- **Imagen base:** Ubuntu `latest`.
- **Instalación de dependencias:** Nginx, Git, ca-certificates.
- **Código fuente:** Clonado desde [josejuansanchez/2048](https://github.com/josejuansanchez/2048) en `/var/www/html/`.
- **Puerto expuesto:** 80.
- **Proceso principal:** Nginx en primer plano (`CMD ["nginx", "-g", "daemon off;"]`).

---

## 3. Construcción y etiquetado de la imagen
Se construyó la imagen localmente:

```bash
docker build -t nginx-2048 .
docker images
