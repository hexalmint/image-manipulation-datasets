from imds.casia import CASIA2
from imds.coverage import Coverage
from imds.defacto import CopyMove, Inpainting, Splicing
from imds.imd import IMD2020


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
