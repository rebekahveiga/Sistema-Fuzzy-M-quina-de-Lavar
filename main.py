# Se necessário, instale o pacote skfuzzy
!pip install scikit-fuzzy
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
cloth_dirtiness =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_dirtiness') #sujeira da roupa
cloth_mass =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_mass') #peso roupa
cloth_sensitivity =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_sensitivity') #sensibilidade da roupa
temperatura = ctrl.Consequent(np.arange(0, 81, 1), 'temperatura')
time_process = ctrl.Consequent(np.arange(0, 151, 1), 'time_process')

#Grau de sujeira
cloth_dirtiness['low'] = fuzz.trimf(cloth_dirtiness.universe, [0, 0, 4])
cloth_dirtiness['medium'] = fuzz.trimf(cloth_dirtiness.universe, [3, 6, 8])
cloth_dirtiness['high'] = fuzz.trimf(cloth_dirtiness.universe, [6, 10, 10])

#Peso das roupas
cloth_mass['light'] = fuzz.trimf(cloth_mass.universe, [0, 0, 4])
cloth_mass['medium'] = fuzz.trimf(cloth_mass.universe, [3, 6, 8])
cloth_mass['heavy'] = fuzz.trimf(cloth_mass.universe, [6, 10, 10])

#Grau de sensibilidade
cloth_sensitivity['sensivel'] = fuzz.trimf(cloth_sensitivity.universe, [0, 0, 4])
cloth_sensitivity['pouco sensivel'] = fuzz.trimf(cloth_sensitivity.universe, [3, 5, 8])
cloth_sensitivity['resistente'] = fuzz.trimf(cloth_sensitivity.universe, [6, 10, 10])

#temperatura
temperatura['low'] = fuzz.trimf(temperatura.universe, [0, 0, 27])
temperatura['medium'] = fuzz.trimf(temperatura.universe, [20, 34, 45])
temperatura['high'] = fuzz.trimf(temperatura.universe, [40, 55, 70])

#Tempo de ciclo
time_process['fast'] = fuzz.trimf(time_process.universe, [0, 0, 50])
time_process['normal'] = fuzz.trimf(time_process.universe, [40, 80, 95])
time_process['slow'] = fuzz.trimf(time_process.universe, [80, 120, 130])

temperatura['low'].view()
temperatura['medium'].view()
temperatura['high'].view()

time_process['slow'].view()
time_process['normal'].view() 
time_process['fast'].view() 

temperatura.view()
time_process.view()
cloth_dirtiness.view()
cloth_mass.view()
cloth_sensitivity.view()

rule1 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['resistente'], temperatura['high'])
rule2 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_mass['heavy'] | cloth_sensitivity['pouco sensivel'], temperatura['medium'])
rule3 = ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['sensivel'] | cloth_mass['heavy'], temperatura['low'])
rule4 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['pouco sensivel'] & cloth_mass['light'], time_process['fast'])
rule5 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['pouco sensivel'] | cloth_mass['light'], time_process['fast'])
rule6 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['sensivel'] & cloth_mass['heavy'], time_process['slow'])
rule7 = ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['pouco sensivel'] & cloth_mass['medium'], time_process['normal'])
rule8 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['resistente'] & cloth_mass['medium'], time_process['slow'])
rule9 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['resistente'] & cloth_mass['medium'], time_process['normal'])
rule10 =ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['resistente'] & cloth_mass['light'], time_process['fast'])
rule11 =ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['resistente'] & cloth_mass['medium'], time_process['fast'])
rule12 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['sensivel'] & cloth_mass['heavy'], time_process['slow'])

#São passadas as 12 regras
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12])
#Essa função produz o resultado do pipeline de execução do sistema Fuzzy
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input['cloth_dirtiness'] = 7.7
tipping.input['cloth_mass'] = 6.3
tipping.input['cloth_sensitivity']= 7

tipping.compute( )

print(tipping.output['temperatura'])
temperatura.view(sim=tipping)
plt.show()

print(tipping.output['time_process'])
time_process.view(sim=tipping)
plt.show()
