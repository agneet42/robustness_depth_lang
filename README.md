## "On the Robustness of Language Guidance for Low-Level Vision Tasks: Findings from Depth Estimation"

<p align="center">
    📃 <a href="https://agneetchatterjee.com/" target="_blank">Paper</a> |
    🎮 <a href="https://agneetchatterjee.com/" target="_blank">Project Website</a>
</p>

## 📄 Abstract
_Recent advances in monocular depth estimation have been made by incorporating natural language as additional guidance.  Although yielding impressive results, the impact of the language prior, particularly in terms of generalization and robustness, remains unexplored. In this paper, we address this gap by quantifying the impact of this prior and introduce methods to benchmark its effectiveness across various settings. We generate "low-level" sentences that convey object-centric,  three-dimensional spatial relationships, incorporate them as additional language priors and evaluate their downstream impact on depth estimation. Our key finding is that current language-guided depth estimators perform optimally only with scene-level descriptions and counter-intuitively fare worse with low level descriptions. Despite leveraging additional data, these methods are not robust to directed adversarial attacks and decline in performance with an increase in distribution shift. Finally, to provide a foundation for future research, we identify points of failures and offer insights to better understand these shortcomings. With an increasing number of methods using language for depth estimation, our findings highlight the opportunities and pitfalls that require careful consideration for effective deployment in real-world settings._

## 📚 Contents
- [Installation](#installation)
- [Data](#data)
- [Sample Scripts](#scripts)
- [Citing](#citing)
- [Acknowledgments](#ack)

<a name="installation"></a>
## 💾 Installation

Please follow the well-described instructions in [VPD](https://github.com/wl-zhao/VPD), to setup their codebase and download the NYUv2 dataset.

<a name="data"></a>
## 🖼️ Data

Refer to the [`data/`](./data) directory.

<a name="scripts"></a>
## 📊 Sample Scripts

Refer to the [`sample_scripts/`](./sample_scripts) directory.

<a name="citing"></a>
## 📜 Citing

```bibtex
@misc{chatterjee2024XYZ,
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