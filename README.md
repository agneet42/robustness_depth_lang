Official PyTorch repo of "On the Robustness of Language Guidance for Low-Level Vision Tasks: Findings from Depth Estimation" [CVPR 2024]

**_Getting it Right: Improving Spatial Consistency in Text-to-Image Models_** by Agneet Chatterjee, Tejas Gokhale, Chitta Baral, Yezhou Yang.

<p align="center">
    📃 <a href="https://agneetchatterjee.com/" target="_blank">Paper</a> |
    🎮 <a href="https://agneetchatterjee.com/" target="_blank">Project Website</a>
</p>

## 📄 Abstract
_Recent advances in monocular depth estimation have been made by incorporating natural language as additional guidance.  Although yielding impressive results, the impact of the language prior, particularly in terms of generalization and robustness, remains unexplored. In this paper, we address this gap by quantifying the impact of this prior and introduce methods to benchmark its effectiveness across various settings. We generate "low-level" sentences that convey object-centric,  three-dimensional spatial relationships, incorporate them as additional language priors and evaluate their downstream impact on depth estimation. Our key finding is that current language-guided depth estimators perform optimally only with scene-level descriptions and counter-intuitively fare worse with low level descriptions. Despite leveraging additional data, these methods are not robust to directed adversarial attacks and decline in performance with an increase in distribution shift. Finally, to provide a foundation for future research, we identify points of failures and offer insights to better understand these shortcomings. With an increasing number of methods using language for depth estimation, our findings highlight the opportunities and pitfalls that require careful consideration for effective deployment in real-world settings._

## 📚 Contents
- [Installation](#installation)
- [Training](#training)
- [Inference](#inference)
- [The SPRIGHT Dataset](#the-spright-dataset)
- [Eval](#evaluation)
- [Citing](#citing)
- [Acknowledgments](#ack)

<a name="installation"></a>
## 💾 Installation

Make sure you have CUDA and PyTorch set up. The PyTorch [official documentation](https://pytorch.org/) is the best place to refer to for that. Rest of the installation instructions are provided in the respective sections. 

If you have access to the Habana Gaudi accelerators, you can benefit from them as our training script supports them.

<a name="training"></a>
## 🔍 Training

Refer to [`training/`](./training).

<a name="inference"></a>
## 🌺 Inference

```python
from diffusers import DiffusionPipeline
import torch 

spright_id = "SPRIGHT-T2I/spright-t2i-sd2"
pipe = DiffusionPipeline.from_pretrained(spright_id, torch_dtype=torch.float16).to("cuda")

image = pipe("A horse above a pizza").images[0]
image
```

You can also run [the demo](https://huggingface.co/spaces/SPRIGHT-T2I/SPRIGHT-T2I) locally:

```bash
git clone https://huggingface.co/spaces/SPRIGHT-T2I/SPRIGHT-T2I
cd SPRIGHT-T2I
python app.py
```

Make sure `gradio` and other dependencies are installed in your environment.

<a name="the-spright-dataset"></a>
## 🖼️ The SPRIGHT Dataset

Refer to our [paper](https://arxiv.org/abs/2404.01197) and [the dataset page](https://huggingface.co/datasets/SPRIGHT-T2I/spright) for more details. Below are some examples from the SPRIGHT dataset:

<p align="center">
<img src="assets/spright_good-1.png"/>
</p>

<a name="evaluation"></a>
## 📊 Evaluation

In the [`eval/`](./eval) directory, we provide details about the various evaluation methods we use in our work .

<a name="citing"></a>
## 📜 Citing

```bibtex
@misc{chatterjee2024getting,
      title={XYZ}, 
      author={XYZ},
      year={2024},
      eprint={XYZ},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

<a name="ack"></a>
## 🙏 Acknowledgments

The authors acknowledge resources and support from the Research Computing facilities at Arizona State University. This work was supported by NSF RI grants \#1750082 and \#2132724. The views and opinions of the authors expressed herein do not necessarily state or reflect those of the funding agencies and employers. 