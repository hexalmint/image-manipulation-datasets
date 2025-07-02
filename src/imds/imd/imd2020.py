import os
from typing import List, Literal, Optional, Tuple, Union

import numpy as np

from imds._dataset import _BaseDataset


class IMD2020(_BaseDataset):
    """This dataset contains 2,010 real-life manipulated images downloaded from the
    Internet. Corresponding real versions of these images are also provided. Moreover,
    there is a manually created binary mask localizing the manipulated area of each
    manipulated image.

    To download the dataset, please visit the following link:
    http://staff.utia.cas.cz/novozada/db/

    Directory structure:
    IMD2020
    ├── 1a1ogs
    │   ├── 1a1ogs_orig.jpg
    │   ├── c8tf5mq_0.png
    │   └── c8tf5mq_0_mask.png
    ├── 1a3oag
    │   ├── 1a3oag_orig.jpg
    │   ├── c8tt7fg_0.jpg
    │   ├── ...
    │   └── c8u0wl4_0_mask.png
    ├── ...
    └── z41
        ├── 00109_fake.jpg
        ├── 00109_fake_mask.png
        └── 00109_orig.jpg

    Args:
        data_dir (str): The directory of the dataset.
        split (str): The split of the dataset. Must be 'train', 'valid', 'test',
            'benchmark', or 'full'.
        crop_size (tuple): The size of the crop to be applied on the image and mask.
        pixel_range (tuple): The range of the pixel values of the input images.
            Ex. (0, 1) scales the pixels from [0, 255] to [0, 1].
        shuffle (bool): Whether to shuffle the dataset before splitting.
    """

    def __init__(
        self,
        data_dir: str,
        split: Literal["train", "valid", "test", "benchmark", "full"] = "full",
        crop_size: Union[Tuple[int, int], None] = None,
        pixel_range: Tuple[float, float] = (0.0, 1.0),
        shuffle: bool = True,
    ) -> None:
        super().__init__(crop_size, pixel_range)

        subdirs = [
            os.path.join(data_dir, subdir)
            for subdir in os.listdir(data_dir)
            if "." not in subdir
        ]

        # Fetch the authentic image filenames (they end in orig.jpg).
        image_files: List[str] = []
        mask_files = []
        for subdir in subdirs:
            for f in os.listdir(subdir):
                if "orig" in f:
                    image_files.append(os.path.abspath(os.path.join(subdir, f)))
                    mask_files.append(None)
                elif "mask" in f:
                    mask_file = os.path.abspath(os.path.join(subdir, f))
                    mask_files.append(mask_file)

                    # Locate the corresponding image file.
                    image_file = mask_file.replace("_mask", "")
                    if not os.path.exists(image_file):
                        image_file = image_file.replace(".png", ".jpg")
                        if not os.path.exists(image_file):
                            raise ValueError(
                                "Could not locate image for mask at {}".format(
                                    mask_file
                                )
                            )
                    image_files.append(image_file)

        # Shuffle the image files for a random split.
        if shuffle:
            p = np.random.permutation(np.arange(len(image_files)))
            image_files = np.array(image_files)[p].tolist()
            mask_files = np.array(mask_files)[p].tolist()

        # Split the filenames into use cases.
        split_size = len(image_files) // 10
        if split == "train":
            self._image_files: List[str] = image_files[: split_size * 8]
            self._mask_files: List[Union[str, None]] = mask_files[: split_size * 8]

        elif split == "valid":
            self._image_files = image_files[split_size * 8 : split_size * 9]
            self._mask_files = mask_files[split_size * 8 : split_size * 9]

        elif split == "test":
            self._image_files = image_files[split_size * 9 :]
            self._mask_files = mask_files[split_size * 9 :]

        elif split == "benchmark":
            self._image_files = image_files[:500]
            self._mask_files = mask_files[:500]

        elif split == "full":
            self._image_files = image_files
            self._mask_files = mask_files

        else:
            raise ValueError("Unknown split: " + split)

    @property
    def image_files(self) -> List[str]:
        """Returns the list of image files in the dataset."""
        return self._image_files

    @property
    def mask_files(self) -> List[Optional[str]]:
        """Returns the list of mask files in the dataset."""
        return self._mask_files
