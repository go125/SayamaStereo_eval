# MINATOView

## How to use

## 1 Use ReadMovie.ipynb

30 fps video is converted to 10 fps. The video is cropped.

## 2 Use GenData.py (crop images)

[Original](https://github.com/go125/PrepareDataForDFV)

### Input example

```script
nohup python GenData.py --base_path /home/ubuntu/Sayama/all_video/ \
--ROOT_DIR ../Mask_RCNN \
--WIDTH 416 \
--HEIGHT 128 \
--OUTPUT_DIR /home/ubuntu/Sayama/out \
--TEMP_DIR /home/ubuntu/Sayama/tmpdir &
```

### Make Masks (for finetuning)

"all video" dir should include only "video2top_png" dir.

```script
nohup python GenData_makeMask.py --base_path /home/ubuntu/Sayama/all_video/ \
--ROOT_DIR ../Mask_RCNN \
--WIDTH 416 \
--HEIGHT 128 \
--OUTPUT_DIR /home/ubuntu/Sayama/out \
--TEMP_DIR /home/ubuntu/Sayama/tmpdir &
```


## 3 Use struct2depth_eval

Please make evaluation numpy file before fine tuning.

https://github.com/go125/struct2depth_eval

## 4 Use depth from video in the wild

Please make the finetuned model.

https://github.com/go125/depth_from_video_in_the_wild/blob/master/README.md

## 5 Use struct2depth_eval

Please make evaluation numpy file before fine tuning.

https://github.com/go125/struct2depth_eval

## 6 Use AbsRelError.ipynb or AbsRelError.py

Please calculate AbsRelError using these files.


