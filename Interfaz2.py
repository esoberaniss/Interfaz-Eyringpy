import streamlit as st

#Informacion general sobre Eyringpy
st.image("logoe.jpg")
st.write("## *What is `Eyringpy`?*")
intro = st.write("`Eyringpy` is a program for computing rate constants using the " 
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
    
    st.write("Please upload the files for your test.")
    
    col1, col2 = st.columns(2)

    with col1:
        React1 = st.file_uploader("**REACT1 (required)**", type=["out"])
        Prod1 = st.file_uploader("**PROD1 (required)**", type=["out"])
        TS = st.file_uploader("**TS (required)**", type=["out"])
        React2 = st.file_uploader("*REACT2*", type=["out"])
        Prod2 = st.file_uploader("*PROD2*", type=["out"])
        IRC = st.file_uploader("**IRC (required)**", type=["out"])
        
    with col2:
        React1_SP = st.file_uploader("*REACT1 - Single point*", type=["out"])
        Prod1_SP = st.file_uploader("*PROD1 - Single point*", type=["out"])
        TS_SP = st.file_uploader("*TS - Single point*", type=["out"])
        React2_SP = st.file_uploader("*REACT2 - Single point*", type=["out"])
        Prod2_SP = st.file_uploader("*PROD2 - Single point*", type=["out"])
    
    if not React1 or not Prod1 or not TS or not IRC:
        st.warning("Please upload all required files to continue.")
    else:
        st.success("All required files have been uploaded!")
        
        st.write("Please select the appropiate parameters for your test.")
        
        phase = st.radio("Phase", options=("Gas","Solution"))
        
        if phase == "Gas":
            st.selectbox("Method", options = ("TST","CVT"))
            st.selectbox("Tunnel", options = ("WIG","ECK"))
            
            temp_inp = st.selectbox("Select the way you want to enter your"
                                " temperature values.", options = ("Range", "List"))
            
            if temp_inp == "Range":
                st.write("Temperature as a range.")
                intemp = st.number_input("Initial temperature", min_value = 0.0000000000, step=0.0000000001, format="%0.10f")
                fintemp = st.number_input("Final temperature", min_value = 0.0000000000, step=0.0000000001, format="%0.10f")
                
                if fintemp <= intemp:
                    st.error("The final temperature must be greater than the initial temperature.")
                else:
                    step = st.number_input("Step size", min_value = 0.0000000000, step=0.0000000001, format="%0.10f")
                    
                    inter_range = fintemp - intemp
                    if step == 0:
                        st.error("The step size must be non-zero.")
                    elif inter_range % step != 0:
                        st.error("The step size is not consistent with the"
                                 " temperature range. It must evenly divide the intervale.")
                    else:
                        pass
                    
            else:
                st.write("Temperature as a list.")
                num_temp = st.number_input("Number of temperature values"
                                           " that you will enter:", min_value=1, step=1,)
                if num_temp:
                    st.write("Enter the temperature values:")
                    cols = st.columns(4)
                    temp_list = []
                    
                    for i in range(num_temp):
                        col = cols[i % 4]  # Seleccionar la columna de manera cíclica
                        temp_value = col.number_input(f"Temperature {i+1}", min_value=0.0000000000,
                                                      step=0.0000000001, format="%0.10f")
                        temp_list.append(temp_value)
                                         
                    
def IRC():
    st.write("## Welcome to **IRC test**")

st.markdown("---")
st.write("# Run your test")
test = st.radio("What type of test do you want to run?", options=("IRC", "Kinetics"))
    
if test=="IRC":
    IRC()
else:
    kinetics()








