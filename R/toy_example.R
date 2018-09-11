library(digest)


## Hello World (Toy Example)

hello_file <- "Hello World"

addquestion <- function(txt) {
  return(paste0(txt, "?"))
}

AddQuestionMark.R <- 'addquestion <- function(txt) {
  return(paste0(txt, "?"))
}'

genesisBlockHello <- list(
  Name = "hello.txt",
  Timestamp = Sys.time(),
  Hash = digest(hello_file, "sha256"),
  PrevHash = ""
)

genesisBlockFunction <- list(
  Name = "AddQuestionMark.R",
  Timestamp = Sys.time(),
  Hash = digest(AddQuestionMark.R),
  PrevHash = ""
)


AddQuestionMark.R <- 'addquestion <- function(txt = hello_file) {
  return(paste0(txt, "?"))
}'

usedAddQuestionBlock <- list(
  Name = "AddQuestionMark.R",
  Timestamp = Sys.time(),
  Hash = digest(AddQuestionMark.R),
  PrevHash = genesisBlockHello$Hash
)

hello_file <- addquestion(hello_file)


modifiedHelloBlock <- list(
  Name = "hello.txt",
  Timestamp = Sys.time(),
  Hash = digest(hello_file, "sha256"),
  PrevHash = usedAddQuestionBlock$Hash
)

out <- data.frame(rbind(genesisBlockHello, genesisBlockFunction, usedAddQuestionBlock, modifiedHelloBlock))
write_json(toJSON(out), "example.json")
