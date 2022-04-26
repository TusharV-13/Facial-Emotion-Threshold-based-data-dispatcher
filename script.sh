pip3 install opencv-python
curl https://files.pythonhosted.org/packages/01/9b/be08992293fb21faf35ab98e06924d7407fcfca89d89c5de65442631556a/opencv-python-4.5.3.56.tar.gz > opencv.tar.gz
tar -xzvf opencv.tar.gz
cd opencv-python-4.5.3.56
python3 setup.py install
import cv2