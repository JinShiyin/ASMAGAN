'''
Description: 
Author: JinShiyin
Email: shiyinjin@foxmail.com
Date: 2022-02-13 15:59:29
'''
import os
import shutil


artist_list = [
    'morisot',
    'munch',
    'kirchner',
    'pollock',
    'kandinsky',
    'monet',
    'nicholas', # roerich
    'cezanne',
    'picasso',
    'samuel',
    'vangogh'
]

out_root = 'test_logs/ASMAfinal/picked-test-images-results-for-fid-sorted-by-artist'
ori_img_dir = 'test_logs/ASMAfinal/picked-test-images-results-for-fid'
img_name_list = os.listdir(ori_img_dir)

for artist in artist_list:
    out_dir = os.path.join(out_root, artist)
    os.makedirs(out_dir, exist_ok=True)
    for img_name in img_name_list:
        if artist in img_name:
            ori_path = os.path.join(ori_img_dir, img_name)
            out_img_name = '_'.join(img_name.split('_')[:3]) + '.jpg'
            dst_path = os.path.join(out_dir, out_img_name)
            shutil.copy(ori_path, dst_path)
            print(f'copy [{ori_path}] to [{dst_path}]')
