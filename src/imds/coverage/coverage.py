import os
from typing import List, Literal, Optional, Tuple, Union

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
        split (str): The split of the dataset. Must be 'train', 'valid', 'test',
            'benchmark', or 'full'.
        pixel_range (tuple): The range of the pixel values of the input images.
            Ex. (0, 1) scales the pixels from [0, 255] to [0, 1].
        shuffle (bool): Whether to shuffle the dataset before splitting.
    """

    def __init__(
        self,
        data_dir: str,
        mask_type: Literal["forged", "copy", "paste", "all"] = "all",
        split: Literal["train", "valid", "test", "benchmark", "full"] = "full",
        crop_size: Union[Tuple[int, int], None] = None,
        pixel_range: Tuple[float, float] = (0.0, 1.0),
        shuffle: bool = True,
    ) -> None:
        super().__init__(crop_size, pixel_range)

        assert mask_type in [
            "forged",
            "copy",
            "paste",
            "all",
        ], f"Invalid mask type: {mask_type}. Must be one of 'forged', 'copy', 'paste', or 'all'."

        # Fetch the image filenames.
        image_dir = os.path.join(data_dir, "image")
        auth_image_paths: List[str] = []
        tamp_image_paths: List[str] = []
        for f in os.listdir(image_dir):
            fname, _ = os.path.splitext(f)
            abs_path = os.path.abspath(os.path.join(image_dir, f))
            if fname.endswith("t"):
                tamp_image_paths.append(abs_path)
            else:
                auth_image_paths.append(abs_path)

        # Create a mask type filter.
        if mask_type == "forged":
            _mask_types = ["forged"]
        elif mask_type == "copy":
            _mask_types = ["copy"]
        elif mask_type == "paste":
            _mask_types = ["paste"]
        elif mask_type == "all":
            _mask_types = ["forged", "copy", "paste"]

        # Fetch the mask filenames.
        mask_dir = os.path.abspath(os.path.join(data_dir, "mask"))
        tamp_mask_paths: List[str] = []
        for tamp_image_path in tamp_image_paths:
            image_name, image_ext = os.path.splitext(
                tamp_image_path.split(os.path.sep)[-1]
            )
            image_name = image_name[
                :-1
            ]  # Remove the 't' at the end of tampered images.
            for mt in _mask_types:
                mask_file = f"{image_name}{mt}{image_ext}"
                mask_file_path = os.path.abspath(os.path.join(mask_dir, mask_file))
                tamp_mask_paths.append(mask_file_path)

        # Increase the number of each tampered image to match the number of masks using that image.
        unique_tamp_image_paths = tamp_image_paths
        tamp_image_paths = []
        for tamp_mask_path in unique_tamp_image_paths:
            tamp_image_paths.extend([tamp_mask_path] * len(_mask_types))

        # Split the filenames into use cases.
        auth_split_size = len(auth_image_paths) // 10
        tamp_split_size = len(tamp_image_paths) // 10
        if split == "train":
            self._image_files = auth_image_paths[: auth_split_size * 8]
            self._mask_files = [None for _ in range((auth_split_size * 8))]

            self._image_files += tamp_image_paths[: tamp_split_size * 8]
            self._mask_files += tamp_mask_paths[: tamp_split_size * 8]

        elif split == "valid":
            self._image_files = auth_image_paths[
                auth_split_size * 8 : auth_split_size * 9
            ]
            self._mask_files = [None for _ in range(len(self._image_files))]

            self._image_files += tamp_image_paths[
                tamp_split_size * 8 : tamp_split_size * 9
            ]
            self._mask_files += tamp_mask_paths[
                tamp_split_size * 8 : tamp_split_size * 9
            ]

        elif split == "test":
            self._image_files = auth_image_paths[auth_split_size * 9 :]
            self._mask_files = [None for _ in range(len(self._image_files))]

            self._image_files += tamp_image_paths[tamp_split_size * 9 :]
            self._mask_files += tamp_mask_paths[tamp_split_size * 9 :]

        elif split == "benchmark":
            self._image_files = auth_image_paths[:5]
            self._mask_files = [None for _ in range(5)]

            self._image_files += tamp_image_paths[:5]
            self._mask_files += tamp_mask_paths[:5]

        elif split == "full":
            self._image_files = auth_image_paths + tamp_image_paths

            self._mask_files = [None for _ in range(len(auth_image_paths))]
            self._mask_files += tamp_mask_paths

        # Shuffle the image files for a random split.
        if shuffle:
            p = np.random.permutation(len(self._image_files))
            self._image_files = np.array(self._image_files)[p].tolist()
            self._mask_files = np.array(self._mask_files)[p].tolist()

    @property
    def image_files(self) -> List[str]:
        """Returns the list of image files in the dataset."""
        return self._image_files

    @property
    def mask_files(self) -> List[Optional[str]]:
        """Returns the list of mask files in the dataset."""
        return self._mask_files
