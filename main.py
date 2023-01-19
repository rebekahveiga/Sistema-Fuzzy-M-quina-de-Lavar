!pip install scikit-fuzzy
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
cloth_dirtiness =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_dirtiness') 
cloth_mass =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_mass')
cloth_sensitivity =  ctrl.Antecedent(np.arange(0,11,1), 'cloth_sensitivity') 
temperature = ctrl.Consequent(np.arange(0, 81, 1), 'temperature')
time_process = ctrl.Consequent(np.arange(0, 151, 1), 'time_process')

#dirty
cloth_dirtiness['low'] = fuzz.trimf(cloth_dirtiness.universe, [0, 0, 4])
cloth_dirtiness['medium'] = fuzz.trimf(cloth_dirtiness.universe, [3, 6, 8])
cloth_dirtiness['high'] = fuzz.trimf(cloth_dirtiness.universe, [6, 10, 10])

#clothing mass
cloth_mass['light'] = fuzz.trimf(cloth_mass.universe, [0, 0, 4])
cloth_mass['medium'] = fuzz.trimf(cloth_mass.universe, [3, 6, 8])
cloth_mass['heavy'] = fuzz.trimf(cloth_mass.universe, [6, 10, 10])

#clothing sensitivity
cloth_sensitivity['sensivel'] = fuzz.trimf(cloth_sensitivity.universe, [0, 0, 4])
cloth_sensitivity['pouco sensivel'] = fuzz.trimf(cloth_sensitivity.universe, [3, 5, 8])
cloth_sensitivity['resistente'] = fuzz.trimf(cloth_sensitivity.universe, [6, 10, 10])

#temperature
temperatura['low'] = fuzz.trimf(temperature.universe, [0, 0, 27])
temperatura['medium'] = fuzz.trimf(temperature.universe, [20, 34, 45])
temperatura['high'] = fuzz.trimf(temperature.universe, [40, 55, 70])

#cycle time
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

rule1 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['resistant'], temperatura['high'])
rule2 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_mass['heavy'] | cloth_sensitivity['unresponsive'], temperatura['medium'])
rule3 = ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['sensitive'] | cloth_mass['heavy'], temperatura['low'])
rule4 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['unresponsive'] & cloth_mass['light'], time_process['fast'])
rule5 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['unresponsive'] | cloth_mass['light'], time_process['fast'])
rule6 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['sensitive'] & cloth_mass['heavy'], time_process['slow'])
rule7 = ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['unresponsive'] & cloth_mass['medium'], time_process['normal'])
rule8 = ctrl.Rule(cloth_dirtiness['high'] & cloth_sensitivity['resistant'] & cloth_mass['medium'], time_process['slow'])
rule9 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['resistant'] & cloth_mass['medium'], time_process['normal'])
rule10 =ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['resistant'] & cloth_mass['light'], time_process['fast'])
rule11 =ctrl.Rule(cloth_dirtiness['low'] & cloth_sensitivity['resistant'] & cloth_mass['medium'], time_process['fast'])
rule12 = ctrl.Rule(cloth_dirtiness['medium'] & cloth_sensitivity['sensitive'] & cloth_mass['heavy'], time_process['slow'])

#12 rules
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12])

# This function produces the result of the execution pipeline of the Fuzzy system
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input['cloth_dirtiness'] = 7.7
tipping.input['cloth_mass'] = 6.3
tipping.input['cloth_sensitivity']= 7

tipping.compute( )

print(tipping.output['temperature'])
temperature.view(sim=tipping)
plt.show()

print(tipping.output['time_process'])
time_process.view(sim=tipping)
plt.show()
