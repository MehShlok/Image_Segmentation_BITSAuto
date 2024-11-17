{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOYAwOLGZug5mhj1bkQryua"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"7CLhCdYKh6BH"},"outputs":[],"source":["import torch\n","import torch.nn as nn\n","\n","from unet_parts import DoubleConv, DownSample, UpSample\n","\n","\n","class UNet(nn.Module):\n","    def __init__(self, in_channels, num_classes):\n","        super().__init__()\n","        self.down_convolution_1 = DownSample(in_channels, 64)\n","        self.down_convolution_2 = DownSample(64, 128)\n","        self.down_convolution_3 = DownSample(128, 256)\n","        self.down_convolution_4 = DownSample(256, 512)\n","\n","        self.bottle_neck = DoubleConv(512, 1024)\n","\n","        self.up_convolution_1 = UpSample(1024, 512)\n","        self.up_convolution_2 = UpSample(512, 256)\n","        self.up_convolution_3 = UpSample(256, 128)\n","        self.up_convolution_4 = UpSample(128, 64)\n","\n","        self.out = nn.Conv2d(in_channels=64, out_channels=num_classes, kernel_size=1)\n","\n","    def forward(self, x):\n","       down_1, p1 = self.down_convolution_1(x)\n","       down_2, p2 = self.down_convolution_2(p1)\n","       down_3, p3 = self.down_convolution_3(p2)\n","       down_4, p4 = self.down_convolution_4(p3)\n","\n","       b = self.bottle_neck(p4)\n","\n","       up_1 = self.up_convolution_1(b, down_4)\n","       up_2 = self.up_convolution_2(up_1, down_3)\n","       up_3 = self.up_convolution_3(up_2, down_2)\n","       up_4 = self.up_convolution_4(up_3, down_1)\n","\n","       out = self.out(up_4)\n","       return out"]}]}