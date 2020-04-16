#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(digest)
library(shinyFiles)

# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("Blockchain Tracking"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
        shinyUI(bootstrapPage(
          actionButton("submit", "Create Block"),
          shinyFilesButton('files', label='File select', title='Please select a file', multiple=FALSE)
        ))
      ),
      
      # Show a plot of the generated distribution
      mainPanel(
        # root = "",    ## hash of dependency root
        # date = "",    ## date object was created, automatically generated
        # title = "",   ## title of content / filename
        # content = "", ## description of file and/or important information
        # context = "", ## link to location of the content if any
        # tags = "",    ## tags of the content for groupung
        # hash = ""     ## sha256 hash digest of object
        
        textInput("root", "Select Root"),
        textInput("title", "Give a title to the block"),
        textInput("content", "Actual Content or Description"),
        textInput("context", "Hyperlinks or file locations of content"),
        textInput("tags", "Grouping Tags")

      )
   )
)

# Define server logic required to draw a histogram
server <- function(input, output, session) {
  

  shinyFileChoose(input, 'files', root=c(root='.'), filetypes=c('', 'txt'))
  
  # output$root <- renderText({ input$root })
  # output$title <- renderText({ input$title })
  # output$content <- renderText({ input$content })
  # output$context <- renderText({ input$context })
  # output$tags <- renderText({ input$tags })
  
  
  observeEvent(input$submit, {
    
    obj <- list(root = input$root,    ## hash of dependency root
               date = Sys.time(),    ## date object was created
               title = input$title,   ## title of content / filename
               content = input$content, ## description of file and/or important information
               context = input$context, ## link to location of the content if any
               tags = input$tags    ## tags of the content for groupung
    )
    
    obj_hash <- digest(object = obj, algo = "sha256")
    
    df <- as.data.frame(obj)
    df$hash <- obj_hash
    
    write.csv(x = df, 
              file = "blockchain-edgelist.csv", 
              append = TRUE,
              row.names = FALSE)
    
  })

}

# Run the application 
shinyApp(ui = ui, server = server)

