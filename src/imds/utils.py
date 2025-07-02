import random
from typing import List, Tuple, Union

import numpy as np
from numpy.typing import NDArray


ArrayDTypes = Union[
    np.float16,
    np.float32,
    np.float64,
    np.float80,
    np.float96,
    np.float128,
    np.float_,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.int128,
    np.int256,
    np.int_,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
    np.uint128,
    np.uint256,
    np.uint,
]


def crop_or_pad(
    arr: Union[
        List[NDArray[ArrayDTypes]],
        NDArray[ArrayDTypes],
    ],
    shape: Tuple[int, int],
    pad_value: Union[List[float], float] = 0,
) -> Union[
    List[NDArray[ArrayDTypes]],
    NDArray[ArrayDTypes],
]:
    """Crop or pad an array (or arrays) to a given shape. Note that if multiple arrays
    are passed, they must all have the same height and width.
    Args:
        arr (list | np.ndarray): Array to crop or pad with format [B, H, W, C] or [H, W, C].
        shape (tuple): Shape of the cropped or padded array with format [H, W].
        pad_value (list | float): Value to use for padding.
    Returns:
        Cropped or padded array with format [B, H, W, C] or [H, W, C].
    """
    if isinstance(arr, list):
        arr_h, arr_w = arr[0].shape[:2]
        for i in range(len(arr)):
            if len(arr[i].shape) == 2:
                arr[i] = np.expand_dims(arr[i], axis=2)

            assert arr[i].shape[:2] == (
                arr_h,
                arr_w,
            ), f"All arrays must have the same height and width. {arr[i].shape[:2]} != {(arr_h, arr_w)}"

        assert isinstance(
            pad_value, list
        ), "Pad value must be a list if multiple arrays are passed."

        assert len(arr) == len(
            pad_value
        ), "Number of arrays and number of pad values must match."

    elif isinstance(arr, np.ndarray):
        if len(arr.shape) == 2:
            arr = np.expand_dims(arr, axis=2)

        assert len(arr.shape) == 3, "Array must be of shape [H, W] or [H, W, C]."

        arr_h, arr_w = arr.shape[:2]

    else:
        raise ValueError("Invalid array type: {}".format(type(arr)))

    # This is used to determine the starting point of the crop.
    starting_crop_height = (random.randint(0, max(arr_h - shape[0], 0)) // 8) * 8
    starting_crop_width = (random.randint(0, max(arr_w - shape[1], 0)) // 8) * 8
    crop_start = (starting_crop_height, starting_crop_width)

    if isinstance(arr, list):
        assert isinstance(
            pad_value, list
        ), "Pad value must be a list if multiple arrays are passed."

        return [
            _crop_or_pad(arr=a, shape=shape, crop_start=crop_start, pad_value=pv)
            for a, pv in zip(arr, pad_value)
        ]

    elif isinstance(arr, np.ndarray):
        assert isinstance(
            pad_value, int
        ), "Pad value must be an integer if only one array is passed."

        return _crop_or_pad(
            arr=arr, shape=shape, crop_start=crop_start, pad_value=pad_value
        )


def _crop_or_pad(
    arr: NDArray[ArrayDTypes],
    shape: Tuple[int, int],
    crop_start: Tuple[int, int],
    pad_value: float = 0,
) -> NDArray[ArrayDTypes]:

    # Pad in the x-axis.
    if arr.shape[0] < shape[0]:
        arr = np.pad(
            arr,
            ((0, shape[0] - arr.shape[0]), (0, 0), (0, 0)),
            "constant",
            constant_values=(0, pad_value),
        )

    # Pad in the y-axis.
    if arr.shape[1] < shape[1]:
        arr = np.pad(
            arr,
            ((0, 0), (0, shape[1] - arr.shape[1]), (0, 0)),
            "constant",
            constant_values=(0, pad_value),
        )

    # Crop in both axes at the same time.
    if arr.shape[0] > shape[0] or arr.shape[1] > shape[1]:
        arr = arr[
            crop_start[0] : crop_start[0] + shape[0],
            crop_start[1] : crop_start[1] + shape[1],
            :,
        ]

    return arr
