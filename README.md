# TissueDetection2024
<a href="https://universe.roboflow.com/zshar/segmentation-tissue-detectionpt3">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a>

## Abstract
Medical ultrasounds visualize internal structures, like organs. A physician interpret-
ing an ultrasound image must identify structure contours, brightness, and texture
differences. YOLOv8 is a state of the art image segmentation model that indicates
the contours of objects in an image. This study develops a real-time segmentation
model that identifies tissue in ultrasound images. Ultrasound images were obtained,
spliced into frames, and annotated in Roboflow. The Ultralytics library and Com-
mand Line Interface trained an image segmentation model. After 111 epochs of
training, the model’s performance increased. The 86th epoch produced the best
model. It had a 0.85115 mAP50-95 rating and 0.91 F1 Score at 0.521 confidence.
The model precisely identifies tissue in a 60 test image assessment. The model
reliably predicted images in 300 ms or less. This study developed a model that can
be utilized in real-time clinical practice. One application is automated demarcation
of tissue with three dimensional modeling scans. Future studies integrating in-vivo
organ structure ultrasound scans into the training dataset would develop a model
competent for clinical practice.

## Greetings
Hello! My name is Zain Shariff, I am a freshman at Curtis Junior High School, and I am deeply excited to showcase my research that I have been working for a year. This year's project consists of the development of an image machine learning model that detects tissue present in ultrasound scans, and detects and trace contours of that tissue.

## How did you do this?
To obtain the images, I used a 3.5 MHz ultrasound as parsed it using a simple python program I had written on my local system. I imported the images onto Roboflow which were annotated. I exported the dataset and developed a YOLOv8 extra large segmentation model using [Ultralytics](https://github.com/ultralytics/ultralytics). This was done on a local system using Command Line Interface CLI.
I have gone more in-depth into the process in my paper.

## Where do I find what?
To find the images used for the dataset go into the dataset folder. The Roboflow Dataset can be found [here](https://universe.roboflow.com/zshar/segmentation-tissue-detectionpt3). For the parser code in python go to the the python file named "splicer.py". The model can be found as "best.pt".
My paper can be found in "paper.pdf".

## License
[Tissue Detection in Ultrasound Images Using Real-Time Image Segmentation Model](https://github.com/zshariff6506/TissueDetection2024) © 2024 by Zain Shariff is licensed under CC BY-NC-SA 4.0
