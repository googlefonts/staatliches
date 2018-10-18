# Source Notes

The font file `Staatliches/fonts/Staatliches-Regular.ttf` is built from source using the following command from the root directory:

```
python sources/BUILD.py && gftools fix-dsig fonts/Staatliches-Regular.ttf --autofix
```

Dependencies installed should include:

 - [fontmake](https://github.com/googlei18n/fontmake)
 - [gftools](https://github.com/googlefonts/gftools)
 - [ttfautohint](https://www.freetype.org/ttfautohint/)

