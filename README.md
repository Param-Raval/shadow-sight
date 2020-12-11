# Shadow Sight

Shadow Detection and removal is the process of enhance the computer vision applications including image segmentation, object recognition, object tracking etc. Detection and Removal of shadow from the images and videos can reduce the undesirable outcomes in the computer vision applications and algorithms. 

* ShadowSight uses Stacked Conditional GANs trained on ISTD and implemented unofficially in [this project](https://github.com/IsHYuhi/ST-CGAN_Stacked_Conditional_Generative_Adversarial_Networks). 

* This project gives the service of shadow detection and removal in the form of a Flask application

## Requirements
* Flask
* Python3.x
* PyTorch 1.5.0
* pillow
* matplotlib

## Run 
* Download the checkpoints (pre-trained model) from [here](https://drive.google.com/drive/folders/1J1l21k5AoUXHxic-Bj3eXBFP--YzjFXO?usp=sharing) and place them in a folder called *checkpoints*.
* Run `app.py` to start the application locally. You can make changes to parameters inside the scripts as needed.

## Some Implementation Details from the ST-CGAN project

### Usage
* Set datasets under ```./dataset```. You can Download datasets from [here](https://github.com/DeepInsight-PCALab/ST-CGAN). 

Then,
#### Training
```
python3 train.py
```
#### Testing
When Testing images from ISTD dataset.
```
python3 test.py -l <checkpoint number>
```
When you would like to test your own image.
```
python3 test.py -l <checkpoint number> -i <image_path> -o <out_path>
```


### Results
Here is a result from test sets.
![](https://github.com/IsHYuhi/ST-CGAN_Stacked_Conditional_Generative_Adversarial_Networks/blob/master/result/91-3.png)
(Left to right: input, ground truth, shadow removal, ground truth shadow, shadow detection)

#### Shadow Detection
Here are some results from validation set.
![](https://github.com/IsHYuhi/ST-CGAN_Stacked_Conditional_Generative_Adversarial_Networks/blob/master/result/detected_shadow.jpg)
(Top to bottom: ground truth, shadow detection)

#### Shadow Removal
Here are some results from validation set.
![](https://github.com/IsHYuhi/ST-CGAN_Stacked_Conditional_Generative_Adversarial_Networks/blob/master/result/shadow_removal.jpg)
(Top to bottom: input, ground truth, shadow removal)

### Trained model
You can download from [here](https://drive.google.com/drive/folders/1J1l21k5AoUXHxic-Bj3eXBFP--YzjFXO?usp=sharing).

## References
* Stacked Conditional Generative Adversarial Networks for Jointly Learning Shadow Detection and Shadow Removal, Jifeng Wang<sup>∗</sup>, Xiang Li<sup>∗</sup>, Le Hui, Jian Yang, **Nanjing University of Science and Technology**, [[arXiv]](https://arxiv.org/abs/1712.02478)
