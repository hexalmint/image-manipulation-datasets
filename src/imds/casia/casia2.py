import os
from typing import Tuple

import numpy as np

from imds._dataset import _BaseDataset


class CASIA2(_BaseDataset):
    """CASIA V2 is a dataset for forgery classification. It contains 4795 images, 1701 authentic and 3274 forged.

    To download the dataset, please visit the following link:
    https://github.com/namtpham/casia2groundtruth

    Directory structure:
    CASIA 2.0
    ├── Au
    │   ├── Au_ani_00001.jpg
    │   ├── Au_ani_00002.jpg
    │   ├── ...
    │   └── Au_txt_30029.jpg
    ├── CASIA 2 Groundtruth
    │   ├── Tp_D_CND_M_N_ani00018_sec00096_00138_gt.png
    │   ├── Tp_D_CND_M_N_art00076_art00077_10289_gt.png
    │   ├── ...
    │   └── Tp_S_NRN_S_O_sec00036_sec00036_00764_gt.png
    └── Tp
        ├── Tp_D_CND_M_N_ani00018_sec00096_00138.tif
        ├── Tp_D_CND_M_N_art00076_art00077_10289.tif
        ├── ...
        └── Tp_S_NRN_S_O_sec00036_sec00036_00764.tif

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
        split: str = "full",
        crop_size: Tuple[int, int] = None,
        pixel_range: Tuple[float, float] = (0.0, 1.0),
        shuffle: bool = True,
    ) -> None:
        super().__init__(crop_size, pixel_range)

        # Fetch the image filenames.
        authentic_dir = os.path.join(data_dir, "Au")
        auth_files = [
            os.path.abspath(os.path.join(authentic_dir, f))
            for f in os.listdir(authentic_dir)
            if f.endswith("tif") or f.endswith("jpg")
        ]

        tampered_dir = os.path.join(data_dir, "Tp")
        tamp_files = [
            os.path.abspath(os.path.join(tampered_dir, f))
            for f in os.listdir(tampered_dir)
            if f.endswith("tif") or f.endswith("jpg")
        ]

        # Ignore these files that have no ground truth masks.
        corrupted_files = [
            "Tp/Tp_D_NRD_S_N_cha10002_cha10001_20094.jpg",
            "Tp/Tp_S_NRD_S_N_arc20079_arc20079_01719.tif",
        ]

        remove_files = []
        for file in tamp_files:
            for f in corrupted_files:
                if f in file:
                    remove_files.append(file)

        for file in remove_files:
            tamp_files.remove(file)

        # Fetch the mask filenames.
        mask_dir = os.path.join(data_dir, "CASIA 2 Groundtruth")
        mask_files = [
            os.path.abspath(os.path.join(mask_dir, f))
            for f in os.listdir(mask_dir)
            if f.endswith(".tif") or f.endswith(".jpg") or f.endswith(".png")
        ]

        # Sort the mask files based on the tampered files.
        sorted_mask_files = []
        for file in tamp_files:
            tamp_id = file[-9:-4]
            mask = None
            for f in mask_files:
                if tamp_id + "_gt" == f[-12:-4]:
                    mask = f
                    break

            if mask is None and file.split("/")[-2] == "Tp":
                raise ValueError("No ground truth file found for image: " + file)

            mask_file = os.path.abspath(os.path.join(mask_dir, mask))
            sorted_mask_files.append(mask_file)

        mask_files = sorted_mask_files

        # Shuffle the image files for a random split.
        auth_files = np.random.permutation(auth_files).tolist()

        # Shuffle the tampered files in the same order as the masks.
        p = np.random.permutation(len(tamp_files))
        tamp_files = [tamp_files[i] for i in p]
        mask_files = [mask_files[i] for i in p]

        # Split the filenames into use cases.
        auth_split_size = len(auth_files) // 10
        tamp_split_size = len(tamp_files) // 10
        if split == "train":
            self._image_files = auth_files[: auth_split_size * 8]
            self.mask_files = [None for _ in range((auth_split_size * 8))]

            self._image_files += tamp_files[: tamp_split_size * 8]
            self.mask_files += mask_files[: tamp_split_size * 8]

        elif split == "valid":
            self._image_files = auth_files[auth_split_size * 8 : auth_split_size * 9]
            self.mask_files = [None for _ in range(len(self._image_files))]

            self._image_files += tamp_files[tamp_split_size * 8 : tamp_split_size * 9]
            self.mask_files += mask_files[tamp_split_size * 8 : tamp_split_size * 9]

        elif split == "test":
            self._image_files = auth_files[auth_split_size * 9 :]
            self.mask_files = [None for _ in range(len(self._image_files))]

            self._image_files += tamp_files[tamp_split_size * 9 :]
            self.mask_files += mask_files[tamp_split_size * 9 :]

        elif split == "benchmark":
            self._image_files = auth_files[:500]
            self.mask_files = [None for _ in range(500)]

            self._image_files += tamp_files[:500]
            self.mask_files += mask_files[:500]

        elif split == "full":
            self._image_files = auth_files + tamp_files

            self.mask_files = [None for _ in range(len(auth_files))]
            self.mask_files += mask_files

        else:
            raise ValueError("Unknown split: " + split)

        # Shuffle the image files to mix authentic and tampered images.
        if shuffle:
            p = np.random.permutation(len(self._image_files))
            self._image_files = [self._image_files[i] for i in p]
            self.mask_files = [self.mask_files[i] for i in p]

    @property
    def image_files(self) -> List[str]:
        """Returns the list of image files in the dataset."""
        return self._image_files
