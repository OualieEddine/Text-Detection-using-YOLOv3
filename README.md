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
## Preprocessing
After downloading the data set, the first step is to generate the annotations (using XML files)
The following command generates train and test directories that contains:
* Annotations: directory that contains the XML files
* JPEGImages: directory that contains re-nammed data set
* ImageSets: directory that contains labels of the images
```
!python data_to_xml.py
```
The last step in this phase is running the following script:
```
!python xml_to_yolov3.py
```
The previous script generate data_train.txt and data_test.txt which are text files that contains full paths of the train and test data set
Generally in this step, we can add (xmin,ymin,w,h,angle) or putting the xml files in the same directory as images, and in our project we choosed the last one.
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
The last step in this phase, it to build the required libraries by running the following command in the darknet resp:
```
!make
```
## Training
After adding the angle calculation, and pixels normalization in the training file (done in our project), now we have to launch the following command to start training
```
!darknet/darknet detector train config_data/labelled_data.data darknet/cfg/yolov3_training.cfg darknet53.conv.74 -dont_show 
```
PS: according to the limitations of using GPU in Google Colab, we used checkpoint in this project to save instance from the training phase

## Testing
Once the model finished the training, its ready to used for detecting
In our project we used a checkpoint to test later
First, its required to mount tensorflow 1 in our colab
```
%tensorflow_version 1.x
```
After uploading the set of test in the required file, we can print set py using the following command:
```
!python print_data.py
```
and py launching the following command, the model will start detecting text and bounding-box it 
```
!python eval.py --test_data_path='imgs/' --gpu_list=0 --checkpoint_path='check/'  --output_dir='out/'
```
As final step, we can print the image set after testing using the following command:
```
!python print_after_data.py
```

## Results Discussition
By running map.py script, we can obtain the evaluation of our model.
In our case, we obtained the following Results:
* Precision = 0.89
* Recall = 0.84
* F1-score = 0.88
* F-measure = 0.86
* Accuracy = 0.94
* (mAP@0.50) = 0.86
 
## Conclusion
I would like to thank all the teachers of our department, jurys, and special thank for my advisor: Dr.A.TIBERMACINE
Concerning the futur works, we will try to publish a scientific publication concerning our work, and why not joining the benchmarking list.




