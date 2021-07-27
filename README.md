# DISCONTINUED (check out [Elodie](https://github.com/jmathai/elodie))

# Welcome to photos.rename()

## Organising photos with a python auto renaming utility

This is work in progress. Basic functionality as CLI tool is given.

Currently supported rename scheme:
> YYYY-MM-DD_old-name.ext

The date is extracted from the exif data of the file.
This currently depends on [exif](https://pypi.org/project/exif/).

### Current limitations

Currently supported file type is jpg / jpeg.  
Maybe I will add PNG support via [Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#png),
[Hachoir](https://hachoir.readthedocs.io/en/latest/index.html), a PNG reading lib or XMP in the future.  
_While evaluating Pillow and Hachoir I saw that my test data does not incorporate any related meta data.
Therefore I would use the modification or creation time of the file as used timestamp for renaming if XMP or
another solution would not work._

## Background of the project

I developed this little script to automatically rename my photos collection taken by my DSLR to reduce the risk of name collisions.
Furthermore this will help me with my photos from my smartphone as well. :)  
Besides I wanted to learn and practice some python coding and the basic Github workflows.

After discovering [Elodie](https://github.com/jmathai/elodie) I am not sure to continue any development. :D

## Current goals and roadmap

* Supporting more renaming schemes

**Optional long-term goals:**

* Adding a simple GUI for image folder path dialogs and options
* Adding support for PNGs

**Finished implementations:**

* Recursive renaming -> including subfolders
