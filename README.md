# TissueDetection2024
<a href="https://universe.roboflow.com/zshar/segmentation-tissue-detectionpt3">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>
</a>


## Greetings
Hello! My name is Zain Shariff, I am a freshman at Curtis Junior High School, and I am deeply excited to showcase my research that I have been working for a year. This year's project consists of the development of an image machine learning model that detects tissue present in ultrasound scans, and detects and trace contours of that tissue.

## How did you do this?
To obtain the images, I used a 3.5 MHz ultrasound as parsed it using a simple python program I had written on my local system. I imported the images onto Roboflow which were annotated. I exported the dataset and developed a YOLOv8 extra large segmentation model using [Ultralytics](https://github.com/ultralytics/ultralytics). This was done on a local system using Command Line Interface CLI.
I have gone more in-depth into the process in my paper.

## Where do I find what?
To find the images used for the dataset go into the dataset folder. The Roboflow Dataset can be found [here](https://universe.roboflow.com/zshar/segmentation-tissue-detectionpt3). For the parser code in python go to the the python file named "parser.py". The model can be found as "best.pt".
My paper can be found in "paper.pdf" and my online slideshow can be found [here](https://docs.google.com/presentation/d/1RDuuYSYptCqnq6JYPsUbXoJ0kYnZSjMX2GxqWrOv4VA/edit?usp=sharing). If you would like to look at poster again in-depth, it can be found in "poster.pdf"

## License
[Tissue Detection in Ultrasound Images Using Real-Time Image Segmentation Model](https://github.com/zshariff6506/TissueDetection2024) © 2024 by Zain Shariff is licensed under CC BY-NC-SA 4.0
