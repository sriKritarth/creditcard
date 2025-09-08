import os
import random

import mlflow
import yaml

with mlflow.start_run():
    epochs = yaml.safe_load(open("params.yaml"))["train_model"]["epochs"]
    mlflow.log_param("epochs", epochs)
    for epoch in range(epochs):
        train_acc = epoch + random.random()
        train_loss = epochs - epoch - random.random()
        val_acc = epoch + random.random()
        val_loss = epochs - epoch - random.random()

        mlflow.log_metric("train/accuracy", train_acc)
        mlflow.log_metric("train/loss", train_loss)
        mlflow.log_metric("val/accuracy", val_acc)
        mlflow.log_metric("val/loss", val_loss)

with open("metrics.txt" , 'w') as outfile:
    outfile.write("Final val accuracy: " + str(val_acc) + "\n")
    outfile.write("Final loss accuracy: " + str(val_loss) + "\n")