import os
from typing import Tuple

import numpy as np

from imds._dataset import _BaseDataset
from imds.defacto import Splicing, CopyMove, Inpainting


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
        download (bool): Whether to download the dataset.
    """

    def __init__(
        self,
        data_dir: str,
        mask_type: str = "forged",
        crop_size: Tuple[int, int] = None,
        pixel_range: Tuple[float, float] = (0.0, 1.0),
        shuffle: bool = True,
        download: bool = False,
    ) -> None:
        super().__init__(crop_size, pixel_range)

        assert mask_type in ["forged", "copy", "paste"]

        if download:
            raise NotImplementedError(
                "Downloading is not implemented yet due to the requirement of a "
                "browser to obtain the dataset. Please refer to the following link "
                "for more information: https://github.com/wenbihan/coverage."
            )

        # Fetch the image filenames.
        image_dir = os.path.join(data_dir, "image")
        self.image_files = [
            os.path.abspath(os.path.join(image_dir, f))
            for f in os.listdir(image_dir)
            if f.endswith("tif") or f.endswith("jpg")
        ]

        # Shuffle the image files for a random split.
        if shuffle:
            self.image_files = np.random.permutation(self.image_files).tolist()

        # Fetch the mask filenames in the correct order.
        mask_dir = os.path.abspath(os.path.join(data_dir, "mask"))
        mask_files = [
            os.path.abspath(os.path.join(mask_dir, f))
            for f in os.listdir(mask_dir)
            if ".tif" in f
        ]
        self.mask_files = []
        for f in self.image_files:
            f_name = f.split(".")[0]
            if f_name[-1] == "t":
                mask_file = f_name.split("/")[-1][:-1] + mask_type + ".tif"
                mask_file = os.path.abspath(os.path.join(mask_dir, mask_file))
                assert mask_file in mask_files
            else:
                mask_file = None

            self.mask_files.append(mask_file)


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
        download (bool): Whether to download the dataset.
    """

    def __init__(
        self,
        data_dir: str,
        split: str = "full",
        crop_size: Tuple[int, int] = None,
        pixel_range: Tuple[float, float] = (0.0, 1.0),
        shuffle: bool = True,
        download: bool = False,
    ) -> None:
        super().__init__(crop_size, pixel_range)

        if download:
            raise NotImplementedError(
                "Downloading is not implemented yet due to the requirement of a "
                "browser to obtain the dataset. Please refer to the following link "
                "for more information: http://staff.utia.cas.cz/novozada/db/."
            )

        subdirs = [
            os.path.join(data_dir, subdir)
            for subdir in os.listdir(data_dir)
            if "." not in subdir
        ]

        # Fetch the authentic image filenames (they end in orig.jpg).
        image_files, mask_files = [], []
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
            self.image_files = image_files[: split_size * 8]
            self.mask_files = mask_files[: split_size * 8]

        elif split == "valid":
            self.image_files = image_files[split_size * 8 : split_size * 9]
            self.mask_files = mask_files[split_size * 8 : split_size * 9]

        elif split == "test":
            self.image_files = image_files[split_size * 9 :]
            self.mask_files = mask_files[split_size * 9 :]

        elif split == "benchmark":
            self.image_files = image_files[:500]
            self.mask_files = mask_files[:500]

        elif split == "full":
            self.image_files = image_files
            self.mask_files = mask_files

        else:
            raise ValueError("Unknown split: " + split)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Defacto dataset loader")
    parser.add_argument(
        "--copy-move-data-dir",
        type=str,
        default=None,
        help="Path to the CopyMove dataset directory.",
    )
    parser.add_argument(
        "--inpainting-data-dir",
        type=str,
        default=None,
        help="Path to the Inpainting dataset directory.",
    )
    parser.add_argument(
        "--splicing-data-dir",
        type=str,
        default=None,
        help="Path to the Splicing dataset directory.",
    )
    parser.add_argument(
        "--casia2-data-dir",
        type=str,
        default=None,
        help="Path to the CASIA2 dataset directory.",
    )
    parser.add_argument(
        "--coverage-data-dir",
        type=str,
        default=None,
        help="Path to the Coverage dataset directory.",
    )
    parser.add_argument(
        "--imd2020-data-dir",
        type=str,
        default=None,
        help="Path to the IMD2020 dataset directory.",
    )
    args = parser.parse_args()

    if (
        args.copy_move_data_dir is None
        and args.inpainting_data_dir is None
        and args.splicing_data_dir is None
        and args.casia2_data_dir is None
        and args.coverage_data_dir is None
        and args.imd2020_data_dir is None
    ):
        parser.error("At least one dataset directory must be specified.")

    if args.splicing_data_dir is not None:
        dataset = Splicing(data_dir=args.splicing_data_dir, split="valid")
        for image, mask in dataset:
            print("Sample:", image.size(), mask.size())
            break
        print("Number of samples:", len(dataset))

    if args.copy_move_data_dir is not None:
        dataset = CopyMove(data_dir=args.copy_move_data_dir, split="valid")
        for image, mask in dataset:
            print("Sample:", image.size(), mask.size())
            break
        print("Number of samples:", len(dataset))

    if args.inpainting_data_dir is not None:
        dataset = Inpainting(data_dir=args.inpainting_data_dir, split="valid")
        for image, mask in dataset:
            print("Sample:", image.size(), mask.size())
            break
        print("Number of samples:", len(dataset))

    if args.casia2_data_dir is not None:
        dataset = CASIA2(data_dir=args.casia2_data_dir, split="valid")
        for image, mask in dataset:
            print("Sample:", image.size(), mask.size())
            break
        print("Number of samples:", len(dataset))

    if args.coverage_data_dir is not None:
        dataset = Coverage(data_dir=args.coverage_data_dir)
        for image, mask in dataset:
            print("Sample:", image.size(), mask.size())
            break
        print("Number of samples:", len(dataset))

    if args.imd2020_data_dir is not None:
        dataset = IMD2020(data_dir=args.imd2020_data_dir, split="valid")
        for image, mask in dataset:
            print("Sample:", image.size(), mask.size())
            break
        print("Number of samples:", len(dataset))


if __name__ == "__main__":
    main()
