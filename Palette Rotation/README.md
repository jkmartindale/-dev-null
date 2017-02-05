# Palette Rotation
Bitmap files sometimes map pixel colors to those defined by a palette of limited colors, most notably the standard 255-colors. In order to animate some assets, some games would rotate values on the palette of bitmap images.

##Task
Take a bunch of game bitmap assets, rotate the palette, and export the frames accordingly.
![Rotation Groups](https://raw.githubusercontent.com/jkmartindale/dev-null/master/Palette%20Rotation/GroupList.png)
![Rotation Animation](https://raw.githubusercontent.com/jkmartindale/dev-null/master/Palette%20Rotation/FullPaletteRotate.gif)

##New Skills
- Editing binary data in PHP
- PHP string replacement with arrays
- PHP DirectoryIterator

##Code Considerations
- Bitmap files must be placed in a `textures` directory
- The `rotated` directory must exist
- There's absolutely no error correction

Task and reference images supplied by [@Rancore202](http://t.me/rancore202) on Telegram.
