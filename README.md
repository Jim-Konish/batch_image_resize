# batch_image_resize
A python script to resize a single image or all images in a directory.

Currently, this only divides width and height by 2 to reduce typical smartphone photos to a size that won't bounce from most email servers.

## Usage

Provide the path to a single image or a directory containing multiple images, and the results will be placed in an `output` beneath the directory containing the source image(s)

### One Image

`python resize.py <image filename>`

### Multiple Images

`python resize.py <directory containing multiple images>`


