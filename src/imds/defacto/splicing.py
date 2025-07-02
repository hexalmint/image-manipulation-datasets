import os
from typing import List, Optional, Tuple, Union

import numpy as np

from imds._dataset import _BaseDataset


class Splicing(_BaseDataset):
    """Digital image forensic has gained a lot of attention as it is becoming easier
    for anyone to make forged images. Several areas are concerned by image
    manipulation: a doctored image can increase the credibility of fake news, impostors
    can use morphed images to pretend being someone else.

    It became of critical importance to be able to recognize the manipulations suffered
    by the images. To do this, the first need is to be able to rely on reliable and
    controlled data sets representing the most characteristic cases encountered. The
    purpose of this work is to lay the foundations of a body of tests allowing both the
    qualification of automatic methods of authentication and detection of manipulations
    and the training of these methods.

    This dataset contains about 105000 splicing forgeries are available under the
    splicing directory. Each splicing is accompanied by two binary masks. One under the
    probemask subdirectory indicates the location of the forgery and one under the
    donormask indicates the location of the source. The external image can be found in
    the JSON file under the graph subdirectory.

    To download the dataset, please visit the following link:
    https://defactodataset.github.io

    Note: The dataset has an issue between the image and probe mask sizes. We must be
    careful in how the images and masks are handled. Since the images have manipulation
    statistics embedded in the pixels, any sort of aggregation function could damage or
    destroy the statistics. Therefore, we need to resize the masks to match the images.
    Then we need to crop the images and masks to the provided crop size. This will
    preserve any manipulation statistics while removing issues in the dataset.

    Directory structure:
    Defacto Splicing
    ├── splicing_1_annotations
    │   ├── donor_mask
    │   │   ├── 0_000000195755.tif
    │   │   ├── 1000_000000348782.tif
    │   │   ├── ...
    │   │   └── 9997_000000206363.tif
    │   ├── graph
    │   │   ├── 0_000000195755.json
    │   │   ├── 1000_000000348782.json
    │   │   ├── ...
    │   │   └── 9997_000000206363.json
    │   └── probe_mask
    │       ├── 0_000000195755.jpg
    │       ├── 1000_000000348782.jpg
    │       ├── ...
    │       └── 9997_000000206363.jpg
    ├── splicing_1_img
    │   └── img
    │       ├── 0_000000195755.tif
    │       ├── 1000_000000348782.tif
    │       ├── ...
    │       └── 9997_000000206363.tif
    ├── ...
    ├── splicing_7_annotations
    │   ├── donor_mask
    │   │   ├── 0_000000529545.tif
    │   │   ├── 100_000000343187.tif
    │   │   ├── ...
    │   │   └── 9999_000000476500.tif
    │   ├── graph
    │   │   ├── 0_000000529545.json
    │   │   ├── 100_000000343187.json
    │   │   ├── ...
    │   │   └── 9999_000000476500.json
    │   └── probe_mask
    │       ├── 0_000000529545.jpg
    │       ├── 100_000000343187.jpg
    │       ├── ...
    │       └── 9999_000000476500.jpg
    └── splicing_7_img
        └── img
            ├── 0_000000529545.tif
            ├── 100_000000343187.tif
            ├── ...
            └── 9999_000000476500.tif

    Args:
        data_dir (str): The directory of the dataset.
        split (str): The split of the dataset. Can be one of 'train', 'valid', 'test',
            'benchmark', and 'full'.
        crop_size (tuple): The size of the crop to be applied on the image and mask.
        pixel_range (tuple): The range of the pixel values of the input images.
            Ex. (0, 1) scales the pixels from [0, 255] to [0, 1].
        shuffle (bool): Whether to shuffle the dataset before splitting.
    """

    def __init__(
        self,
        data_dir: str,
        split: str = "full",
        crop_size: Union[Tuple[int, int], None] = None,
        pixel_range: Tuple[float, float] = (0.0, 1.0),
        shuffle: bool = True,
    ) -> None:
        super().__init__(crop_size, pixel_range)

        # Fetch the image filenames.
        image_dirs = [
            os.path.join(data_dir, f"splicing_{i}_img", "img") for i in range(1, 8)
        ]
        image_files = [
            os.path.abspath(os.path.join(shard, f))
            for shard in image_dirs
            for f in os.listdir(shard)
            if f.endswith("tif") or f.endswith("jpg")
        ]

        # Shuffle the image files for a random split.
        if shuffle:
            image_files = np.random.permutation(image_files).tolist()

        split_size = len(image_files) // 10

        if split == "train":
            self._image_files = image_files[: split_size * 8]

        elif split == "valid":
            self._image_files = image_files[split_size * 8 : split_size * 9]

        elif split == "test":
            self._image_files = image_files[split_size * 9 :]

        elif split == "benchmark":
            self._image_files = image_files[:1000]

        elif split == "full":
            self._image_files = image_files

        else:
            raise ValueError(f"Unknown split: {split}")

        # Fetch the mask files.
        mask_dirs = [
            os.path.join(data_dir, f"splicing_{i}_annotations", "probe_mask")
            for i in range(1, 8)
        ]

        self._mask_files = []
        for f in self._image_files:
            shard = f.split("/")[-3].split("_")[-2]
            f = f.split("/")[-1]
            mask_file = os.path.abspath(os.path.join(mask_dirs[int(shard) - 1], f))
            if not os.path.exists(mask_file) and mask_file[-3:] == "jpg":
                self._mask_files.append(mask_file.replace(".jpg", ".tif"))
            elif not os.path.exists(mask_file) and mask_file[-3:] == "tif":
                self._mask_files.append(mask_file.replace(".tif", ".jpg"))
            else:
                self._mask_files.append(mask_file)

    @property
    def image_files(self) -> List[str]:
        """Returns the list of image files in the dataset."""
        return self._image_files

    @property
    def mask_files(self) -> List[Optional[str]]:
        """Returns the list of mask files in the dataset."""
        return self._mask_files
