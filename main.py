from pathlib import Path

from exif import Image

extensions = ('.jpg', '.jpeg', '.JPG', '.JPEG')


def rename_imgs(file):
    if file.is_file() and file.suffix in extensions:
        with open(file, 'rb') as pic:
            img = Image(pic)
        if img.has_exif:
            try:
                parsed_date = img.datetime_original.replace(
                    ':', '-').split(' ')
                if parsed_date[0] not in str(file):
                    file.rename(
                        Path(file.parent / Path(parsed_date[0] + '_' + file.stem + file.suffix)))
            except:
                print(f'{file.stem} has no valid datetime original exif tag')
                try:
                    parsed_date = img.datetime.replace(
                        ':', '-').split(' ')
                    if parsed_date[0] not in str(file):
                        file.rename(
                            Path(file.parent / Path(parsed_date[0] + '_' + file.stem + file.suffix)))
                except:
                    print(f'Alternative tag for {file.stem} not found')


if __name__ == '__main__':
    print('Still wip. But this project will grow and be helpful while organising your photos. :)')

    try:
        img_dir = Path(input('Please enter the path to your photos here: '))
        recursive = True if input(
            'Should the renaming include subfolders? [yes, no]: ') == 'yes' else False

        print(
            f'Renaming images in {img_dir}. (This may take a while! Recursive renaming: {recursive})')
        if recursive:
            for img in img_dir.rglob('*'):
                rename_imgs(img)
        else:
            for img in img_dir.iterdir():
                rename_imgs(img)
        print('Renaming done. :)')

    except Exception as inst:
        print('Unfortunately an error occurred. Check this output. If you believe it\'s an error on my side please open an issue on Github.',
              inst, sep='\n\n')
