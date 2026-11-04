# Identificador de números primos

Aplicación web en Python y Streamlit para comprobar si un número entero es primo.

## Ejecutar en local

Se recomienda usar Python 3.9 o posterior.

```bash
python -m venv .venv
```

Activa el entorno virtual y luego instala las dependencias e inicia la aplicación:

```bash
pip install -r requirements.txt
streamlit run identificar_primos.py
```

En Windows, activa el entorno con `.venv\Scripts\activate`; en macOS o Linux, con `source .venv/bin/activate`.

## Publicar con GitHub y Streamlit Community Cloud

1. Sube `identificar_primos.py`, `requirements.txt` y este `README.md` a un repositorio de GitHub.
2. Inicia sesión en [Streamlit Community Cloud](https://share.streamlit.io/) con GitHub y autoriza el acceso al repositorio.
3. Crea una aplicación nueva, selecciona el repositorio y la rama, y establece `identificar_primos.py` como archivo principal.
4. Pulsa **Deploy**. Streamlit Cloud instalará las dependencias declaradas en `requirements.txt`.

Cada actualización que subas a la rama seleccionada se podrá publicar desde la misma aplicación.
