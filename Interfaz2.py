import streamlit as st

#Informacion general sobre Eyringpy
st.image("logoe.jpg")
st.write("## *What is `Eyringpy`?*")
st.write("`Eyringpy` is a program for computing rate constants using the " 
         "transition state theory (TST), in the gas phase and in solution."
         "The Gibbs activation energy is obtained by computing from scratch"
         " the canonical partition functions. Unimolecular and bimolecular"
         " reactions with one or two products are supported. Rate constants of"
         " bimolecular reactions involving the formation of pre-reactive"
         " and/or product complexes are also estimated. The reaction symmetry"
         " is considered. One-dimensional Wigner and Eckart tunneling"
         " corrections are also available. To compute rate constants in"
         " solution,`Eyringpy` employs the Collins–Kimball theory to include"
         " the diffusion-limit, the Marcus theory for electron transfer (ET)"
         " processes, and the molar fractions to account for the effect of pH"
         " in aqueous reactions.")

#Apartado para ejecutar test
def kinetics():
    st.write("## Welcome to **Kinetics test**")
    st.write("Please select the appropiate parameters for your test.")
    
    phase = st.radio("Phase", options=("Gas","Solution"))
    
    if phase == "Gas":
        st.selectbox("Method", options = ("Transition State Theory","CVT"))
        st.selectbox("Tunnel", options = ("WIG","ECK"))
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Temperature as a range.")
            st.write("*If you want to enter your"
                          " temperature as an intervale.*")
            intemp = st.number_input("Initial temperature", min_value=0.00, step=0.01)
            fintemp = st.number_input("Final temperature", min_value=0.00, step=0.01)
            step = st.number_input("Step size", min_value = 0, max_value = 1000, step = 1)
        
        with col2:
            st.write("Temperature as a list.")
            st.write("*If you want to enter your"
                          " temperature as list of values.*")
            st.text_input("List of temperatures")
def IRC():
    st.write("## Welcome to **IRC test**")

st.markdown("---")
st.write("# Run your test")
test = st.radio("What type of test do you want to run?", options=("IRC", "Kinetics"))

if test=="IRC":
    IRC()
else:
    kinetics()








