# Table of contents
* [Overview]()
* [Library I used]()
* [Techniques I used]()
* [Hyper Parameters]()
* [bonus]()


# Overview :

### Problem Statement
Misdiagnosis of the many diseases impacting agricultural crops can lead to misuse of chemicals leading to the emergence of resistant pathogen strains, increased input costs, and more outbreaks with significant economic loss and environmental impacts. Current disease diagnosis based on human scouting is time-consuming and expensive, and although computer-vision based models have the promise to increase efficiency, the great variance in symptoms due to age of infected tissues, genetic variations, and light conditions within trees decreases the accuracy of detection.

### Problem Type
Given a photo of an apple leaf where the challenge is to train a **Multilabel Classification** to defined if the leaf in the photo is healthy or diseased (rust or scab), sometimes more than one disease on a single leaf (multiple_diseases), thats why it is Multilabel Classification .

### Data
The data contains 1821 images for training set and same for test set , in total 3642 .
Training set contains 4 columns : (image_id, healthy, multiple_disease, rust, scab) , where the test set contains the image_id .

### Evaluation
Submissions are evaluated on mean column-wise **ROC AUC**. In other words, the score is the average of the individual AUCs of each predicted column.


# Library I used :
* pandas
* numpy
* os
* sklearn
* tensorflow
* keras
* warnings
* efficientnet
* kaggle_datasets

# Techniques I used :
* Model
   * Ensemble model : best model was **predictions of model[0] * 0.7 + predictions of model[3] * 0.3**.
   * Transfer learning : EfficientNetB7 model .
* Data augmentation techniques
  * Random flip left and right .
  * Random flip up and down .
* TPU accelerator
* EarlyStopping
* ReduceLROnPlateau


# Hyper Parameters :
* Batch size : 46
* Img_size : 800
* Epochs : 100 (with EarlyStopping)
* Folds : 5
* Seed : 42

# Bonus :

# Reference :
[Background Removal](https://www.kaggle.com/victorlouisdg/plant-pathology-opencv-background-removal)
[Competition](https://www.kaggle.com/c/plant-pathology-2020-fgvc7)
