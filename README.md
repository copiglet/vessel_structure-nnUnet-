
# Vascular Structure Training Project

## Project Overview
This project focuses on the development of a training pipeline using nnU-Net to accurately segment and analyze vascular structures in medical images, particularly in lung scans. The primary objective is to enhance the precision in separating vascular structures from lung tissues.

### Technologies Used
- **Programming Language**: Python
- **Libraries & Frameworks**: nnU-Net, PyTorch, TensorFlow, DICOM
- **Data Processing**: NumPy, Pandas, OpenCV
- **Others**: Git, Docker

## Background
Improving the accuracy of distinguishing vascular structures from lung tissues in medical imaging analysis is a crucial challenge. This project aims to develop a model capable of effectively segmenting vascular structures in high-resolution 3D medical images.

## Pipeline Overview
The Jupyter notebook includes several key stages:
1. **Dataset Description Writing** (`write_dataset_descp` function)
   - Creation of the `dataset.json` file, defining the dataset details.
   - Includes dataset name, description, image size, references, labels, etc.

2. **nnU-Net Environment Setup**
   - Setting up environment variables like `nnUNet_raw`, `nnUNet_preprocessed`, `RESULTS_FOLDER` to specify paths for datasets and outputs.

3. **Data Conversion and Preprocessing**
   - Execution of data set conversion and preprocessing steps for nnU-Net.

## Model Training and Evaluation
Detailed information about the model training process, performance evaluation methods, and analysis of the results are covered in separate sections.

## Results and Applications
The results obtained from this pipeline play a vital role in enhancing the accuracy of lung tissue analysis and can significantly contribute to improved diagnostic accuracy in clinical settings.

## Challenges and Solutions
Focus was placed on managing the complexity of high-resolution medical image data and developing strategies for efficient use of computing resources.

---

Feel free to modify or extend this README file as needed for your project.
