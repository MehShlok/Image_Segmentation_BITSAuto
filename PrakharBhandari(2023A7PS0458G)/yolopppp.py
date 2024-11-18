import torch

model = torch.hub.load("hustvl/yolop", "yolop", pretrained=True)

img = torch.randn(1, 3, 640, 640)
det_out, de_seg_out, ll_seg_out = model(img)

print(det_out)
print(type(det_out[0].shape()))
