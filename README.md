# Transformer-NeRF

This project is based on the [PyTorch implementation](https://github.com/yenchenlin/nerf-pytorch) of [NeRF](http://www.matthewtancik.com/nerf) with key changes made to the neural network architecture. The primary alteration involves replacing the Multi-Layer Perceptron (MLP) with a transformer. More exactly, two new classes, NeRFTransformer and TransformerBlock, were added in the run_nerf_helpers.py file.

Here are some videos generated with the transformer-based NeRF:

<img src="https://drive.google.com/uc?export=download&id=1g9T9gB0Sg4DGRI6XwPCKgXD977cTODIk" width="350" height="250"/>
<img src="https://drive.google.com/uc?export=download&id=1rt1IGQP1cHjqMincggHzLyOOeXAF8qFl" width="350" height="250"/>
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
  
The LLFF data loader requires ImageMagick.

You will also need the [LLFF code](http://github.com/fyusion/llff) (and COLMAP) set up to compute poses if you want to run on your own real data.
  
</details>


### Quick Start

Download data for two example datasets: `lego` and `fern`
```
bash download_example_data.sh
```

### Training

To train a low-res `lego` NeRF:
```
python run_nerf.py --config configs/lego.txt
```

---

To train a low-res `fern` NeRF:
```
python run_nerf.py --config configs/fern.txt
```

---

### More Datasets
Other datasets can be downloaded from [here](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1). Place the downloaded dataset according to the following directory structure:
```
├── configs                                                                                                       
│   ├── ...                                                                                     
│                                                                                               
├── data                                                                                                                                                                                                       
│   ├── nerf_llff_data                                                                                                  
│   │   └── fern                                                                                                                             
│   │   └── flower  # downloaded llff dataset                                                                                  
│   │   └── horns   # downloaded llff dataset
|   |   └── ...
|   ├── nerf_synthetic
|   |   └── lego
|   |   └── ship    # downloaded synthetic dataset
|   |   └── ...
```

---

To train NeRF on different datasets: 

```
python run_nerf.py --config configs/{DATASET}.txt
```

replace `{DATASET}` with `trex` | `horns` | `flower` | `fortress` | `lego` | etc.

---

To test NeRF trained on different datasets: 

```
python run_nerf.py --config configs/{DATASET}.txt --render_only
```

replace `{DATASET}` with `trex` | `horns` | `flower` | `fortress` | `lego` | etc.


### Reproduce our results with our pre-trained models

Our pre-trained transformer-based NeRF models for the Lego, Flower, and Fern datasets can be downloaded from [here](https://drive.google.com/drive/folders/1YDTc_y1C9Iit4nbcsC234R7PvBu85Zgw?usp=sharing). Place the directories in `./logs` in order to test it later. See the following directory structure for an example:

```
├── logs 
│   ├── fern_test    # downloaded logs
│   ├── flower_test  # downloaded logs
│   ├── lego_test    # downloaded logs
```

Run 
```
python run_nerf.py --config configs/{DATASET}.txt --render_only
```

