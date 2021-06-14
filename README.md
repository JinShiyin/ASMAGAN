# ASMA-GAN
## Anisotropic Stroke Control for Multiple Artists Style Transfer
## Proceedings of the 28th ACM International Conference on Multimedia
**The official repository with Pytorch**

[[Arxiv paper]](https://arxiv.org/abs/2010.08175)

## Methodology
![Framework](/doc/img/framework.png)

## Results
<img src="./doc/img/1.png"  style="zoom: 20%;"/>
<img src="./doc/img/2.png"  style="zoom: 20%;"/>

<img src="./doc/img/3.png"  style="zoom: 20%;"/>
<img src="./doc/img/4.png"  style="zoom: 20%;"/>

<img src="./doc/img/5.png"  style="zoom: 20%;"/>
<img src="./doc/img/6.png"  style="zoom: 20%;"/>

<img src="./doc/img/7.png"  style="zoom: 20%;"/>
<img src="./doc/img/8.png"  style="zoom: 20%;"/>

<img src="./doc/img/9.png"  style="zoom: 20%;"/>
<img src="./doc/img/10.png"  style="zoom: 20%;"/>

<img src="./doc/img/11.png"  style="zoom: 20%;"/>
<img src="./doc/img/12.png"  style="zoom: 20%;"/>

<img src="./doc/img/13.png"  style="zoom: 12%;"/>
<img src="./doc/img/14.png"  style="zoom: 12%;"/>

## Video
<img src="./doc/img/video.webp"/>

**High-quality videos can be found in the link below:**

[[Google Drive link for video 1]](https://drive.google.com/file/d/1hdne7Gw39d34zt3w1NYV3Ln5cT8PfCNm/view?usp=sharing)

[[Google Drive link for video 2]](https://drive.google.com/file/d/1oftHAnLmgFis4XURcHTccGSWbWSXYKK1/view?usp=sharing)

[[Baidu Drive link for video]](https://pan.baidu.com/s/1WTS6jm2TY17bYJurw57LUg ) Password: ```b26n```

[[Online Video]](https://www.bilibili.com/video/BV12v411p7j5/)


## Dependencies
- python3.6+
- pytorch1.5+
- torchvision
- opencv
- pillow
- numpy


## Usage
### To test the pretrained model
```
python test_one_image.py --isTrain false  --name people --Arc_path arcface_model/arcface_checkpoint.tar --pic_a_path crop_224/6.jpg --pic_b_path crop_224/ds.jpg --output_path output/
```

--name refers to the SimSwap training logs name.

## Pretrained model

### Usage
There are two archive files in the drive: **checkpoints.zip** and **arcface_checkpoint.tar**

- **Copy the arcface_checkpoint.tar into ./arcface_model**
- **Unzip checkpoints.zip, place it in the root dir ./**

[[Google Drive]](https://drive.google.com/drive/folders/1jV6_0FIMPC53FZ2HzZNJZGMe55bbu17R?usp=sharing)

[[Baidu Drive]](https://pan.baidu.com/s/1wFV11RVZMHqd-ky4YpLdcA) Password: ```jd2v```


## To cite our paper
```
@inproceedings{DBLP:conf/mm/ChenYLQN20,
  author    = {Xuanhong Chen and
               Xirui Yan and
               Naiyuan Liu and
               Ting Qiu and
               Bingbing Ni},
  title     = {Anisotropic Stroke Control for Multiple Artists Style Transfer},
  booktitle = {{MM} '20: The 28th {ACM} International Conference on Multimedia, 2020},
  publisher = {{ACM}},
  year      = {2020},
  url       = {https://doi.org/10.1145/3394171.3413770},
  doi       = {10.1145/3394171.3413770},
  timestamp = {Thu, 15 Oct 2020 16:32:08 +0200},
  biburl    = {https://dblp.org/rec/conf/mm/ChenYLQN20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## Related Projects
Learn about our other projects [[RainNet]](https://neuralchen.github.io/RainNet), [[Sketch Generation]](https://github.com/TZYSJTU/Sketch-Generation-with-Drawing-Process-Guided-by-Vector-Flow-and-Grayscale), [[CooGAN]](https://github.com/neuralchen/CooGAN), [[Knowledge Style Transfer]](https://github.com/AceSix/Knowledge_Transfer), [[SimSwap]](https://github.com/neuralchen/SimSwap),[[ASMA-GAN]](https://github.com/neuralchen/ASMAGAN),[[Pretrained_VGG19]](https://github.com/neuralchen/Pretrained_VGG19).