# Glide-Text2Im Image Generation

This project demonstrates the generation of images using the Glide-Text2Im library. It leverages the CLIP model and diffusion models to generate high-quality images based on textual prompts.

## Installation

To run this project, you need to install the Glide-Text2Im library. Use the following command to install it:

```python
!pip install git+https://github.com/openai/glide-text2im
```

Additionally, ensure that you have the necessary dependencies installed, such as PIL, torch, and IPython.

## Usage

1. Import the required modules:
```python
from PIL import Image
from IPython.display import display
import torch as th
import torch.nn as nn
from glide_text2im.clip.model_creation import create_clip_model
from glide_text2im.download import load_checkpoint
from glide_text2im.model_creation import (
    create_model_and_diffusion,
    model_and_diffusion_defaults,
    model_and_diffusion_defaults_upsampler,
)
from glide_text2im.tokenizer.simple_tokenizer import SimpleTokenizer
```

2.Configure the device:
```python
has_cuda = th.cuda.is_available()
device = th.device('cpu' if not has_cuda else 'cuda')
print(device)
```
3.Load and set up the models:
```python
op = model_and_diffusion_defaults()
op['use_fp16'] = has_cuda
op['timestep_respacing'] = '100'
model, diffusion = create_model_and_diffusion(**op)
# ... Load and configure additional models ...
```

4.Load the CLIP model:
```python
clip_model = create_clip_model(device=device)
clip_model.image_encoder.load_state_dict(load_checkpoint('clip/image-enc', device))
clip_model.text_encoder.load_state_dict(load_checkpoint('clip/text-enc', device))
```
5.Define the sampling parameters:
```python
prompt = "Cat running"
batch_size = 1
guidance_scale = 3.0
upsample_temp = 0.997
```

6.Generate the image:
```python
tokenizer = SimpleTokenizer()
text = tokenizer.tokenize(prompt)
text = th.LongTensor(text).unsqueeze(0).to(device)
z = th.randn(batch_size, model.z_shape[0], device=device)
z = diffusion.p_mean_variance(model.model, z, clip_denoised=True, model_kwargs={'text': text})
z = z / z.norm(dim=-1, keepdim=True) * guidance_scale
z = z.to(device)
img = model.model(z, text=text, return_loss=False, upsample_temp=upsample_temp)
```

7.Display the image:
```python
img = img.clamp(-1, 1)
img = (img + 1) * 0.5
img = img.permute(0, 2, 3, 1)
img = img[0].cpu().numpy()
img = (img * 255).astype('uint8')
img = Image.fromarray(img)
display(img)
```

## Contributing
Padala Bala Siva Sai Megi Reddy Padala

## License
[MIT](https://choosealicense.com/licenses/mit/)



