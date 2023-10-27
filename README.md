<p align="center">
  <img src="https://user-images.githubusercontent.com/47277280/111466253-18db3380-8734-11eb-9c6a-387ad34197af.PNG" width="200">
</p>
<h1 align="center">🌱 Plant Pathology 2020 🍃</h1>
<p align="center">Challenge to identify the category of foliar diseases in apple trees 🍏</p>
<p align="center">
  <a href="https://www.kaggle.com/c/plant-pathology-2020-fgvc7">🏆 Competition Link 🏆</a>
</p>

<br>

# 🥳 Achievement Announcement!
**I'm excited to announce that I was able to reach the top 4% in the world in the Competition 🌍🏆.**

<br>

# 📚 Table of Contents
1. [Overview](#-overview)
2. [Libraries Used](#libraries-used)
3. [Model Downloads](#-model-downloads)
4. [Techniques Used](#-techniques-used)
5. [Hyper Parameters](#hyper-parameters)

<br>


# 🌐 Overview
### 🚨 Problem Statement
Misdiagnosis of diseases in agricultural crops can lead to devastating effects. Our challenge is to employ a **Multilabel Classification** model to accurately diagnose leaf conditions based on images, aiding in the mitigation of economic and environmental impacts.

### 🤖 Problem Solution
Leverage **Deep Learning CNN Architecture** and **EfficientNetB7**, trained with a **TPU** for optimal performance.

### 📊 Data
* Total Images: 3642 (1821 for training and testing each)
* Columns in Training Set: image_id, healthy, multiple_disease, rust, scab
* More data details [Here](https://www.kaggle.com/c/plant-pathology-2020-fgvc7/data).


### 📈 Evaluation
Submissions are evaluated on mean column-wise **ROC AUC.**

<br>

# Libraries Used
* pandas
* numpy
* tensorflow
* sklearn
* ... and many more!

<br>

# 📥 Model Downloads
Ensure you have the pre-trained models for accurate predictions:
1. 📌 Download the pre-trained models from this Google Drive link:
   [Download Models Here](https://drive.google.com/drive/u/1/folders/1EN2pNV_Jc7fmoCXd1Z4SZ02HfYxxPlWh)
2. 🗂️ Place the downloaded models (`model1.h5` and `model2.h5`) in the root directory of your project.

<br>

# 👩‍🔬 Techniques Used
* CNN Model with Transfer learning
* Data Augmentation Techniques (Random flips)
* TPU Accelerator
* ... and others!

<br>

# Hyper Parameters
* Batch Size: 64
* Image Size: 800 & 768
* Epochs: 100 (with Early Stopping)
# Plant-Pathology-2020-FGVC7
