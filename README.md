# Files guid
* Images: An image for each case .
* top-4%-lb: Here is the main work .
* back_ground: Code used to remove background . (note that I didn't use it in my model)
* Plant EDA: Exploratory data analysis on the data (simple) . **NOTE** : to see all the plots in the GitHub notebook you should paste the GitHub notebook link [Here](https://nbviewer.jupyter.org) 
# Table of contents
* [Overview](#overview)
* [Libraries I used](#Libraries-i-used)
* [Techniques I used](#techniques-i-used)
* [Hyper Parameters](#hyper-parameters)
* [Bonus](#bonus)
* [Reference](#reference)

# Overview
### Problem Statement
Misdiagnosis of the many diseases impacting agricultural crops can lead to misuse of chemicals leading to the emergence of resistant pathogen strains, increased input costs, and more outbreaks with significant economic loss and environmental impacts. Current disease diagnosis based on human scouting is time-consuming and expensive, and although computer-vision based models have the promise to increase efficiency, the great variance in symptoms due to age of infected tissues, genetic variations, and light conditions within trees decreases the accuracy of detection.
### Problem Type
Given a photo of an apple leaf where the challenge is to train a **Multilabel Classification** to define if the leaf in the photo is healthy or not (rust or scab), sometimes more than one disease on a single leaf (multiple_diseases), thats why it is Multilabel Classification .
### Problem solution
Here we should use **DeepLearning CNN Architecture** to classify healthy from not healthy images , where first we need to import our data and prepare it for the Neural Network by reshaping the images and do some image preprocessing on the data .

After preparing our data we should build our model using one of the APIs like keras , the model I used is **EfficientNetB7** thats why I trained it using [**TPU**](https://en.wikipedia.org/wiki/Tensor_Processing_Unit) instead of **GPU** witch is mush more faster for huge models like B7 .

Evaluating our model is the most important step where we need to make sure that the model is giving the optimal accuracy so we can use it in a real life scenario , where we can do this by using different techniques that been mentioned down .

At the end we test our model on the hold-out data to get the accuracy that the model will give after deploying it .
More details in the code .
### Data
The data contains 1821 images for training set and same for test set , in total 3642 .
Training set contains 4 columns : (image_id, healthy, multiple_disease, rust, scab) , where the test set contains the image_id .

[Here](https://www.kaggle.com/c/plant-pathology-2020-fgvc7/data) you can find the data .

![healthy](https://user-images.githubusercontent.com/47277280/111466253-18db3380-8734-11eb-9c6a-387ad34197af.PNG)
![multy](https://user-images.githubusercontent.com/47277280/111466259-1aa4f700-8734-11eb-9af1-1719cdbd7179.PNG)


![rust](https://user-images.githubusercontent.com/47277280/111466267-1d075100-8734-11eb-98bf-9faf53606d94.PNG)
![scab](https://user-images.githubusercontent.com/47277280/111466269-1d9fe780-8734-11eb-88d5-18805f567f4e.PNG)

### Evaluation
Submissions are evaluated on mean column-wise **ROC AUC**. In other words, the score is the average of the individual AUCs of each predicted column.
# Libraries I used
* pandas
* numpy
* matplotlib
* plotly
* cv2
* tqdm
* os
* sklearn
* tensorflow
* keras
* warnings
* efficientnet
* kaggle_datasets
# Techniques I used
* CNN Model
   * Transfer learning : **EfficientNetB7** model on 5 folds. 
   * Ensemble model : best model was **predictions of fold 1** * 0.7 + **predictions of fold 4** * 0.3.
* Data augmentation techniques
  * Random flip left and right .
  * Random flip up and down .
* TPU accelerator
* EarlyStopping
* ReduceLROnPlateau
# Hyper Parameters
* Batch size : 64
* Img_size : 800
* Epochs : 100 (with EarlyStopping)
* Folds : 5
* Seed : 42
# Bonus
The bonus in this project is **pyplot** library where you can interact with plots unlike matplotlib , you can find it in **Plant EDA** file .
Also **back_ground** file will help you to separate the leaf from the background in the image, this can speed up your model and improve the accuracy in some cases .
# Reference
* [Background Removal](https://www.kaggle.com/victorlouisdg/plant-pathology-opencv-background-removal)
* [EDA](https://www.kaggle.com/tarunpaparaju/plant-pathology-2020-eda-models)
* [Competition](https://www.kaggle.com/c/plant-pathology-2020-fgvc7)
