x <- read.csv("/Users/yat/Desktop/subset.csv")

# Calculator function
calculator <- function(MET_RX_DOSE) {
  counter <- 0
  for(i in MET_RX_DOSE){
    if(!is.na(i)){
      counter <- counter + 1
    }
  }
  counter
} 

# execute the function
count <- c()
for(subject in 1:nrow(x)){
  # Followed by the sample input file, the MET_RX_DOSE are located in 435~466 columns
  count <- cbind(count,calculator(x[subject,435:466])) 
}

#Write result to the output file
result <- cbind(x, MET_RX_DOSE_COUNT=t(count))
write.csv(result, file = "/Users/yat/Desktop/subset_out.csv", row.names=FALSE)
