# MINATOView

## How to use

## 1 Use ReadMovie.ipynb

30 fps video is converted to 10 fps. The video is cropped. By using raw avi file, download part is not needed now.

## 2 Use GenData.py (Crop images)

[Original](https://github.com/go125/PrepareDataForDFV)

```script
nohup python GenData.py --base_path /home/ubuntu/Sayama/all_video/ \
--ROOT_DIR ../Mask_RCNN \
--WIDTH 416 \
--HEIGHT 128 \
--OUTPUT_DIR /home/ubuntu/Sayama/out \
--TEMP_DIR /home/ubuntu/Sayama/tmpdir &
```

## 3 Use GenData.py (Make Masks for finetuning)

[Original](https://github.com/go125/PrepareDataForDFV)

"all video" dir should include only "video2top_png" dir.

```script
nohup python GenData_makeMask.py --base_path /home/ubuntu/Sayama/all_video/ \
--ROOT_DIR ../Mask_RCNN \
--WIDTH 416 \
--HEIGHT 128 \
--OUTPUT_DIR /home/ubuntu/Sayama/out \
--TEMP_DIR /home/ubuntu/Sayama/tmpdir &
```


## 4 Use struct2depth_eval

Please make evaluation numpy file before fine tuning.

https://github.com/go125/struct2depth_eval

## 5 Use depth from video in the wild

Please make the finetuned model.

https://github.com/go125/depth_from_video_in_the_wild/blob/master/README.md

## 6 Use struct2depth_eval

Please make evaluation numpy file before fine tuning.

https://github.com/go125/struct2depth_eval

## 7 Use AbsRelError.py

[Original](https://github.com/go125/SfmLearner_eval)

Please calculate AbsRelError using this file.

The calculation file is changed from the original so that stereo camera groundtruth is available.

## 8 Use AbsRelError_NoScaleMatching.py

[Original](https://github.com/go125/SfmLearner_eval)

Please calculate AbsRelError (No scale Matching) using this file.

The calculation file is changed from the original so that acceleration data is available.

## 9 Use AbsRelError.ipynb

[Original](https://github.com/go125/SfmLearner_eval)

You can get images in the paper.

## Future

- MeasureLength.ipynb should be completed.
