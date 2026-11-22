# Deep Learning Course

A collection of PyTorch notebooks and source code written while studying a Deep Learning course. It starts from the fundamentals (tensors, linear regression) and works up to convolutional networks and Transformers.

## Contents

| Folder | Topic |
|---|---|
| `Introduction/` | Tensors, probability distributions, a basic model |
| `First_example/` | Linear regression, computation graphs, gradient descent, loss functions, binary and multi-class classification |
| `Deep_network/` | Deep networks, SGD, the training process (dogs vs. cats classification), and the small `utdl` helper package |
| `Convolution/` | Convolution, convolutional networks, dilation and up-convolution |
| `Residuals_Normalizations/` | Residual connections and normalization techniques |
| `Making_it_work/` | A complete training script (`model.py`, `train.py`) |
| `Transformer/` | Positional embeddings, Multi-Head Attention, the Transformer architecture, and training scripts |

Files named `*_notebook.ipynb` are the exercise versions, and `*_extended.ipynb` are the extended versions.

## Installation

Requirements: Python 3.10 or newer.

```bash
# 1. Clone the repository
git clone https://github.com/thanhtruc44/UT_Austin_DL_code.git
cd UT_Austin_DL_code

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt
```

If you have an NVIDIA GPU, install the PyTorch build that matches your CUDA version by following <https://pytorch.org/get-started/locally/>.

## Data

The datasets are **not** included in this repository because of their size. Download them and place them at the following locations:

| Dataset | Location | Used by |
|---|---|---|
| Dogs and Cats | `Deep_network/dogs_and_cats/` (layout: `dogs_and_cats/{train,test}/{cats,dogs}/`) | `Deep_network/` |
| Oxford 102 Flowers | `Introduction/flowers/flowers-102/` ([source](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)) | `Introduction/` |

## Usage

**Notebooks:**

```bash
jupyter notebook
```

Open a notebook in the corresponding folder. For `Deep_network/`, run Jupyter from that folder so that `utdl` can be imported.

**Training script:**

```bash
cd Making_it_work
python train.py

# View training curves
tensorboard --logdir runs
```

`train.py` uses the `fire` library, so arguments can be passed on the command line. Run `python train.py --help` to see the options.

## License

No license has been chosen yet. To let others reuse this code, consider adding a `LICENSE` file, for example MIT.
