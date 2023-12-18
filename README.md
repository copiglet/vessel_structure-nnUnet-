
# Vascular Structure Segmentation in Lung CT Scans

## Project Overview
This project focuses on developing a pipeline using nnU-Net for segmenting vascular structures from Ground Glass Opacities (GGO) and consolidation masks in lung CT scans. The primary goal is to enhance the precision of medical imaging analysis by effectively separating the vascular mask from these specific areas.

### Technologies Used
- **Programming Language**: Python
- **Libraries & Frameworks**: nnU-Net, PyTorch, TensorFlow, DICOM
- **Data Processing**: NumPy, Pandas, OpenCV
- **Others**: Git, Docker

## Background
The challenge in medical imaging, particularly in lung CT scans, is to accurately distinguish vascular structures from Ground Glass Opacities (GGO) and consolidation areas. This project aims to develop a model capable of effectively identifying and segmenting these structures.

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

## Images
Below are examples of the image data used in the project:

1. Vascular structure image file:
   ![Vascular Structure](vessel_img.png)

2. Final training dataset image with vascular mask separated:
   ![Training Dataset Image](image.png)

## Results and Applications
The results obtained from this pipeline are crucial for enhancing the accuracy of lung tissue analysis in CT scans. By effectively segmenting vascular structures from GGO and consolidation masks, the project contributes to improved diagnostic accuracy in clinical settings.

## Challenges and Solutions
Focus was placed on managing the complexity of high-resolution medical image data and developing strategies for efficient use of computing resources.

---

Feel free to modify or extend this README file as needed for your project.
