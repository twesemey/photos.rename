from pathlib import Path

from exif import Image


def rename_imgs(path):
    for file in Path(path).iterdir():
        if file.is_file():
            with open(file, 'rb') as pic:
                img = Image(pic)
            if img.has_exif:
                parsed_date = img.datetime.replace(':', '-').split(' ')
                if parsed_date[0] in str(file):
                    continue
                file.rename(
                    Path(file.parent / Path(parsed_date[0] + '_' + file.stem + file.suffix)))


if __name__ == '__main__':
    print('Still wip. But this project will grow and be helpful while organising your photos. :)')

    try:
        img_dir = Path(input('Please enter the path to your photos here: '))
    except Exception as inst:
        print(inst)

    print(f'Renaming images in {img_dir}. (This may take a while)')
    rename_imgs(img_dir)
    print('Renaming done. :)')
