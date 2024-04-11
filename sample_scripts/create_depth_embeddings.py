
import argparse
import copy
import os
import os.path as osp
import time
import torch
from  tqdm import tqdm
import csv
from glob import glob
import json

def main():
    import sys
    sys.path.append('../')
    from vpd.models import FrozenCLIPEmbedder

    text_encoder = FrozenCLIPEmbedder()
    text_encoder.cuda()

    config_path = './data/zero_shot_depth_data.json'
    base_path = '/nyu_depth_v2/official_splits/test'
    
    depth_data = {}
    with open(config_path, 'r') as f:
        data = json.load(f)
        for rows in data:
            image_path = rows['test_image_path'].split(base_path)[1]
            depth_data[image_path] = rows
    
    file_name_path = '/data_5/data/agneet/masked_depth_estimation/VPD/depth/dataset/filenames/nyudepthv2/exp2_test_list.txt'
    ordered_data = []
    with open(file_name_path, 'r') as f:
        file = csv.reader(f)
        for rows in file:
            ordered_data.append(rows[0].split(' ')[0])
    
    zeroshot_weights = []
    with torch.no_grad():
        for data in tqdm(ordered_data):
            depth_sentence = depth_data[data]['depth_sentences']
            texts = depth_sentence[0] +  ". " + depth_sentence[1] +  ". " + depth_sentence[2] +  ". " + depth_sentence[3]
            embeddings = text_encoder.encode([texts]).detach().squeeze()
            zeroshot_weights.append(embeddings)
        zeroshot_weights = torch.stack(zeroshot_weights, dim=0)
    
    print(zeroshot_weights.shape)
    torch.save(zeroshot_weights.cpu(), './depth_embeddings/depth_4.pth')

if __name__ == '__main__':
    main()