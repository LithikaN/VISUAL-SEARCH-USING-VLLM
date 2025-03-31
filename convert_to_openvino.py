import openvino as ov

# Define input and output paths
onnx_model_path = "mobilenet-v2.onnx"
ir_model_path = "mobilenet-v2-pytorch.xml"

# Convert ONNX model to OpenVINO IR format
ov_model = ov.convert_model(onnx_model_path)

# Save the converted model
ov.save_model(ov_model, ir_model_path)

print(f"OpenVINO model saved as {ir_model_path} and mobilenet-v2-pytorch.bin")


