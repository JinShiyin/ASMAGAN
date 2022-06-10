'''
Description: 
Author: JinShiyin
Email: shiyinjin@foxmail.com
Date: 2022-02-18 21:46:19
'''

import os
import shutil


artist_name_list = [
    'paul-cezanne',
    'nicholas-roerich',
    'claude-monet',
    'vincent-van-gogh',
    'pablo-picasso',
    'edvard-munch',
    'samuel-peploe',
    'wassily-kandinsky', #
    'ernst-ludwig-kirchner',
    'berthe-morisot',
    'jackson-pollock',
]

our_name_list = [
    'cezanne',
    'roerich',
    'monet',
    'vangogh',
    'picasso',
    'munch',
    'peploe',
    'kandinsky',
    'kirchner',
    'morisot',
    'pollock'
]

img_root = 'test_logs/ASMAfinal/picked-test-images-results-for-fid-sorted-by-artist'
out_dir = 'test_logs/ASMAfinal/results_for_deception_rate'

for i in range(len(our_name_list)):
    our_name = our_name_list[i]
    artist_name = artist_name_list[i]
    img_dir = os.path.join(img_root, our_name)
    img_name_list = os.listdir(img_dir)
    for img_name in img_name_list:
        ori_img_path = os.path.join(img_dir, img_name)
        img_basename = os.path.splitext(img_name)[0]
        dst_path = os.path.join(out_dir, f'{img_basename}_stylized_{artist_name}.jpg')
        shutil.copy(ori_img_path, dst_path)
        print(f'copy [{ori_img_path}] to [{dst_path}]')