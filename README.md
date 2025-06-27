# Image Manipulation Datasets

This python package contains torch dataset classes for common image manipulation datasets.

Currently, the supported datasets are:
- CASIA
    - CASIA 2.0
- Defacto
    - Copy/Move
    - Splicing
    - Inpainting
- Coverage
- IMD2020

## Install
```bash
pip install git+https://github.com/cainspencerm/image-manipulation-datasets.git@0.6
```

## Usage

All datasets are compatible with PyTorch's `torch.utils.data.DataLoader`. For examples on how to create and use datasets, see the examples section.

**Note:** Dataset constructors load the image and mask filepaths synchronously on initialization, opting to lazily load images and masks when accessed. 

## Examples

### Loading Datasets

#### CASIA 2.0

Ensure that the ground truth directory is in data_dir and named 'CASIA 2 Groundtruth'.

```python
from imds import casia

# Create dataset object for dataloader.
dataset = casia.Casia2(data_dir='data/CASIA2.0')  # optional split=['train', 'val', 'test', 'benchmark', 'full']
```

#### Defacto Copy/Move

```python
from imds import defacto

# Create dataset object for dataloader.
dataset = defacto.CopyMove(data_dir='data/copy-move')  # optional split=['train', 'val', 'test', 'benchmark', 'full']
```

#### Defacto Inpainting

```python
from imds import defacto

# Create dataset object for dataloader.
dataset = defacto.Inpainting(data_dir='data/inpainting')  # optional split=['train', 'val', 'test', 'benchmark', 'full']
```

#### Defacto Splicing

```python
from imds import defacto

# Create dataset object for dataloader.
dataset = defacto.Splicing(data_dir='data/splicing')  # optional split=['train', 'val', 'test', 'benchmark', 'full']
```

#### Coverage

```python
from imds import coverage

# Create dataset object for dataloader.
dataset = coverage.Coverage(data_dir='data/coverage')  # optional split=['train', 'val', 'test', 'benchmark', 'full']
```

#### IMD2020

```python
from imds import imd

# Create dataset object for dataloader.
dataset = imd.IMD2020(data_dir='data/IMD2020')  # optional split=['train', 'val', 'test', 'benchmark', 'full']
```

## Sample Quality

Datasets are not always perfect. Of the available datasets, COVERAGE, CASIA 2, and Defacto Splicing had images and masks that didn't match in size, though they have been verified as pairs. For this reason, the dataset classes resize the masks to the size of the original image, with the hopes that the masks line up correctly with the image. This is unverified as it would require manually verifying each of the over 110,000 image and mask pairs.
