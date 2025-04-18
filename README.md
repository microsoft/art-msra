<h1 align="center">ART: Anonymous Region Transformer for<br>Variable Multi-Layer Transparent Image Generation</h1>
<p align="center">
  <a href="https://arxiv.org/abs/2502.18364"><img src='https://img.shields.io/badge/arXiv-Paper-red?logo=arxiv&logoColor=white' alt='arXiv'></a>


<p align="center"><img src="assets/teaser.png" width="100%"></p>

<span style="font-size: 16px; font-weight: 600;">This repository supports [generating multi-layer transparent images](#multi-layer-generation) (constructed with multiple RGBA image layers) based on a global text prompt and an anonymous region layout (bounding boxes without layer captions). The anonymous region layout can be either [predicted by LLM](#llm-for-layout-planning) or manually specified by users.



<!-- Features -->
## 🌟 Features
- **Anonymous Layout**: Requires only a single global caption to generate multiple layers, eliminating the need for individual captions for each layer.
- **High Layer Capacity**: Supports the generation of 50+ layers, enabling complex multi-layer outputs.
- **Efficiency**: Maintains high efficiency compared to full attention and spatial-temporal attention mechanisms.


<!-- TODO List -->
## 🚧 TODO List
- [x] Release inference code and pretrained model
- [ ] Release training code


## Table of Contents
- [Multi Layer Generation](#multi-layer-generation)
  - [Environment Setup](#environment-setup)
  - [Testing](#testing-multi-layer-generation)
- [LLM For Layout Planning](#llm-for-layout-planning)
  - [Environment Setup](#environment)
  - [Data Format](#data-format)
  - [Inference](#inference)


## Multi Layer Generation

### Environment Setup

#### 1. Create Conda Environment
```bash
conda create -n multilayer python=3.10 -y
conda activate multilayer
```

#### 2. Install Dependencies 
```bash
pip3 install torch==2.4.0 torchvision==0.19.0
pip install diffusers==0.31.0 transformers==4.44.0 accelerate==0.34.2 peft==0.12.0 datasets==2.20.0
pip install wandb==0.17.7 einops==0.8.0 sentencepiece==0.2.0 mmengine==0.10.4 prodigyopt==1.0
```

#### 3. Login to Hugging Face
```bash
huggingface-cli login
```

### Quick Start
Use example.py to simply have a try:
```
python example.py
```

### Testing Multi-Layer-Generation

#### 1. Download Checkpoints

Create a path `multi_layer_gen/checkpoints` and download the following checkpoints into this path.

| Variable | Description | Action Required |
|----------|-------------|-----------------|
| `ckpt_dir` | Anonymous region transformer checkpoint | Download from [Google Drive](https://drive.google.com/drive/folders/1xKLCCCaI9QBWaJpS83XEgluhxD-gb-Yz?usp=sharing) |
| `transp_vae_ckpt` | Multi-layer transparency decoder checkpoint | Download from [Google Drive](https://drive.google.com/file/d/1_0erQNUp_LzZAyCiXApCKuIu4xlOo98n/view?usp=sharing) |
| `pre_fuse_lora_dir` | LoRA weights to be fused initially | Download from [Google Drive](https://drive.google.com/drive/folders/1y15r-GtizmbyE3u8J0isyqSJ17P_ZGro?usp=sharing) |
| `extra_lora_dir` | Optional LoRA weights (for aesthetic improvement) | Download from [Google Drive](https://drive.google.com/drive/folders/1_503hwaem7WEllVV-5olD5yi1UUiMCZm?usp=sharing) |

The downloaded checkpoints should be organized as follows:
```
checkpoints/
├── anonymous_region_transformer_ckpt/
│   ├── layer_pe.pth
│   └── pytorch_lora_weights.safetensors
├── extra_lora/
|   └── pytorch_lora_weights.safetensors
├── pre_fuse_lora/
|   └── pytorch_lora_weights.safetensors
└── transparent_decoder_ckpt.pt
```

#### 2. Run the testing Script
```bash
python multi_layer_gen/test.py \
--cfg_path=multi_layer_gen/configs/multi_layer_resolution512_test.py \
--save_dir=multi_layer_gen/output/ \
--ckpt_dir=multi_layer_gen/checkpoints/anonymous_region_transformer_ckpt \
--transp_vae_ckpt=multi_layer_gen/checkpoints/transparent_decoder_ckpt.pt \
--pre_fuse_lora_dir=multi_layer_gen/checkpoints/pre_fuse_lora \
--extra_lora_dir=multi_layer_gen/checkpoints/extra_lora
```

#### 3*. A notebook example 
Please see `test.ipynb`.


## LLM For Layout Planning

### Environment

#### 1. Create Conda Environment

```ba
conda create -n layoutplanner python=3.10 -y
conda activate layoutplanner
```

#### 2. Install Dependencies 
```ba
cd layout_planner
pip install -r requirements_part1.txt
pip install -r requirements_part2.txt
```

if encounter the following issues

- if meet `'ImportError: libGL.so.1: cannot open shared object file: No such file or directory'`

  ```bash
   apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install ffmpeg libsm6 libxext6  -y
  ```

- if need to add `flash-attn-2`

  ```bash
   pip install flash-attn --no-build-isolation
  ```
  or
  Get url from https://github.com/Dao-AILab/flash-attention/releases/
  ```bash
   pip install https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.3cxx11abiFALSE-cp310-cp310-linux_x86_64.whl
  ```



### Inference

#### 1. Configure Inference Script

Edit the following parameters in `scripts/inference_template.sh`:

| Variable           | Description                                             | Action Required                      |
|--------------------|---------------------------------------------------------|--------------------------------------|
| `input_model`      | Base model checkpoint location                          | Set to your downloaded model path ([Download here](https://huggingface.co/NousResearch/Meta-Llama-3-8B)) |
| `resume`           | Path to the trained layout planner checkpoint           | Set to your checkpoint path  ([Download here](https://cloud.tsinghua.edu.cn/d/08bf30ccf1c0462b86a6/))         |
| `width`            | Width of the layout for inference                       | Set the layout width for inference   |
| `height`           | Height of the layout for inference                      | Set the layout height for inference  |
| `save_path`        | Path to save the generated output JSON                  | Set your desired save path           |
| `do_sample`        | Whether to use `do_sample` for generation               | Set `True` for `do_sample`, `False` for greedy decoding |
| `temperature`      | Sampling temperature if `do_sample = True`              | Adjust as needed                     |
| `inference_caption`| User input describing the content of the desired layout | Provide the desired caption for layout generation |

#### 2. Run Inference

```bash
bash scripts/inference_template.sh
```
