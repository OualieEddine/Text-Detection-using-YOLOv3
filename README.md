# Text-Detection-using-YOLOv3
## Intro
This is my graduation project which consists at using YOLOv3 to detect HORIZONTAL and INCLINED text in a given picture. Under the mentoring of Dr. A.TIBERMACINE, we finally built accurate model for the mentioned title above.
* The output Boxes are colored with Green (0,255,0) and using thickness=2.
* The used data set is ICDAR 2015 which is available on the following link: https://rrc.cvc.uab.es/?ch=4&com=downloads (login is required)
* Resolution used is : 720x1280
* The training was done on Google Colab, and containing all the details
* Training Colaboratory sheet : https://colab.research.google.com/drive/1tDsiE1ECmYelKMwVHGWge0jsyqKqoZPm?usp=sharing
* Testing Colaboratory sheet: https://colab.research.google.com/drive/1zmuNx2VJzI8vQ8-kh1uL3JB157By6ait?usp=sharing
* For future works, we are aiming to join the top bencharmking for this purpose.
* PS: The model supports using any provided dataset that containing an angle.

### PS: Concerning the prepared dataset, YOLOv3 weights, last mobile weight... and according to its large size (1GB) and the limitations of github on the uploaded file size, all the previous mentioned files are available on my drive and you can download it from the following link: 
https://drive.google.com/drive/folders/1jyoanDf5DyLUx8ah2r9pIHbZ4i_pNek0?usp=sharing

https://drive.google.com/drive/folders/1-tYGsCONOz2WphUibSZps08jV5DZeqhI?usp=sharing

## Preprocessing
After downloading the data set, the first step is to generate the annotations (using XML files)
The following command generates train and test directories that contains:
* Annotations: directory that contains the XML files
* JPEGImages: directory that contains re-nammed data set
* ImageSets: directory that contains labels of the images
![data](https://user-images.githubusercontent.com/86682718/123941929-8f720900-d992-11eb-9746-8658b0591f8a.PNG)

```
!python data_to_xml.py
```
The last step in this phase is running the following script:
```
!python xml_to_yolov3.py
```
![last](https://user-images.githubusercontent.com/86682718/123941767-63ef1e80-d992-11eb-8e98-85c793548596.PNG)

The previous script generate data_train.txt and data_test.txt which are text files that contains full paths of the train and test data set
Generally in this step, we can add (x,y,w,h,angle) or putting the xml files in the same directory as images, and in our project we choosed the last one and adding a txt file for each images contating the cardinalitines of all the text boxes in this picture.


PS: dont forget to add another file.data which contains the paths of the previous txt files and the backup which new mobile-model will be saved
OPTIONAL: in case you want to add any label with bounding box, all what is required is to create a new file.txt and saving the label on it, later it will be attached with training command.
## Preparing Model
In this project we are using YOLOv3 
The first step is to download darknet weights with the following command:
```
!wget https://pjreddie.com/media/files/darknet53.conv.74
```
Later, we have to obtain the darknet resp, and changing the number of classes to :1 and filters to "(NumOfClasses+5)*3"
By running the following commands, the operation will be done
```
!sed -i 's/batch=1/batch=64/' cfg/yolov3_training.cfg
!sed -i 's/subdivisions=1/subdivisions=16/' cfg/yolov3_training.cfg
!sed -i 's/max_batches = 500200/max_batches = 4000/' cfg/yolov3_training.cfg
!sed -i '610 s@classes=80@classes=1@' cfg/yolov3_training.cfg
!sed -i '696 s@classes=80@classes=1@' cfg/yolov3_training.cfg
!sed -i '783 s@classes=80@classes=1@' cfg/yolov3_training.cfg
!sed -i '603 s@filters=255@filters=18@' cfg/yolov3_training.cfg
!sed -i '689 s@filters=255@filters=18@' cfg/yolov3_training.cfg
!sed -i '776 s@filters=255@filters=18@' cfg/yolov3_training.cfg
```
![Capture](https://user-images.githubusercontent.com/86682718/123943567-30ad8f00-d994-11eb-8269-6de2e3b7f119.PNG)

The last step in this phase, it to build the required C++ libraries by running the following command in the darknet resp:
```
!make
```
![gg](https://user-images.githubusercontent.com/86682718/123943806-66527800-d994-11eb-973a-14afbcfc0119.PNG)

## Training
After adding the angle calculation, and pixels normalization in the training file (done in our project), now we have to launch the following command to start training
```
!darknet/darknet detector train config_data/labelled_data.data darknet/cfg/yolov3_training.cfg darknet53.conv.74 -dont_show 
```
![training](https://user-images.githubusercontent.com/86682718/123943967-8eda7200-d994-11eb-925a-9bdde4c4667b.PNG)

PS: according to the limitations of using GPU in Google Colab, we used checkpoint in this project to save instance from the training phase

![sssssss](https://user-images.githubusercontent.com/86682718/123950332-791c7b00-d99b-11eb-8956-fb04e8ecdce2.PNG)


PS: You can always check the weights of the mobile model on the backup folder

![kkkkk](https://user-images.githubusercontent.com/86682718/123945357-f7761e80-d995-11eb-80cb-eb425dfc851e.PNG)

## Testing
Once the model finished the training, its ready to used for detecting
In our project we used a checkpoint to test later
First, its required to mount tensorflow 1 in our colab
```
%tensorflow_version 1.x
```
![tt](https://user-images.githubusercontent.com/86682718/123944290-e678dd80-d994-11eb-956c-24285ed5f127.PNG)

After uploading the set of test in the required file, we can print set py using the following command:
```
!python print_data.py
```
![download (6)](https://user-images.githubusercontent.com/86682718/123944317-ed075500-d994-11eb-83e8-435678819787.png)

and py launching the following command, the model will start detecting text and bounding-box it 
```
!python eval.py --test_data_path='imgs/' --gpu_list=0 --checkpoint_path='check/'  --output_dir='out/'
```
![dd](https://user-images.githubusercontent.com/86682718/123944569-26d85b80-d995-11eb-9415-8c8b98d26359.PNG)

As final step, we can print the image set after testing using the following command:
```
!python print_after_data.py
```
![download (1)](https://user-images.githubusercontent.com/86682718/123944353-f4c6f980-d994-11eb-81d6-e1660a74534c.png)

Its required in the previous step to choose: Testin_Directory_Path, Model_Path, and Output_Path

As final step, we added the option of saving a txt file that cotnains the cardinalities of bounding box, which will help later in the case of recognition

## Results Discussion
By running map.py script, we can obtain the evaluation of our model.
In our case, we obtained the following Results:
* Precision = 0.89
* Recall = 0.84
* F1-score = 0.88
* F-measure = 0.86
* Accuracy = 0.94
* (mAP@0.50) = 0.86

 ![zzzz](https://user-images.githubusercontent.com/86682718/123945265-df9e9a80-d995-11eb-8ac5-089c22f74c96.PNG)

## Conclusion
### I would like to thank all the teachers of our department, jurys, and special thank for my supervisor: Dr.A.TIBERMACINE
### Concerning the futur works, we will try to publish a scientific publication concerning our work, and why not joining the benchmarking list.




