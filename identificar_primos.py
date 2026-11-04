import streamlit as st


def es_primo(numero: int) -> bool:
    """Indica si un entero es primo mediante divisiones hasta su raíz cuadrada."""
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


st.set_page_config(page_title="Identificador de números primos", page_icon="🔢")

st.title("🔢 Identificador de números primos")
st.write(
    "Escribe un número entero y descubre si es primo. Un número primo es un "
    "entero mayor que 1 que solo es divisible entre 1 y sí mismo."
)

with st.form("formulario_primo"):
    entrada = st.text_input("Número entero", placeholder="Por ejemplo: 17")
    enviado = st.form_submit_button("Comprobar", type="primary")

if enviado:
    try:
        numero = int(entrada.strip())
    except ValueError:
        st.error("Entrada no válida. Escribe un número entero, como 17 o -4.")
    else:
        if es_primo(numero):
            st.success(f"{numero} es un número primo. ✅")
        else:
            st.info(f"{numero} no es un número primo.")
