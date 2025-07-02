from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Union

import numpy as np
import torch
from PIL import Image
from torch.utils import data

from imds import utils


class _BaseDataset(data.Dataset[Tuple[torch.Tensor, torch.Tensor]], ABC):
    def __init__(
        self,
        crop_size: Union[Tuple[int, int], None],
        pixel_range: Tuple[float, float],
        dtype: torch.dtype = torch.float32,
    ):
        super().__init__()

        self.crop_size = crop_size
        self.pixel_range = pixel_range
        self.data_type = dtype

    @property
    @abstractmethod
    def image_files(self) -> List[str]:
        """Returns the list of image files in the dataset."""
        ...

    @property
    @abstractmethod
    def mask_files(self) -> List[Optional[str]]:
        """Returns the list of mask files in the dataset."""
        ...

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        # Load the image file.
        image_file = self.image_files[idx]
        image = Image.open(image_file)

        # Force three color channels.
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Load the mask file.
        mask_file = self.mask_files[idx]
        pixel_min, pixel_max = self.pixel_range

        if mask_file is None:

            # The mask doesn't exist; assume it has no manipulated pixels.
            crop_size = self.crop_size if self.crop_size is not None else image.size
            mask_tensor = torch.zeros(crop_size, dtype=self.data_type).unsqueeze(dim=0)

            # Normalize the image.
            norm_image = np.array(image) * (pixel_max - pixel_min) / 255.0 + pixel_min

            # Crop or pad the image.
            crop_image = utils.crop_or_pad(
                arr=norm_image, shape=crop_size, pad_value=pixel_max
            )

            # Convert the image to a tensor.
            image_tensor = (
                torch.from_numpy(crop_image).to(self.data_type).permute(2, 0, 1)
            )

        else:

            # Load the mask.
            mask = Image.open(mask_file)

            # Force one color channel.
            if mask.mode != "L":
                mask = mask.convert("L")

            # Resize the mask to match the image.
            mask = mask.resize(image.size[:2])

            # Normalize the image and mask.
            norm_image = np.array(image) * (pixel_max - pixel_min) / 255.0 + pixel_min
            norm_mask = np.array(mask) / 255.0

            # Convert partially mixed pixel labels to manipulated pixel labels.
            norm_mask = (norm_mask > 0.0).astype(norm_mask.dtype)

            # Crop or pad the image and mask.
            crop_size = (
                self.crop_size if self.crop_size is not None else norm_image.shape[:2]
            )
            crop_image, crop_mask = utils.crop_or_pad(
                arr=[norm_image, norm_mask], shape=crop_size, pad_value=[pixel_max, 1.0]
            )

            # Convert the image and mask to tensors.
            image_tensor = (
                torch.from_numpy(crop_image).to(self.data_type).permute(2, 0, 1)
            )
            mask_tensor = (
                torch.from_numpy(crop_mask).to(self.data_type).permute(2, 0, 1)
            )

        return image_tensor, mask_tensor

    def __len__(self) -> int:
        return len(self.image_files)
