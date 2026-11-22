import os
from torchvision import datasets, transforms

# Dataset root: <this project>/dogs_and_cats/dogs_and_cats
_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_ROOT = os.path.join(_BASE, "dogs_and_cats", "dogs_and_cats")


def get_transform(resize=(32, 32)):
    return transforms.Compose([transforms.Resize(resize), transforms.ToTensor()])


def get_dataset(name, split, transform=None):
    return datasets.ImageFolder(os.path.join(DATA_ROOT, split), transform=transform)
