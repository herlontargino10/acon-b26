$comLines = Get-Content '.\SIMULADO_HIDRODINAMICA_PADRAO_PROFESSOR_ANTI_GRAVITY_COMENTADO.md' -Encoding UTF8
$comments = @{}
$currentQ = 0
$currentComment = @()
$inComment = $false

for ($i = 0; $i -lt $comLines.Count; $i++) {
    $line = $comLines[$i]
    if ($line -match '^## Quest.o (\d+)') {
        if ($inComment -and $currentQ -gt 0) {
            $comments[$currentQ] = $currentComment -join "
"
        }
        $currentQ = [int]$matches[1]
        $currentComment = @()
        $inComment = $false
    }
    elseif ($line -match '^### Gabarito Comentado') {
        $inComment = $true
        $currentComment += $line
    }
    elseif ($inComment) {
        $currentComment += $line
    }
}
if ($inComment -and $currentQ -gt 0) {
    $comments[$currentQ] = $currentComment -join "
"
}

Write-Host "Q10 comment:"
Write-Host $comments[10]
Write-Host "--------------------"
Write-Host "Q11 comment:"
Write-Host $comments[11]
