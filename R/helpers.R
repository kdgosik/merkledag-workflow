library(digest)


#' @description  Example of object to be created
#' @details this will be used to create a csv file

data.frame(root = "",    ## hash of dependency root
           date = "",    ## date object was created
           title = "",   ## title of content / filename
           content = "", ## description of file and/or important information
           context = "", ## link to location of the content if any
           tags = "",    ## tags of the content for groupung
           hash = ""     ## sha256 hash digest of object
           )



