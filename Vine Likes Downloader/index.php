<?php

ProcessVideos(1);
function ProcessVideos($Page)
{
	$Likes = json_decode(file_get_contents('https://vine.co/api/timelines/users/976708504217849856/likes?page=' . $Page . '&size=90'))->data;
	foreach ($Likes->records as $Like)
	{
		preg_match('/"contentUrl" : "(.*)",/', file_get_contents($Like->permalinkUrl), $Matches);
		file_put_contents(str_replace('https://vine.co/v/', '', $Like->permalinkUrl) . '.mp4', fopen($Matches[1], 'r'));
		echo $Matches[1], '<br>';
	}

	if (!is_null($Likes->nextPage))
		ProcessVideos($Likes->nextPage);
}