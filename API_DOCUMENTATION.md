# Image Manipulation Datasets (IMDS) - API Documentation

## Overview

The `imds` package provides PyTorch-compatible dataset classes for common image manipulation datasets used in digital forensics and deepfake detection research. All datasets are designed to work seamlessly with PyTorch's `torch.utils.data.DataLoader`.

## Installation

```bash
pip install git+https://github.com/cainspencerm/image-manipulation-datasets.git@0.6
```

## Core Components

### Base Dataset Class

All dataset classes inherit from the private `_BaseDataset` class, which provides common functionality for image and mask loading, preprocessing, and tensor conversion.

#### Common Parameters

All dataset classes share these common initialization parameters:

- **`data_dir`** (str): Path to the dataset directory
- **`split`** (str, optional): Dataset split to use. Options: `'train'`, `'valid'`, `'test'`, `'benchmark'`, `'full'`. Default: `'full'`
- **`crop_size`** (Tuple[int, int], optional): Size of crops to apply to images and masks. If `None`, uses original image size. Default: `None`
- **`pixel_range`** (Tuple[float, float], optional): Target pixel value range for normalization. Default: `(0.0, 1.0)`
- **`shuffle`** (bool, optional): Whether to shuffle the dataset before splitting. Default: `True`
- **`download`** (bool, optional): Whether to download the dataset (not implemented). Default: `False`

#### Common Methods

##### `__getitem__(idx: int) -> Tuple[torch.Tensor, torch.Tensor]`

Returns a tuple of (image, mask) tensors for the given index.

**Returns:**
- **image** (torch.Tensor): Shape `(C, H, W)` with pixel values in the specified `pixel_range`
- **mask** (torch.Tensor): Shape `(1, H, W)` with binary values `[0, 1]` indicating manipulated regions

##### `__len__() -> int`

Returns the total number of samples in the dataset.

## Dataset Classes

### CASIA 2.0

```python
from imds import casia

class CASIA2(_BaseDataset):
```

CASIA V2 dataset for forgery classification containing 4,795 images (1,701 authentic and 3,274 forged).

#### Directory Structure
```
CASIA 2.0/
├── Au/                    # Authentic images
│   ├── Au_ani_00001.jpg
│   └── ...
├── CASIA 2 Groundtruth/   # Ground truth masks
│   ├── *_gt.png
│   └── ...
└── Tp/                    # Tampered images
    ├── Tp_*.tif
    └── ...
```

#### Usage Example
```python
from imds import casia
from torch.utils.data import DataLoader

# Create dataset
dataset = casia.CASIA2(
    data_dir='data/CASIA2.0',
    split='train',
    crop_size=(256, 256),
    pixel_range=(0.0, 1.0)
)

# Use with DataLoader
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

for images, masks in dataloader:
    # images: (batch_size, 3, 256, 256)
    # masks: (batch_size, 1, 256, 256)
    pass
```

#### Download
Visit: https://github.com/namtpham/casia2groundtruth

---

### Coverage

```python
from imds import coverage

class Coverage(_BaseDataset):
```

The Copy-Move Forgery Database with Similar but Genuine Objects (COVERAGE) dataset containing copy-move forged images with corresponding originals.

#### Additional Parameters
- **`mask_type`** (str, optional): Type of mask to use. Options: `'forged'`, `'copy'`, `'paste'`. Default: `'forged'`

#### Directory Structure
```
COVERAGE/
├── image/
│   ├── 1.tif         # Original image
│   ├── 1t.tif        # Tampered image
│   └── ...
└── mask/
    ├── 1copy.tif     # Copy region mask
    ├── 1forged.tif   # Forged region mask
    ├── 1paste.tif    # Paste region mask
    └── ...
```

#### Usage Example
```python
from imds import coverage

# Create dataset with forged region masks
dataset = coverage.Coverage(
    data_dir='data/coverage',
    mask_type='forged',
    split='train'
)

# Create dataset with copy region masks
copy_dataset = coverage.Coverage(
    data_dir='data/coverage',
    mask_type='copy',
    split='test'
)
```

#### Download
Visit: https://github.com/wenbihan/coverage

---

### Defacto Datasets

The Defacto dataset collection includes three types of image manipulation datasets.

#### Defacto CopyMove

```python
from imds import defacto

class CopyMove(_BaseDataset):
```

Contains approximately 19,000 copy-move forgeries with binary masks indicating forgery locations and source regions.

#### Directory Structure
```
Defacto CopyMove/
├── copymove_annotations/
│   ├── donor_mask/        # Source region masks
│   │   ├── *.tif
│   │   └── ...
│   ├── graph/             # JSON metadata
│   │   ├── *.json
│   │   └── ...
│   └── probe_mask/        # Forgery region masks
│       ├── *.jpg
│       └── ...
└── copymove_img/
    └── img/
        ├── *.tif
        └── ...
```

#### Defacto Inpainting

```python
from imds import defacto

class Inpainting(_BaseDataset):
```

Contains approximately 25,000 object-removal forgeries with corresponding masks.

#### Directory Structure
```
Defacto Inpainting/
├── inpainting_annotations/
│   ├── graph/             # JSON metadata
│   ├── inpaint_mask/      # Inpainting masks
│   └── probe_mask/        # Forgery detection masks
└── inpainting_img/
    └── img/
        └── ...
```

#### Defacto Splicing

```python
from imds import defacto

class Splicing(_BaseDataset):
```

Contains approximately 105,000 splicing forgeries with binary masks and metadata about source images.

#### Directory Structure
```
Defacto Splicing/
├── splicing_1_annotations/
│   ├── donor_mask/        # Source region masks
│   ├── graph/             # JSON metadata
│   └── probe_mask/        # Forgery detection masks
├── splicing_1_img/
│   └── img/
├── ...
├── splicing_7_annotations/
└── splicing_7_img/
```

#### Usage Examples
```python
from imds import defacto

# Copy-move dataset
copymove_dataset = defacto.CopyMove(
    data_dir='data/copy-move',
    split='train',
    crop_size=(512, 512)
)

# Inpainting dataset
inpainting_dataset = defacto.Inpainting(
    data_dir='data/inpainting',
    split='valid'
)

# Splicing dataset
splicing_dataset = defacto.Splicing(
    data_dir='data/splicing',
    split='test',
    crop_size=(256, 256)
)
```

#### Download
Visit: https://defactodataset.github.io

---

### IMD2020

```python
from imds import imd

class IMD2020(_BaseDataset):
```

Contains 2,010 real-life manipulated images downloaded from the Internet with corresponding authentic versions and manually created binary masks.

#### Directory Structure
```
IMD2020/
├── 1a1ogs/
│   ├── 1a1ogs_orig.jpg       # Original image
│   ├── c8tf5mq_0.png         # Manipulated image
│   └── c8tf5mq_0_mask.png    # Manipulation mask
├── 1a3oag/
│   ├── 1a3oag_orig.jpg
│   ├── c8tt7fg_0.jpg
│   └── ...
└── ...
```

#### Usage Example
```python
from imds import imd

# Create dataset
dataset = imd.IMD2020(
    data_dir='data/IMD2020',
    split='benchmark',
    pixel_range=(-1.0, 1.0)  # Different normalization range
)

# Access samples
for image, mask in dataset:
    # image: torch.Tensor shape (3, H, W)
    # mask: torch.Tensor shape (1, H, W)
    print(f"Image shape: {image.shape}")
    print(f"Mask shape: {mask.shape}")
    break
```

#### Download
Visit: http://staff.utia.cas.cz/novozada/db/

## Utility Functions

### crop_or_pad

```python
from imds.utils import crop_or_pad

def crop_or_pad(
    arr: Union[List[np.ndarray], np.ndarray],
    shape: tuple,
    pad_value: Union[List[int], int] = 0
) -> Union[List[np.ndarray], np.ndarray]:
```

Crop or pad an array (or list of arrays) to a target shape. Used internally for image preprocessing.

#### Parameters
- **`arr`**: Input array(s) with format `[H, W, C]` or `[H, W]`
- **`shape`**: Target shape `(height, width)`
- **`pad_value`**: Value(s) to use for padding

#### Returns
- Cropped or padded array(s) matching the target shape

#### Usage Example
```python
import numpy as np
from imds.utils import crop_or_pad

# Single array
image = np.random.rand(100, 100, 3)
cropped_image = crop_or_pad(image, (256, 256), pad_value=0)

# Multiple arrays
image = np.random.rand(100, 100, 3)
mask = np.random.rand(100, 100, 1)
cropped_image, cropped_mask = crop_or_pad(
    [image, mask], 
    (256, 256), 
    pad_value=[0, 1]
)
```

## Common Usage Patterns

### Basic Dataset Loading

```python
from imds import casia, defacto, coverage, imd

# Load different datasets
datasets = {
    'casia': casia.CASIA2('data/CASIA2.0'),
    'copymove': defacto.CopyMove('data/copy-move'),
    'inpainting': defacto.Inpainting('data/inpainting'),
    'splicing': defacto.Splicing('data/splicing'),
    'coverage': coverage.Coverage('data/coverage'),
    'imd2020': imd.IMD2020('data/IMD2020')
}

for name, dataset in datasets.items():
    print(f"{name}: {len(dataset)} samples")
```

### Training/Validation/Test Splits

```python
from imds import casia
from torch.utils.data import DataLoader

# Create train/validation/test datasets
train_dataset = casia.CASIA2('data/CASIA2.0', split='train')
val_dataset = casia.CASIA2('data/CASIA2.0', split='valid')
test_dataset = casia.CASIA2('data/CASIA2.0', split='test')

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

print(f"Train: {len(train_dataset)} samples")
print(f"Validation: {len(val_dataset)} samples")
print(f"Test: {len(test_dataset)} samples")
```

### Custom Preprocessing

```python
from imds import defacto
import torchvision.transforms as transforms

# Create dataset with specific preprocessing
dataset = defacto.Splicing(
    data_dir='data/splicing',
    split='train',
    crop_size=(224, 224),
    pixel_range=(-1.0, 1.0)  # For models expecting [-1, 1] range
)

# Additional transforms can be applied after dataset loading
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=10)
])

# Apply transforms in training loop
for image, mask in dataset:
    # Apply transforms to image (mask might need separate handling)
    augmented_image = transform(image)
```

### Benchmark Evaluation

```python
from imds import casia, defacto, coverage, imd
from torch.utils.data import DataLoader

# Create benchmark datasets (fixed size for fair comparison)
benchmark_datasets = {
    'casia': casia.CASIA2('data/CASIA2.0', split='benchmark'),
    'defacto_cm': defacto.CopyMove('data/copy-move', split='benchmark'),
    'defacto_inp': defacto.Inpainting('data/inpainting', split='benchmark'),
    'defacto_spl': defacto.Splicing('data/splicing', split='benchmark'),
    'coverage': coverage.Coverage('data/coverage', split='benchmark'),
    'imd2020': imd.IMD2020('data/IMD2020', split='benchmark')
}

# Evaluate model on each benchmark
for name, dataset in benchmark_datasets.items():
    loader = DataLoader(dataset, batch_size=16, shuffle=False)
    print(f"Evaluating on {name}: {len(dataset)} samples")
    
    # Your evaluation code here
    # accuracy = evaluate_model(model, loader)
    # print(f"{name} accuracy: {accuracy:.3f}")
```

## Data Quality Notes

Some datasets have known issues:

1. **Size Mismatches**: COVERAGE, CASIA 2, and Defacto Splicing datasets may have images and masks with different sizes
2. **Automatic Resizing**: Masks are automatically resized to match image dimensions
3. **Preservation of Statistics**: The preprocessing pipeline is designed to preserve manipulation statistics in pixels

## Error Handling

```python
from imds import casia

try:
    dataset = casia.CASIA2('data/CASIA2.0')
    print(f"Dataset loaded successfully: {len(dataset)} samples")
except FileNotFoundError:
    print("Dataset directory not found")
except ValueError as e:
    print(f"Invalid dataset configuration: {e}")
```

## Performance Tips

1. **Use appropriate batch sizes**: Larger images require smaller batch sizes
2. **Consider crop_size**: Smaller crops improve memory usage and training speed
3. **Shuffle for training**: Always use `shuffle=True` for training splits
4. **Pin memory**: Use `pin_memory=True` in DataLoader for GPU training
5. **Number of workers**: Set `num_workers` in DataLoader for parallel loading

```python
from torch.utils.data import DataLoader

# Optimized DataLoader configuration
loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4,
    pin_memory=True,
    persistent_workers=True
)
```