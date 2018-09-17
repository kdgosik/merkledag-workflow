library(dplyr)

iris %>% 
    group_by(Species) %>% 
    summarise(mean(Petal.Length))