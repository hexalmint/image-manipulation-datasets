import os
from typing import List, Optional, Literal, Tuple, Union

import numpy as np

from imds._dataset import _BaseDataset


class Coverage(_BaseDataset):
    """The Copy-Move Forgery Database with Similar but Genuine Objects (COVERAGE)
    accompanies the following publication: "COVERAGE--A NOVEL DATABASE FOR COPY-MOVE
    FORGERY DETECTION," IEEE International Conference on Image processing (ICIP), 2016.

    COVERAGE contains copymove forged (CMFD) images and their originals with similar but
    genuine objects (SGOs). COVERAGE is designed to highlight and address tamper
    detection ambiguity of popular methods, caused by self-similarity within natural
    images. In COVERAGE, forged-original pairs are annotated with (i) the duplicated and
    forged region masks, and (ii) the tampering factor/similarity metric. For
    benchmarking, forgery quality is evaluated using (i) computer vision-based methods,
    and (ii) human detection performance.

    To download the dataset, please visit the following link:
    https://github.com/wenbihan/coverage

    Directory structure:
    COVERAGE
    ├── image
    │   ├── 1.tif
    │   ├── 1t.tif
    │   ├── ...
    │   ├── 100.tif
    │   └── 100t.tif
    ├── label
    │   ├── ...  # Not implemented.
    ├── mask
    │   ├── 1copy.tif
    │   ├── 1forged.tif
    │   ├── 1paste.tif
    │   ├── ...
    │   ├── 100copy.tif
    │   ├── 100forged.tif
    │   └── 100paste.tif
    └── readme.txt

    Args:
        data_dir (str): The directory of the dataset.
        mask_type (str): The type of mask to use. Must be 'forged', 'copy', or 'paste'.
        crop_size (tuple): The size of the crop to be applied on the image and mask.
        pixel_range (tuple): The range of the pixel values of the input images.
            Ex. (0, 1) scales the pixels from [0, 255] to [0, 1].
        shuffle (bool): Whether to shuffle the dataset before splitting.
    """

    def __init__(
        self,
        data_dir: str,
        mask_type: Literal["forged", "copy", "paste"] = "forged",
        crop_size: Union[Tuple[int, int], None] = None,
        pixel_range: Tuple[float, float] = (0.0, 1.0),
        shuffle: bool = True,
    ) -> None:
        super().__init__(crop_size, pixel_range)

        assert mask_type in ["forged", "copy", "paste"]

        # Fetch the image filenames.
        image_dir = os.path.join(data_dir, "image")
        self._image_files = [
            os.path.abspath(os.path.join(image_dir, f))
            for f in os.listdir(image_dir)
            if f.endswith("tif") or f.endswith("jpg")
        ]

        # Shuffle the image files for a random split.
        if shuffle:
            self._image_files = np.random.permutation(self.image_files).tolist()

        # Fetch the mask filenames in the correct order.
        mask_dir = os.path.abspath(os.path.join(data_dir, "mask"))
        mask_files = [
            os.path.abspath(os.path.join(mask_dir, f))
            for f in os.listdir(mask_dir)
            if ".tif" in f
        ]
        self._mask_files = []
        for f in self.image_files:
            f_name = f.split(".")[0]
            if f_name[-1] == "t":
                mask_file = f_name.split("/")[-1][:-1] + mask_type + ".tif"
                mask_file = os.path.abspath(os.path.join(mask_dir, mask_file))
                assert mask_file in mask_files
            else:
                mask_file = None

            self._mask_files.append(mask_file)

    @property
    def image_files(self) -> List[str]:
        """Returns the list of image files in the dataset."""
        return self._image_files

    @property
    def mask_files(self) -> List[Optional[str]]:
        """Returns the list of mask files in the dataset."""
        return self._mask_files
