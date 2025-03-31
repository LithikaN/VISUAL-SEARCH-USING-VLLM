# -*- coding: utf-8 -*-
import torch
import torchvision.models as models

# Load a pre-trained MobileNetV2 model
model = models.mobilenet_v2(pretrained=True)
model.eval()  # Set to evaluation mode

# Define dummy input (batch size 1, 3 color channels, 224x224 image size)
dummy_input = torch.randn(1, 3, 224, 224)

# Export the model to ONNX format
onnx_model_path = "mobilenet-v2.onnx"
torch.onnx.export(
    model, 
    dummy_input, 
    onnx_model_path, 
    export_params=True, 
    opset_version=11, 
    do_constant_folding=True, 
    input_names=['input'], 
    output_names=['output'], 
    dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
)

print(f"ONNX model saved as {onnx_model_path}")


