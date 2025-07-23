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

## 🛑 Important Notice (updated 2025/07/23)

This repository previously contained code and pretrained model weights for generating multi-layer transparent images using a global text prompt and anonymous region layout. However, because the model was trained on data later determined to be illegally sourced, we have removed the model weights and inference checkpoints from this repository, along with all associated download links. If you have any questions, please contact the original authors through official channels.

As a result:

- The pretrained models and associated checkpoints are no longer available for download.
- No runnable or usable code for inference or training is provided.
- We do not provide any means to use or reproduce the model at this time.
- The training code, which relied on this data, has also been removed.



