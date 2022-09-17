library(dplyr)
library(readr)

student_data <- read_csv("C:\\Users\\storr\\Documents\\0_coding\\shiny_app_students\\all_student_data.csv")

#head(student_data)

get_cohort <- function(prog) {
  data <- student_data %>%
    filter(programme == prog)
  return(data)
}


