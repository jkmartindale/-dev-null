$Data = Invoke-RestMethod -Uri https://earn.com/lists/
$Data -match '<div id="dotco-data" data-value="(.*)"' | Out-Null
$Data = [System.Net.WebUtility]::HtmlDecode($Matches[1])
(ConvertFrom-Json $Data).landing_lists.results.order.length
# $Data = (ConvertFrom-Json $Data).landing_lists.results.index
