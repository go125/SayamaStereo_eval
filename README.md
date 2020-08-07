# MINATOView

## How to use

## 1 Use ReadMovie.ipynb

30 fps video is converted to 10 fps. The video is cropped.

## 2 Use GenData.py (crop images)

### Input example

```script
nohup python GenData.py --base_path /home/ubuntu/Sayama/all_video/ \
--ROOT_DIR ../Mask_RCNN \
--WIDTH 416 \
--HEIGHT 128 \
--OUTPUT_DIR /home/ubuntu/Sayama/out \
--TEMP_DIR /home/ubuntu/Sayama/tmpdir &
```

### Make Masks

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

https://github.com/go125/struct2depth_eval

## 4 Use SfmLearner_eval

