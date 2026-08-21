import streamlit as st
st.title("Bootcamp Data Analytics for Oil & Gas M1")
st.sidebar.title("Parameters")

modulos = st.sidebar.selectbox("Seleccione un modulo", ["Introduccion a variables", "Funciones"])

if modulos == "Introduccion a variables":

  pozo = "SPE-001"
  petroleo_bpd = 1250
  agua_bpd = 350.50
  status = True
  liquido_total_bpd = petroleo_bpd + agua_bpd
  corte_agua_pct = agua_bpd / liquido_total_bpd * 100
  
  st.write(pozo)
  st.write(petroleo_bpd)
  st.write(agua_bpd)
  st.write(status)
  st.write(liquido_total_bpd)
  st.write(corte_agua_pct)

elif modulos == "Funciones":
  def calcular_caudal_vogel(caudal_max=1200,presion_yacimiento=3000,presion_fondo=200,decimales=2):
    """
      Calculo de caudal de petroleo con Vogel
  
      Parámetros:
       
      caudal_max = Caudal maximo teorico del pozo, BPD
      presion_yacimiento = Presion promedio del pozo, PSI
      presion_fondo = Presion del fondo del pozo, PSI
      decimales = Cantidad de decimales que se quieren en el resultado
  
    """
  
    relacion_presion = presion_fondo/presion_yacimiento
    caudal = caudal_max*(1 - 0.2*relacion_presion - 0.8*(relacion_presion**2))
    return round(caudal, decimales)
  
  caudal_maximo = st.number_input("Ingrese el caudal maximo")
  presion_yacimiento = st.number_input("Ingrese la presion de yacimiento")
  presion_fondo = st.number_input("Ingrese la presion de fondo fluyente")
  decimales = st.slider("Seleccione la cantidad de decimales para su resultado")

