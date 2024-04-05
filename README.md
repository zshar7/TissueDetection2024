# TissueDetection2024
<a href="https://universe.roboflow.com/zshar/segmentation-tissue-detectionpt3">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a>

## Abstract
Ultrasounds are utilized in the medical field to visualize organ structures in the body. A physician
viewing ultrasound scans has to identify the contours of the structures and differences in the brightness
and texture of the tissue to further make interpretation of the image. YOLOv8 is a program that
can be used in a real-time image segmentation model, which when trained, can trace contours of
an object in an image. This study focuses on the development of a real-time segmentation model to
identify tissue in ultrasound images. Ultrasound images were obtained and spliced into frames, which
were manually annotated in Roboflow. Command Line Interface was used to train an extra large
segmentation model with YOLO. Training was conducted in three sessions, and showed improvement
of the model throughout training with lower loss, and increase in metrics. The best model was
obtained at the 86th epoch. Its mAP50-95 rating was 0.85115 and F1 Score was measured at 0.91 at
0.521 confidence. The model was precisely able to identify tissue in the 60 test images assessment
done manually. The model predicted images in 300 ms or less reliably. This study developed a
model that can be utilized in real-time clinical practice such as the automated demarcation of tissue
with three dimensional modeling scans, which was previously manually done. The application of
knowledge in ultrasound scans of in-vivo organ structures would be helpful in clinical practice.

## Greetings
Hello! My name is Zain Shariff, I am a freshman at Curtis Junior High School, and I am deeply excited to showcase my research that I have been working for a year. This year's project consists of the development of an image machine learning model that detects tissue present in ultrasound scans, and detects and trace contours of that tissue.

## How did you do this?
To obtain the images, I used a 3.5 MHz ultrasound as parsed it using a simple python program I had written on my local system. I imported the images onto Roboflow which were annotated. I exported the dataset and developed a YOLOv8 extra large segmentation model using [Ultralytics](https://github.com/ultralytics/ultralytics). This was done on a local system using Command Line Interface CLI.
I have gone more in-depth into the process in my paper.

## Where do I find what?
To find the images used for the dataset go into the dataset folder. The Roboflow Dataset can be found [here](https://universe.roboflow.com/zshar/segmentation-tissue-detectionpt3). For the parser code in python go to the the python file named "splicer.py". The model can be found as "best.pt".
My paper can be found in "paper.pdf" and my online slideshow can be found [here](https://docs.google.com/presentation/d/1RDuuYSYptCqnq6JYPsUbXoJ0kYnZSjMX2GxqWrOv4VA/edit?usp=sharing). If you would like to look at poster again in-depth, it can be found in "poster.pdf"

## License
[Tissue Detection in Ultrasound Images Using Real-Time Image Segmentation Model](https://github.com/zshariff6506/TissueDetection2024) © 2024 by Zain Shariff is licensed under CC BY-NC-SA 4.0
