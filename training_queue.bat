echo Setting CUDA DEVICES
SET CUDA_VISIBLE_DEVICES=1
echo


echo Start 'Paul Dark Faces Mix' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\020_Paul_DarkFaces_Mix_1K\010_FaceLandmarks_1K\010_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\020_Paul_DarkFaces_Mix_1K\010_FaceLandmarks_1K\020_Checkpoint

echo 'Paul Dark Faces Mix' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\020_Paul_DarkFaces_Mix_1K\010_FaceLandmarks_1K\020_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\020_Paul_DarkFaces_Mix_1K\010_FaceLandmarks_1K\030_ExportedModel

echo 'Paul Dark Faces Mix' Training Exported
echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX




echo Start 'Paul Eric Lacombe Mix' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\030_Paul_EricLacombe_Mix_1K\010_Face_Landmarks_010\010_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\030_Paul_EricLacombe_Mix_1K\010_Face_Landmarks_010\020_Checkpoint

echo 'Paul Eric Lacombe Mix' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\030_Paul_EricLacombe_Mix_1K\010_Face_Landmarks_010\020_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\030_Paul_EricLacombe_Mix_1K\010_Face_Landmarks_010\030_ExportedModel

echo 'Paul Eric Lacombe Mix' Training Exported
echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX





echo Start 'Paul Hipster Shit Mix' Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\050_Experimental\030_GeometricEdges\070_Combined_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\050_Experimental\030_GeometricEdges\080_Checkpoints

echo 'Paul Hipster Shit Mix' Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\050_Experimental\030_GeometricEdges\080_Checkpoints^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source_Paul_1K\050_Experimental\030_GeometricEdges\090_ExportedModels

echo 'Paul Hipster Shit Mix' Training Exported
echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX







echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
echo XXXXXXXXXXXXXXXXX
echo Finished executing Queue

cmd /k