MS SCANNER v1.0
===============

Requirements:
- Termux (Android ARM64)
- Python 3.14

Install dependencies:
pkg install python clang x11-repo binutils
pkg install opencv-python python-numpy python-onnxruntime python-pillow
pip install aiohttp ddddocr cython setuptools

Run:
python run.py

Or shortcut:
ln -sf ~/ms-scanner-v1.0/run.py $PREFIX/bin/ms
ms

Developer: @andrew_ms_7
