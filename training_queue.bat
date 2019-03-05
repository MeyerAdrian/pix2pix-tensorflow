echo Setting CUDA DEVICES
SET CUDA_VISIBLE_DEVICES=1
echo


echo Start 'Adrian_EricLacombe' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\040_Adrian_EricLacombe_Mix_1K\010_FaceLandmark_1K\010_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\040_Adrian_EricLacombe_Mix_1K\010_FaceLandmark_1K\020_Checkpoint

echo 'Adrian_EricLacombe' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\040_Adrian_EricLacombe_Mix_1K\010_FaceLandmark_1K\020_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\040_Adrian_EricLacombe_Mix_1K\010_FaceLandmark_1K\030_ExportedModel

echo 'Adrian_EricLacombe' Training Exported
echo XXXXXXXXXXXXXXXXX



echo Resume 'Adrian_M' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\010_Adrian_M\050_FaceLandmarks_1K\020_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\010_Adrian_M\050_FaceLandmarks_1K\030_Checkpoint^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\010_Adrian_M\050_FaceLandmarks_1K\030_Checkpoint

echo 'Adrian_M' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\010_Adrian_M\050_FaceLandmarks_1K\030_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\010_Adrian_M\050_FaceLandmarks_1K\040_ExportedModel

echo 'Adrian_M' Training Exported
echo XXXXXXXXXXXXXXXXX



echo Start 'EricLacombe' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\030_EricLacombe_1K\030_FaceLandmark_1K\020_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\030_EricLacombe_1K\030_FaceLandmark_1K\030_Checkpoint

echo 'EricLacombe' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\030_EricLacombe_1K\030_FaceLandmark_1K\030_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\030_EricLacombe_1K\030_FaceLandmark_1K\040_ExportedModel

echo 'EricLacombe' Training Exported
echo XXXXXXXXXXXXXXXXX





echo XXXXXXXXXXXXXXXXX
echo XXXXXXXXXXXXXXXXX
echo Finished executing Queue

cmd /k