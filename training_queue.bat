Rem "Paul Face" Landmark Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source\010_Paul_K\080_Crop_512_FaceLandmarks\020_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source\010_Paul_K\080_Crop_512_FaceLandmarks\030_Checkpoint

echo 'Paul Face' Landmark Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source\010_Paul_K\080_Crop_512_FaceLandmarks\030_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source\010_Paul_K\080_Crop_512_FaceLandmarks\040_ExportedModel

echo 'Paul Face' Landmark Export Finished
echo XXXXXXXXXXXXXXXXX



Rem "Dark Faces" Face Landmark Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source\050_Dark_Faces\020_FaceLandmarks_512\020_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source\050_Dark_Faces\020_FaceLandmarks_512\030_Checkpoint

echo 'Dark Faces' Landmark Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source\050_Dark_Faces\020_FaceLandmarks_512\030_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source\050_Dark_Faces\020_FaceLandmarks_512\040_ExportedModel

echo 'Dark Faces' Landmark Export Finished
echo XXXXXXXXXXXXXXXXX



Rem "Dark Faces Paul Mix" Face Landmark Training
py .\pix2pix.py -m train^
 -i D:\Local_Data\Projects\Paul_Pix2Pix\Source\060_Dark_Faces_Paul_Mix\010_FaceLandmarks_512\020_SBS^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source\060_Dark_Faces_Paul_Mix\010_FaceLandmarks_512\030_Checkpoint

echo 'Dark Faces Paul Mix' Landmark Training Finished
echo XXXXXXXXXXXXXXXXX

py .\pix2pix.py -m export^
 -c D:\Local_Data\Projects\Paul_Pix2Pix\Source\060_Dark_Faces_Paul_Mix\010_FaceLandmarks_512\030_Checkpoint^
 -o D:\Local_Data\Projects\Paul_Pix2Pix\Source\060_Dark_Faces_Paul_Mix\010_FaceLandmarks_512\040_ExportedModel

echo 'Dark Faces Paul Mix' Landmark Export Finished
echo XXXXXXXXXXXXXXXXX



echo XXXXXXXXXXXXXXXXX
echo XXXXXXXXXXXXXXXXX
echo Finished executing Queue

cmd /k