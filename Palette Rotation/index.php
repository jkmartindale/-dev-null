<?php

//Original image palette
$BasePalette =
[
	'00008fff0000dbff00008fff00003fef000000d3',
	'000073000000c3000000870000004b0000000f00',
	'00ff0083007f003f000000000000000000000000',
	'000753000013a700001fff00',
	'0000438b00008fff0000438b',
	'00000000000000ff000000a70000005300000000'
];

//Rotated image palettes
$Palette2 =
[
	'0000dbff00008fff00003fef000000d300008fff',
	'0000c3000000870000004b0000000f0000007300',
	'007f003f00000000000000000000000000ff0083',
	'000753000013a700001fff00',
	'0000438b00008fff0000438b',
	'000000ff000000a7000000530000000000000000'
];
$Palette3 =
[
	'00008fff00003fef000000d300008fff0000dbff',
	'0000870000004b0000000f00000073000000c300',
	'00000000000000000000000000ff0083007f003f',
	'0013a700001fff0000075300',
	'00008fff0000438b0000438b',
	'000000a7000000530000000000000000000000ff'
];
$Palette4 =
[
	'00003fef000000d300008fff0000dbff00008fff',
	'00004b0000000f00000073000000c30000008700',
	'000000000000000000ff0083007f003f00000000',
	'001fff00000753000013a700',
	'0000438b0000438b00008fff',
	'000000530000000000000000000000ff000000a7'
];
$Palette5 =
[
	'000000d300008fff0000dbff00008fff00003fef',
	'00000f00000073000000c3000000870000004b00',
	'0000000000ff0083007f003f0000000000000000',
	'001fff00000753000013a700',
	'0000438b0000438b00008fff',
	'0000000000000000000000ff000000a700000053'
];

function RotateImage($Filename)
{
	global $BasePalette, $Palette2, $Palette3, $Palette4, $Palette5;
	$Image = bin2hex(fread(fopen('textures/' . $Filename, 'r'), filesize('textures/' . $Filename)));
	fwrite(fopen('rotated/' . str_replace('.bmp', '1.bmp', $Filename), 'w'), hex2bin($Image));
	fwrite(fopen('rotated/' . str_replace('.bmp', '2.bmp', $Filename), 'w'), hex2bin(str_replace($BasePalette, $Palette2, $Image)));
	fwrite(fopen('rotated/' . str_replace('.bmp', '3.bmp', $Filename), 'w'), hex2bin(str_replace($BasePalette, $Palette3, $Image)));
	fwrite(fopen('rotated/' . str_replace('.bmp', '4.bmp', $Filename), 'w'), hex2bin(str_replace($BasePalette, $Palette4, $Image)));
	fwrite(fopen('rotated/' . str_replace('.bmp', '5.bmp', $Filename), 'w'), hex2bin(str_replace($BasePalette, $Palette5, $Image)));
}

$Directory = new DirectoryIterator('textures');
foreach ($Directory as $File)
	if (!$File->isDot())
		RotateImage($File->getFileName());