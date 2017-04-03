# Mooniak Families for Google Fonts
by Multiple Designers

This repository hot fixes the binary sources for [Mooniak families](https://github.com/mooniak)

## Changes from source
1. Change font names to fit within Google Font's api. We can only have weights from Thin to Black.
2. Autohint fonts using ttfautohint.


## Building fonts
```
$ cd build
$ sh build.sh
```

## Dependencies
[FontTools](https://github.com/fonttools/fonttools)
[Font Bakery](https://github.com/googlefonts/fontbakery)
[ttfautohint](https://www.freetype.org/ttfautohint/)