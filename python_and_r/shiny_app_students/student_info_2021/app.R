#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(DT)
source("../student_data.R")
student_names <- as.list(student_data$`Full Name`)
cohorts <- unique(as.list(student_data$cohort))
programmes <- unique(as.list(student_data$programme))

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("RHUL Student Results Information 2020/21"),

    # Sidebar
    sidebarLayout(
        sidebarPanel(
          width = 3,
          img(src = "https://www.royalholloway.ac.uk/images/logo-og-default.jpg", height = "auto", width = 200),
          selectInput("programme", h3("Select a Programme"), choices = append(programmes, "All", after=0)),
          selectInput("cohort", h3("Select a Cohort"), choices = append(cohorts, "All", after=0)),
          selectInput("students", h3("Select a student"), choices = append(student_names, "All", after=0))
        ),

        # Main Panel
        mainPanel(
          width = 9,
          DT::dataTableOutput("results")
          
        )
        )
    )

# Define server logic required to draw a histogram
server <- function(input, output) {

    output$results <- DT::renderDataTable({
      if(input$cohort == "All" && input$programme == "All" && input$students == "All") student_data
      else if (input$cohort != "All" && input$programme == "All" && input$students == "All") student_data <- student_data %>% filter(cohort == input$cohort)
      else if (input$cohort == "All" && input$programme != "All" && input$students == "All") student_data <- student_data %>% filter(programme == input$programme)
      else if (input$cohort == "All" && input$programme == "All" && input$students != "All") student_data <- student_data %>% filter(`Full Name` == input$students)
      else if (input$cohort != "All" && input$programme != "All" && input$students == "All") student_data <- student_data %>% filter(cohort == input$cohort, programme == input$programme)
      else if (input$cohort != "All" && input$programme == "All" && input$students != "All") student_data <- student_data %>% filter(cohort == input$cohort, `Full Name` == input$students)
      else if (input$cohort == "All" && input$programme != "All" && input$students != "All") student_data <- student_data %>% filter(programme == input$programme, `Full Name` == input$students)
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
