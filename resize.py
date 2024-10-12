import argparse
import pathlib

from PIL import Image, ImageDraw

def resizeTestImage():
    im = Image.open('PXL_20231101_110353518.jpg')
    print(im.size)
    new_size = tuple(int(x / 2) for x in im.size)
    im = im.resize(new_size)
    im.save('resized.jpg')

def resize_image_from_file(f:pathlib.Path, output_dir:pathlib.Path):
    im = Image.open(f)
    original_size = im.size
    new_size = tuple(int(x / 2) for x in original_size)
    print(f'Resizing {f.name} from {original_size} to {new_size}...')
    im = im.resize(new_size)
    new_name = f'{f.stem}_resized{f.suffix}'
    new_path = output_dir / pathlib.Path(new_name)
    print(f'Saving as {new_path}')
    im.save(new_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to an image file or directory containing image files")

    args = parser.parse_args()

    source_path = pathlib.Path(args.source)

    if(source_path.is_dir):
        f:pathlib.Path
        output_dir = source_path / 'output'
        output_dir.mkdir(exist_ok=True)
        for f in source_path.glob('*.*'):
            print(f)
            resize_image_from_file(f, output_dir)

    else:
        output_dir = source_path.parent / 'output'
        output_dir.mkdir(exist_ok=True)
        resize_image_from_file(source_path, output_dir)




    pass

if(__name__ == "__main__"):
    main()
