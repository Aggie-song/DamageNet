# DamageNet
DamageNet is a network architecture designed for multi-class damage recognition in concrete structures, aiming to overcome the limitations of traditional CNNs in capturing the complex visual features of cracks, exposed rebar, and spalling. It introduces a dual-branch encoder that combines convolutional and Transformer architectures in a hierarchical design, allowing both local and global features to be extracted at the same resolution. This structure enables the effective integration of local perception and global context. To further enhance feature fusion, a cross-domain coupling attention module is employed, facilitating complementary interactions between CNN and Transformer features. This improves the network’s ability to represent diverse and fine-grained damage characteristics. By leveraging cross-modal representation learning and refined feature integration, DamageNet enhances segmentation accuracy and demonstrates strong adaptability and generalization in complex damage detection scenarios.

# Dataset:
The DamageNet dataset focuses on detecting structural damage in buildings, including three target classes: crack, spalling, and exposed rebar. It follows a standard directory structure with separate **train**, **val**, and **test** folders under the **dataset** directory. Each of these contains **img** and **mask** subfolders, where **img** holds original `.jpg` images and **mask** contains corresponding `.png` masks. In the mask images, cracks, spalling, and exposed rebar are labeled with pixel values 1, 2, and 3 respectively, facilitating effective model training and recognition. Additionally, **train.txt** and **val.txt** files list the image and mask paths for the training and validation sets, supporting efficient data loading and processing.

dataset/
├── train/               
│   ├── img/              
│   │   ├── image1.jpg    
│   │   ├── image2.jpg    
│   │   └── ...          
│   └── mask/             
│       ├── mask1.png     
│       ├── mask2.png     
│       └── ...          
├── val/                  
│   ├── img/              
│   │   ├── val_image1.jpg
│   │   └── ...          
│   └── mask/             
│       ├── val_mask1.png 
│       └── ...          
├── test/                 
│   ├── img/              
│   │   ├── test_image1.jpg
│   │   └── ...          
│   └── mask/             
│       ├── test_mask1.png
│       └── ...          
├── train.txt             
└── val.txt               
