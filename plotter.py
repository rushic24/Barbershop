import matplotlib.pyplot as plt

'''
This file is to plot the results generated by main.py
'''

# python main.py --im_path1 16.png --im_path2 15.png --im_path3 117.png --sign realistic --smooth 5  

image_files = ['16.png', '15.png', '117.png']
imgs = [plt.imread(f"./input/face/{x}") for x in image_files]

# [generatedmask, generatedimg]

outfiles = ['./output/vis_mask_16_15_realistic.png', 'output/16_15_117_realistic.png']
outimgs = [plt.imread(x) for x in outfiles]
imgs = [imgs[1], imgs[0], outimgs[1], imgs[2], outimgs[0]]
imgtitle = ["Structure", "Appearance", "Mask", "Identity"]

fig, axd = plt.subplot_mosaic([['upper left', 'mid', 'right'],
                               ['mid left', 'mid', 'right'],
                               ['lower left', 'mid', 'right']],
                              figsize=(5.5, 3.5), constrained_layout=True)
for k, j in zip(axd, imgs):
    axd[k].imshow(j)
plt.show()
