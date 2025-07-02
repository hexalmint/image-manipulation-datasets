# Image Manipulation Datasets (IMDS)

This Python package provides PyTorch-compatible dataset classes for common image manipulation datasets used in digital forensics and deepfake detection research.

## Supported Datasets

- **CASIA 2.0** - Forgery classification dataset with 4,795 images
- **Defacto** - Collection of manipulation datasets:
  - Copy/Move (~19,000 forgeries)
  - Splicing (~105,000 forgeries) 
  - Inpainting (~25,000 forgeries)
- **Coverage** - Copy-move forgery database with similar genuine objects
- **IMD2020** - Real-life manipulated images from the Internet (2,010 images)

## Installation

```bash
pip install git+https://github.com/cainspencerm/image-manipulation-datasets.git@0.6
```

## Quick Start

```python
from imds import casia, defacto, coverage, imd
from torch.utils.data import DataLoader

# Load any dataset
dataset = casia.CASIA2(data_dir='data/CASIA2.0', split='train')
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

for images, masks in dataloader:
    # images: torch.Tensor shape (batch_size, 3, H, W)
    # masks: torch.Tensor shape (batch_size, 1, H, W) 
    pass
```

## Documentation

For comprehensive API documentation, usage examples, and advanced features, see:

**[📖 API Documentation](API_DOCUMENTATION.md)**

The documentation includes:
- Complete API reference for all dataset classes
- Usage examples and common patterns
- Directory structure requirements for each dataset
- Performance optimization tips
- Error handling guidelines

## Sample Quality

Datasets are not always perfect. Of the available datasets, COVERAGE, CASIA 2, and Defacto Splicing had images and masks that didn't match in size, though they have been verified as pairs. For this reason, the dataset classes resize the masks to the size of the original image, with the hopes that the masks line up correctly with the image. This is unverified as it would require manually verifying each of the over 110,000 image and mask pairs.
