## Sample Scripts

We share a sample example to perform zero-shot testing. In general, the following steps need to be performed for evaluation : 

* ```create_depth_embeddings.py``` - Creates the corresponding CLIP embeddings for the depth sentences. The code is a modified version of [this](https://github.com/wl-zhao/VPD/blob/main/depth/dump_nyu_text_embeddings.py); to create any embedding, please modify the code accordingly.

* Depending on the \# of images in your test set, you may need to add new files [here](https://github.com/wl-zhao/VPD/tree/main/depth/dataset/filenames/nyudepthv2) and update the [dataloader](https://github.com/wl-zhao/VPD/blob/main/depth/dataset/nyudepthv2.py). Specifically, the ```class_id``` needs to be updated so that the correct CLIP embeddings are loaded.

* Make sure the correct CLIP embeddings are loaded [here](https://github.com/wl-zhao/VPD/blob/main/depth/models_depth/model.py#L68).
