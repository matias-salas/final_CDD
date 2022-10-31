library(tidyverse)
library(forcats)
library(dplyr)

df = read_csv('C:/Users/Usuario/OneDrive/Desktop/Uni/UNSAM/ciencia_de_datos/Intro_ciencia_de_datos/FINAL_CODIGOS/presupuestos_comunas_anios_comma.csv')


plot_1  = ggplot(df) + 
  geom_density_ridges(aes(x= anio,y=factor(desc_comuna), fill= desc_comuna), alpha=0.5)+ 
  labs(title ="Presupuesto por año para cada comuna") + 
  xlab("Años")+ 
  ylab("Comunas") + 
  theme(legend.position = "nome", axis.line = element_line(colour = "black", size =0.5))

plot_1
