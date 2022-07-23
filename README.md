# Sistema-Fuzzy-M-quina-de-Lavar
 Sistema Fuzzy embarcado em uma máquina de lavar roupa capaz de controlar corretamente a temperatura da agua e tempo do ciclo.

Antecedentes (entradas)
Grau da sujeira (cloth_dirtiness -> variável linguistica)
Universe: Grau de sujeira da roupa em uma escala de 0 a 10
Qualificadores do conjunto fuzzy cloth_dirtiness: low, medium e high
Peso (cloth_mass)
Universe: Peso das roupas em uma escala de 0 a 10
Qualificadores do conjunto fuzzy cloth_mass: light, medium e heavy
Sensibilidade (cloth_sensitivity)
Universe: Sensibilidade das roupas em uma escala de 0 a 10
Qualificadores do conjunto fuzzy cloth_sensitivity: sensível, pouco sensível e resistente

Consequents (Outputs)
Temperatura
Universe: Quão quente vai ser a água em uma escala de 0 a 80 (graus)
Qualificadores do conjunto fuzzy temperature: low, medium, high
Tempo de Ciclo (time_process)
Universe: O tempo de ciclo do processo em uma escala de 0 a 150 (minutos)
Fuzzy set: fast, normal, slow
