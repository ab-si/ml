# install and load the data from caret package
install.packages("caret", dependencies=TRUE)

library(caret)
library(reshape2)

data(iris)

# Renaming the dataset
dataset <- iris

# or
# filename <- "~/work/github/ml/iris/iris.csv"
# dataset <- read.csv(file=filename, header=FALSE)

colnames(dataset) <- c("Sepal.Length","Sepal.Width","Petal.Length","Petal.Width","Species")

# Creating a validation and testing dataset
validation_index <- createDataPartition(dataset$Species, p=0.80, list=FALSE)
validation_data <- dataset[-validation_index,]
train_test_data <- dataset[validation_index,]

# data summary
dim(train_test_data)
head(train_test_data)

# Levels of classes
levels(train_test_data$Species)

# Count of each class
table(train_test_data$Species)

#Summary
summary(train_test_data)

