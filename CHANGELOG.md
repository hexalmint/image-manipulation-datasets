# CHANGELOG

<!-- version list -->

## v1.1.0 (2025-07-02)

### Bug Fixes

- Change pad_value parameter type to float in _crop_or_pad
  ([`77e59a6`](https://github.com/srmlcn/imds/commit/77e59a652a33880f81de65f91ef53985ce37fb41))

- Change pad_value parameter type to float in crop_or_pad
  ([`524914c`](https://github.com/srmlcn/imds/commit/524914cbdd04e37d2ccfa364777194b7f1644de2))

- Enforce image_path and mask_path pairs align by index on the Coverage dataset
  ([`a9f5a63`](https://github.com/srmlcn/imds/commit/a9f5a639a00fee18822c5283e66ff958137375cc))

- Set the default crop_size parameter to None on the Defacto Splicing dataset
  ([`89ba672`](https://github.com/srmlcn/imds/commit/89ba672aec2ae395e29e47c903c9c5d789a6806a))

- Type hint the crop_size parameter to include Tuple and None
  ([`b918dbb`](https://github.com/srmlcn/imds/commit/b918dbb1803e1d34126f68b9e41d5f988e6dd36f))

- Type hint the crop_size parameter to include Tuple and None on the CASIA2 dataset
  ([`3246891`](https://github.com/srmlcn/imds/commit/324689184277280b6a06f9b516f402acc8820cc7))

- Type hint the crop_size parameter to include Tuple and None on the Coverage dataset
  ([`e371015`](https://github.com/srmlcn/imds/commit/e3710159adc2aed28fe46efd563f06de361b28fe))

- Type hint the crop_size parameter to include Tuple and None on the Defacto CopyMove dataset
  ([`96c1575`](https://github.com/srmlcn/imds/commit/96c15756f6cf421b19dc6dc81aff18127b7ac894))

- Type hint the crop_size parameter to include Tuple and None on the Defacto Inpainting dataset
  ([`dd968b7`](https://github.com/srmlcn/imds/commit/dd968b7ff4046b9303c7516090cd0be535c86581))

- Type hint the crop_size parameter to include Tuple and None on the Defacto Splicing dataset
  ([`6dd44d9`](https://github.com/srmlcn/imds/commit/6dd44d988e02fa6b75270cb8409c06cb707467ab))

- Type hint the crop_size parameter to include Tuple and None on the IMD2020 dataset
  ([`55dcd04`](https://github.com/srmlcn/imds/commit/55dcd04b02cf8cb34c8831d27d13d342dd5f8d23))

### Chores

- Add a test workflow that runs mypy in PRs
  ([`7a507d2`](https://github.com/srmlcn/imds/commit/7a507d2c3796200957608d14afebb1ebb2f93e4f))

- Add the py.typed marker file
  ([`f773467`](https://github.com/srmlcn/imds/commit/f77346734b18460c57ad4761699d96483640b9d8))

- Install mypy
  ([`3996e92`](https://github.com/srmlcn/imds/commit/3996e928b6c31c625fced5a53c874ee04d2bc3a0))

- Install types-pillow
  ([`381738c`](https://github.com/srmlcn/imds/commit/381738cd65c3e6f18f9731ca49378cfd4eba0ed9))

### Documentation

- Add the split parameter to the Coverage dataset docstring
  ([`8cf6a8c`](https://github.com/srmlcn/imds/commit/8cf6a8c7005af4b469de85589299027e6dd6e70a))

- Correct the shape parameter description in the crop_or_pad docstring
  ([`b63ce0d`](https://github.com/srmlcn/imds/commit/b63ce0dc2137d873a05f831c95c026b3a54d2130))

### Features

- Add a split parameter to the Coverage Dataset
  ([`18978c7`](https://github.com/srmlcn/imds/commit/18978c72e128c4be4263ea33259ec5f8ca6a9fbc))

- Add assertion statements for pad_value type narrowing in crop_or_pad
  ([`cd46581`](https://github.com/srmlcn/imds/commit/cd4658171ccc4a2032ff62c642430dfab4b07712))

- Convert _BaseDataset into an ABC
  ([`5d490b7`](https://github.com/srmlcn/imds/commit/5d490b7c6293d4ffb5572d37b3013c7031fee820))

- Convert the _BaseDataset image_files property into an abstract property
  ([`84bafb5`](https://github.com/srmlcn/imds/commit/84bafb531cc9333d946a3d00ff7890f2ba56554e))

- Convert the _BaseDataset mask_files property into an abstract property
  ([`cdc403d`](https://github.com/srmlcn/imds/commit/cdc403d77ed9c300f31bfa12c1013c9d6301c2af))

- Implement an all option to the mask_type parameter on the Coverage dataset
  ([`c47b05d`](https://github.com/srmlcn/imds/commit/c47b05d37534817c86d41862647776eeb871ab22))

- Implement the _BaseDataset image_files property for the CASIA2 dataset
  ([`eb07c46`](https://github.com/srmlcn/imds/commit/eb07c469e684ecdb328ab9d3febff63149bb2e56))

- Implement the _BaseDataset image_files property for the Coverage dataset
  ([`771cf60`](https://github.com/srmlcn/imds/commit/771cf600c2f96cefd2e988e9dccd22a09aeed903))

- Implement the _BaseDataset image_files property for the Defacto CopyMove dataset
  ([`7e50550`](https://github.com/srmlcn/imds/commit/7e505504ca1d9a497c36030a5e0ab5c4195e9169))

- Implement the _BaseDataset image_files property for the Defacto Inpainting dataset
  ([`9e71806`](https://github.com/srmlcn/imds/commit/9e71806cfed23399da0a27da487c6a9bc65ea3a2))

- Implement the _BaseDataset image_files property for the Defacto Splicing dataset
  ([`4a87708`](https://github.com/srmlcn/imds/commit/4a877080ffdd3f8c3852bf199b2ee06e6d68754d))

- Implement the _BaseDataset image_files property for the IMD2020 dataset
  ([`0f3fc98`](https://github.com/srmlcn/imds/commit/0f3fc988192e88d258e9e1060f0ca216691539d9))

- Implement the _BaseDataset mask_files property for the CASIA2 dataset
  ([`3a9900a`](https://github.com/srmlcn/imds/commit/3a9900a9e960d989debb1f2846115a652ff53c68))

- Implement the _BaseDataset mask_files property for the Coverage dataset
  ([`76124f4`](https://github.com/srmlcn/imds/commit/76124f486b1d8145fab1fc2235ab25b1d475f8ec))

- Implement the _BaseDataset mask_files property for the Defacto CopyMove dataset
  ([`27d3205`](https://github.com/srmlcn/imds/commit/27d32056ff60735e22fdcddf4d418e8aa00cad41))

- Implement the _BaseDataset mask_files property for the Defacto Inpainting dataset
  ([`7bcba4e`](https://github.com/srmlcn/imds/commit/7bcba4e2f6daba7a2eccbddc33d37a7d6fb74c10))

- Implement the _BaseDataset mask_files property for the Defacto Splicing dataset
  ([`a457415`](https://github.com/srmlcn/imds/commit/a4574154bd309710cf2be40d008b89b83646bd09))

- Implement the _BaseDataset mask_files property for the IMD2020 dataset
  ([`5710095`](https://github.com/srmlcn/imds/commit/57100951f817a168de868ef5e8554ce8bdb29fd7))

### Refactoring

- Add type hint to auth_files variable in __init__ on CASIA2
  ([`9e49d60`](https://github.com/srmlcn/imds/commit/9e49d60be50707e8521d42e58b13a62f20fc3a76))

- Add type hint to idx parameter of __getitem__ on _BaseDataset
  ([`7e8bc47`](https://github.com/srmlcn/imds/commit/7e8bc47958639d1e93c8d89ecb4bdcea5cd9a631))

- Add type hint to image_files variable in __init__ on IMD2020
  ([`0012496`](https://github.com/srmlcn/imds/commit/0012496ae135c198201097214eee9a0f908f4467))

- Add type hint to mask_files variable in __init__ on CASIA2
  ([`bcda63d`](https://github.com/srmlcn/imds/commit/bcda63d08f3e2abab64365bc61b34cba2a7d66d2))

- Add type hint to mask_files variable in __init__ on IMD2020
  ([`5b3df23`](https://github.com/srmlcn/imds/commit/5b3df23b5faf8fc8e7468b628e5f98e31f418eda))

- Add type hint to self._image_files variable in __init__ on CASIA2
  ([`e06d20d`](https://github.com/srmlcn/imds/commit/e06d20d3dd8058fedb7e749b479e7559a20db1ca))

- Add type hint to self._image_files variable in __init__ on Coverage
  ([`5584cf6`](https://github.com/srmlcn/imds/commit/5584cf6659f4d743cd3ce89d68de29658da49851))

- Add type hint to self._image_files variable in __init__ on Defacto CopyMove
  ([`185a0af`](https://github.com/srmlcn/imds/commit/185a0af6d23900a0f2381d666ed3cca0efe83353))

- Add type hint to self._image_files variable in __init__ on Defacto Inpainting
  ([`ff97537`](https://github.com/srmlcn/imds/commit/ff97537ae8c9df7964e8801391d45e9b053c1f16))

- Add type hint to self._image_files variable in __init__ on Defacto Splicing
  ([`fc5c94d`](https://github.com/srmlcn/imds/commit/fc5c94dbccea8996b762ac001d156a3ff1f797d3))

- Add type hint to self._image_files variable in __init__ on IMD2020
  ([`c15f9d4`](https://github.com/srmlcn/imds/commit/c15f9d449239ebad4aa9f3409f2991a0f4756b4c))

- Add type hint to self._mask_files variable in __init__ on CASIA2
  ([`2ca51f7`](https://github.com/srmlcn/imds/commit/2ca51f7cb3b41d25ba00f36922eb2218a763b53b))

- Add type hint to self._mask_files variable in __init__ on Coverage
  ([`18d1efc`](https://github.com/srmlcn/imds/commit/18d1efc96ce04d694ee9f479a3aa4bf32409a4d4))

- Add type hint to self._mask_files variable in __init__ on Defacto CopyMove
  ([`0a34bc9`](https://github.com/srmlcn/imds/commit/0a34bc9cf63b65f2351b36dd42ff944ed8f9fb44))

- Add type hint to self._mask_files variable in __init__ on Defacto Inpainting
  ([`ca43dd8`](https://github.com/srmlcn/imds/commit/ca43dd85883bc282cdf6d4c14c377a6811527d03))

- Add type hint to self._mask_files variable in __init__ on Defacto Splicing
  ([`e1be858`](https://github.com/srmlcn/imds/commit/e1be858b2753d287d1ab286ff45ed8ce249a72eb))

- Add type hint to self._mask_files variable in __init__ on IMD2020
  ([`acb13ab`](https://github.com/srmlcn/imds/commit/acb13ab0c016dca4c024ced08c0e3f5c9b914569))

- Add type hint to tamp_files variable in __init__ on CASIA2
  ([`b1e805e`](https://github.com/srmlcn/imds/commit/b1e805ebb440b2389cf3660c9b3d39c77f626cb6))

- Call _crop_or_pad with keyword arguments for signature safety
  ([`d18bd51`](https://github.com/srmlcn/imds/commit/d18bd5152a9868a2c13aab52765f746755033df9))

- Call crop_or_pad with keyword arguments for signature safety in __getitem__ on _BaseDataset
  ([`c6b068f`](https://github.com/srmlcn/imds/commit/c6b068f01f905bdcbbcd65c4ba5430868a662837))

- Change crop size type to use Optional instead of Union with None on _BaseDataset
  ([`26f7628`](https://github.com/srmlcn/imds/commit/26f7628778371eb706b5e54923e92c4ae31b50b8))

- Change crop size type to use Optional instead of Union with None on CASIA2
  ([`09e9494`](https://github.com/srmlcn/imds/commit/09e94943636060ef975a7a25d143b80d6ea546ad))

- Change crop size type to use Optional instead of Union with None on Coverage
  ([`4710de1`](https://github.com/srmlcn/imds/commit/4710de14bf7a4539f206c04a3b4da2f750344a1e))

- Change crop size type to use Optional instead of Union with None on Defacto CopyMove
  ([`f621a7a`](https://github.com/srmlcn/imds/commit/f621a7accaed6496cd95edf68cc55cde3cd97640))

- Change crop size type to use Optional instead of Union with None on Defacto Inpainting
  ([`3a2f3f8`](https://github.com/srmlcn/imds/commit/3a2f3f8501556f0844fd18d4abacadabfbff3166))

- Change crop size type to use Optional instead of Union with None on Defacto Splicing
  ([`dca23fe`](https://github.com/srmlcn/imds/commit/dca23fe039b6b0662efc4556a16bb9a3f35e2f6f))

- Change crop size type to use Optional instead of Union with None on IMD2020
  ([`d3166c9`](https://github.com/srmlcn/imds/commit/d3166c9e251963a43206b561322ee7afbbb9a207))

- Choose tampered files to remove dynamically in CASIA2
  ([`001f0c8`](https://github.com/srmlcn/imds/commit/001f0c8ce3f3b01182ba323822308e213ccfdb11))

- Modify type hint of remove_files to use List instead of list in __init__ on CASIA2
  ([`5a4defa`](https://github.com/srmlcn/imds/commit/5a4defa13115cfe33f01e1b7c88d398e19701a5a))

- Narrow ndarray types to all floats and ints in crop_or_pad
  ([`e105c88`](https://github.com/srmlcn/imds/commit/e105c883e0ff862e82a8a60b6eeb519936a0970c))

- Narrow the crop_start parameter type in _crop_or_pad
  ([`22f351d`](https://github.com/srmlcn/imds/commit/22f351d5a3d756024fbb4d55e9dfbc47e3bd3f39))

- Narrow the mask_type parameter to a Literal on the Coverage dataset
  ([`722f3db`](https://github.com/srmlcn/imds/commit/722f3db6ca69e49efc3ff670eba1dac01d60d709))

- Narrow the PyTorch Dataset parent class type in _BaseDataset
  ([`24398af`](https://github.com/srmlcn/imds/commit/24398afff0af61ae0c9c1e3b76326a71f11679f7))

- Narrow the shape parameter type in _crop_or_pad
  ([`10665dd`](https://github.com/srmlcn/imds/commit/10665ddfa6a31c4642cc793aa156d7ebca88b284))

- Narrow the shape parameter type in crop_or_pad
  ([`9ab33d0`](https://github.com/srmlcn/imds/commit/9ab33d0a570819d5ed9d251b4e84faaa91560ff3))

- Narrow the split parameter to a Literal on the CASIA2 dataset
  ([`3090848`](https://github.com/srmlcn/imds/commit/30908489e2bd4fe552479d18ae3b1e4d93ecc5c1))

- Narrow the split parameter to a Literal on the Defacto CopyMove dataset
  ([`b3b2284`](https://github.com/srmlcn/imds/commit/b3b228478a21a37fd43dfcd20b47e145efcf8659))

- Narrow the split parameter to a Literal on the Defacto Inpainting dataset
  ([`8e812d9`](https://github.com/srmlcn/imds/commit/8e812d9df56786ad55f1433d9aac75d36325b3bf))

- Narrow the split parameter to a Literal on the Defacto Splicing dataset
  ([`bae6886`](https://github.com/srmlcn/imds/commit/bae6886c7a671385ad44c04a52bb0e114b734227))

- Narrow the split parameter to a Literal on the IMD2020 dataset
  ([`b5af2fd`](https://github.com/srmlcn/imds/commit/b5af2fde35428df930a18fa4cde4a119a9c285a9))

- Rely on Image.size property to determine correctly typed crop_size in __getitem__ on _BaseDataset
  ([`ed0303b`](https://github.com/srmlcn/imds/commit/ed0303b5ccd1b79a0f55876a62372924491700a6))

- Remove variable reassignments where type becomes ambiguous in __getitem__ on _BaseDataset
  ([`f6c78fd`](https://github.com/srmlcn/imds/commit/f6c78fdc81ab05b49262f863141c3474f403c9c0))

- Rename crop_height and crop_width start with starting_ for clarity
  ([`2a6b413`](https://github.com/srmlcn/imds/commit/2a6b413fb00d2e099f3006a47e36676d8bfbb645))


## v1.0.1 (2025-07-02)

### Bug Fixes

- Remove the download parameter to the casia2 dataset
  ([`d354574`](https://github.com/srmlcn/imds/commit/d354574dc9946dbfad941de5d8ded222f69a669b))

- Remove the download parameter to the coverage dataset
  ([`5cd4b11`](https://github.com/srmlcn/imds/commit/5cd4b1138c9094261853b57b95dd417afbb0a0db))

- Remove the download parameter to the defacto copymove dataset
  ([`01633d3`](https://github.com/srmlcn/imds/commit/01633d3d3d8b2cd2979f3f82cfbe8abf00cfd7a0))

- Remove the download parameter to the defacto inpainting dataset
  ([`3290462`](https://github.com/srmlcn/imds/commit/3290462a4be4821d7040d5d3395869966e2c31d0))

- Remove the download parameter to the defacto splicing dataset
  ([`45895d1`](https://github.com/srmlcn/imds/commit/45895d18f0b2549fc79a158ebf6fe41639ef86b4))

- Remove the download parameter to the imd2020 dataset
  ([`f7e20c5`](https://github.com/srmlcn/imds/commit/f7e20c52f6cd889e1e8b84fb5f467bd18599ab7f))

### Documentation

- Remove the download parameter from the Common Parameters section
  ([`9056067`](https://github.com/srmlcn/imds/commit/90560677ac0c090d230d2311541f0ad995945d0e))

- Update the installation instructions to reflect pypi usage
  ([`35a89ea`](https://github.com/srmlcn/imds/commit/35a89eaeade815b752b3dbc4b9a53ef591dffad9))


## v1.0.0 (2025-07-02)

- Initial Release
