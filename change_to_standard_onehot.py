import os
import numpy as np
import SimpleITK as sitk
from tqdm import tqdm
import shutil

if __name__ == "__main__":
    path1_img = r"C:\Git\DataSet\Pancreas\compressed_volume"
    path1_seg = r"C:\Git\DataSet\Pancreas\compressed_segmentation"
    path2_img = r"E:\Pancreas_169_zwh\imgs"
    path2_seg = r"E:\Pancreas_169_zwh\labels"
    path2_seg_altered = r"E:\Pancreas_169_zwh\labels_altered"

    if not os.path.exists(path2_seg_altered):
        os.mkdir(path2_seg_altered)
    else:
        shutil.rmtree(path2_seg_altered)
        os.mkdir(path2_seg_altered)

    for ind,nii in tqdm(enumerate(os.listdir(path2_seg))):
        image = sitk.ReadImage(os.path.join(path2_seg,nii))
        spacing = image.GetSpacing()
        direction = image.GetDirection()
        origin = image.GetOrigin()

        npy = sitk.GetArrayFromImage(image)
        npy_transposed = np.transpose(npy, (3,0,1,2))
        npy_transposed[npy_transposed==255]=1
        img_alterd = sitk.GetImageFromArray(npy_transposed)

        img_alterd.SetSpacing(spacing)
        img_alterd.SetDirection(direction)
        img_alterd.SetOrigin(origin)

        sitk.WriteImage(img_alterd,os.path.join(path2_seg_altered,nii))
