import mlflow
import random
import yaml
import os

with mlflow.start_run():
    epochs = yaml.safe_load(open('params.yaml'))["train_model"]["epochs"]
    mlflow.log_param("epochs",epochs)
    for epoch in range(epochs):
        train_acc = epoch + random.random()
        train_loss = epochs - epoch - random.random
        val_acc = epoch + random.random()
        val_loss = epochs - epoch - random.random



        mlflow.log_metric("train/accuracy" , train_acc)
        mlflow.log_metric("train/loss" , train_loss)
        mlflow.log_metric("val/accuracy" , val_acc)
        mlflow.log_metric("val/loss" , val_loss)
        


