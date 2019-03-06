echo Setting CUDA DEVICES
SET CUDA_VISIBLE_DEVICES=1
echo


echo Start 'Dark Faces' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\020_DarkFaces_1K\030_FaceLandmark_1K\020_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\020_DarkFaces_1K\030_FaceLandmark_1K\030_Checkpoint

echo 'Dark Faces' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\020_DarkFaces_1K\030_FaceLandmark_1K\030_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\020_DarkFaces_1K\030_FaceLandmark_1K\040_ExportedModel

echo 'Dark Faces' Training Exported
echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX




echo Start 'Adrian Dark Faces' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\050_Adrian_DarkFaces_1K\010_FaceLandmark_1K\010_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\050_Adrian_DarkFaces_1K\010_FaceLandmark_1K\020_Checkpoint

echo 'Adrian Dark Faces' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\050_Adrian_DarkFaces_1K\010_FaceLandmark_1K\020_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\050_Adrian_DarkFaces_1K\010_FaceLandmark_1K\030_ExportedModel

echo 'Adrian Dark Faces' Training Exported
echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX





echo Start 'Adrian Dark Faces Glitch' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\060_Adrian_DarkFaces_Glitch_1K\010_FaceLandmark_1K\010_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\060_Adrian_DarkFaces_Glitch_1K\010_FaceLandmark_1K\020_Checkpoint

echo 'Adrian Dark Faces Glitch' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\060_Adrian_DarkFaces_Glitch_1K\010_FaceLandmark_1K\020_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\060_Adrian_DarkFaces_Glitch_1K\010_FaceLandmark_1K\030_ExportedModel

echo 'Adrian Dark Faces Glitch' Training Exported
echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX





echo Start 'Adrian Dark Faces Pix Sort' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\060_Adrian_DarkFaces_PixSort_1K\010_FaceLandmark_1K\010_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\060_Adrian_DarkFaces_PixSort_1K\010_FaceLandmark_1K\020_Checkpoint

echo 'Adrian Dark Faces Pix Sort' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\060_Adrian_DarkFaces_PixSort_1K\010_FaceLandmark_1K\020_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_1K\060_Adrian_DarkFaces_PixSort_1K\010_FaceLandmark_1K\030_ExportedModel

echo 'Adrian Dark Faces Pix Sort' Training Exported
echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX







echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
echo XXXXXXXXXXXXXXXXX
echo Finished executing Queue

cmd /k