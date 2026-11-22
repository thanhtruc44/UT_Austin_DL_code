# Deep Learning Course

Tập hợp notebook và mã nguồn PyTorch được viết khi học môn Deep Learning, đi từ kiến thức nền tảng (tensor, hồi quy tuyến tính) đến mạng tích chập và Transformer.

## Nội dung

| Thư mục | Chủ đề |
|---|---|
| `Introduction/` | Tensor, phân phối xác suất, mô hình cơ bản |
| `First_example/` | Hồi quy tuyến tính, đồ thị tính toán, gradient descent, hàm mất mát, phân loại nhị phân và đa lớp |
| `Deep_network/` | Mạng sâu, SGD, quá trình huấn luyện (bài toán phân loại chó/mèo), thư viện nhỏ `utdl` |
| `Convolution/` | Tích chập, mạng tích chập, dilation và up-convolution |
| `Residuals_Normalizations/` | Kết nối residual và các kỹ thuật chuẩn hoá |
| `Making_it_work/` | Script huấn luyện hoàn chỉnh (`model.py`, `train.py`) |
| `Transformer/` | Positional embedding, Multi-Head Attention, kiến trúc Transformer, script huấn luyện |

Các file `*_notebook.ipynb` là bản bài tập, còn `*_extended.ipynb` là bản mở rộng.

## Cài đặt

Yêu cầu: Python 3.10 trở lên.

```bash
# 1. Clone repo
git clone https://github.com/thanhtruc44/UT_Austin_DL_code.git
cd UT_Austin_DL_code

# 2. Tạo môi trường ảo
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 3. Cài thư viện
pip install -r requirements.txt
```

Nếu có GPU NVIDIA, hãy cài PyTorch đúng phiên bản CUDA theo hướng dẫn tại <https://pytorch.org/get-started/locally/>.

## Dữ liệu

Dữ liệu **không** nằm trong repo vì dung lượng lớn. Hãy tải về và đặt đúng vị trí:

| Dữ liệu | Đặt tại | Dùng cho |
|---|---|---|
| Dogs and Cats | `Deep_network/dogs_and_cats/` (cấu trúc `dogs_and_cats/{train,test}/{cats,dogs}/`) | `Deep_network/` |
| Oxford 102 Flowers | `Introduction/flowers/flowers-102/` ([nguồn](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)) | `Introduction/` |

## Cách chạy

**Notebook:**

```bash
jupyter notebook
```

Mở notebook trong thư mục tương ứng. Với `Deep_network/`, hãy chạy từ thư mục này để import được `utdl`.

**Script huấn luyện:**

```bash
cd Making_it_work
python train.py

# Xem biểu đồ huấn luyện
tensorboard --logdir runs
```

`train.py` dùng thư viện `fire`, nên bạn có thể truyền tham số qua dòng lệnh, xem `python train.py --help`.

## Giấy phép

Chưa chọn giấy phép. Nếu muốn người khác được phép dùng lại, bạn có thể thêm file `LICENSE`, ví dụ MIT.
