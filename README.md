# Transformer-NeRF

This project is based on the [PyTorch implementation](https://github.com/yenchenlin/nerf-pytorch) of [NeRF](http://www.matthewtancik.com/nerf) with key changes made to the neural network architecture. The primary modification involves replacing the Multi-Layer Perceptron (MLP) with a transformer. More exactly, two new classes, **NeRFTransformer** and **TransformerBlock**, were added in the run_nerf_helpers.py file.

Here are some videos generated with the transformer-based NeRF:

<img src="https://drive.google.com/uc?export=download&id=1g9T9gB0Sg4DGRI6XwPCKgXD977cTODIk" width="350" height="250"/> <img src="https://drive.google.com/uc?export=download&id=1d8yjiPCTPTYR9KEAJlYjMeZAPM-1chuR" width="350" height="250"/>
<img src="https://drive.google.com/uc?export=download&id=1r51B7FvVX7Jb8W2j6nS_DnDvav3kyEPb" width="250" height="250"/>

## Installation

```
git clone https://github.com/orianapresacan/Transformer-NeRF.git
cd Transformer-NeRF
pip install -r requirements.txt
```

<details>
  <summary> Dependencies (click to expand) </summary>
  
  ## Dependencies
  - PyTorch 1.4
  - matplotlib
  - numpy
  - imageio
  - imageio-ffmpeg
  - configargparse
  
</details>

**PyTorch with CUDA Support**

This project requires PyTorch with CUDA support. Please ensure you have a CUDA-compatible version of PyTorch installed in your environment. 

**Memory Considerations**

This project's model was trained on an NVIDIA RTX 3090 GPU. This GPU has substantial memory capacity, which was needed to handle the computational demands and memory requirements of the training process. If you use a GPU with less memory than the RTX 3090 (24 GB), you may encounter memory limitations.


### Quick Start

Download the Flower, Fern, or Lego dataset from [here](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1). Place the downloaded dataset according to the following directory structure:
```                                                                                           
├── data                                                                                                                                                                                                       
│   ├── nerf_llff_data                                                                                                  
│   │   └── fern    # downloaded llff dataset                                                                                                        
│   │   └── flower  # downloaded llff dataset                                                                                  
|   |   └── ...
|   ├── nerf_synthetic
|   |   └── lego    # downloaded synthetic dataset
|   |   └── ...
```

### Generate videos with our pre-trained models

The pre-trained transformer-based NeRF models for the Lego, Flower, and Fern datasets can be downloaded from [here](https://drive.google.com/drive/folders/1YDTc_y1C9Iit4nbcsC234R7PvBu85Zgw?usp=sharing). Place the directories in `./logs` in order to test it. See the following directory structure for an example:

```
├── logs 
│   ├── fern_test    # downloaded logs
│   │    └── 200000.tar
│   ├── flower_test  # downloaded logs
│   │    └── 200000.tar
│   ├── lego_test    # downloaded logs
│   │    └── 200000.tar
```

Run 
```
python run_nerf.py --config configs/{DATASET}.txt --render_only
```

replace `{DATASET}` with `fern` | `flower` | `lego` | etc.

### Training

To train a low-res `lego` transformer-based NeRF:
```
python run_nerf.py --config configs/lego.txt
```

To train a low-res `fern` transformer-based NeRF:
```
python run_nerf.py --config configs/fern.txt
```

To train a low-res `flower` transformer-based NeRF:
```
python run_nerf.py --config configs/flower.txt
```
