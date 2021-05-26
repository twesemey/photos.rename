# Welcome to photos.rename()

## Organising photos with a python auto renaming utility

This is work in progress. Basic functionality as CLI tool is given.

Currently supported rename scheme:
> YYYY-MM-DD_old-name.ext

The date is extracted from the exif data of the file.
This currently depends on [exif](https://pypi.org/project/exif/).

### Current limitations

Currently supported file types are jpeg and tiff (untested).
Maybe I will add PNG support via [Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png), [Hachoir](https://hachoir.readthedocs.io/en/latest/index.html), a PNG reading lib or XMP in the future.  
While evaluating Pillow and Hachoir I saw that my test data does not incorporate any related meta data. Therefore I would use the modification or creation time of the file as used timestamp for renaming if XMP or another solution would not work.

## Background of the project

I developed this little script to automatically rename my photos collection taken by my DSLR to reduce the risk of name collisions.
Furthermore this will help me with my photos from my smartphone as well. :)

## Current goals and roadmap

* Supporting more renaming schemes

**Optional longterm goals:**
* Adding support for PNGs
* Adding a simple GUI for image folder path dialogs
