$origLines = Get-Content '.\SIMULADO_HIDRODINAMICA_PADRAO_PROFESSOR_ANTI_GRAVITY.md' -Encoding UTF8
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
    elseif ($line -match '^\*\*Quest.o (\d+):\*\*') {
        # ignore
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

Write-Host "Extracted $($comments.Count) comments."

$v2Lines = @()
$currentQ = 0
$qActive = $false
$inGabaritoSection = $false

for ($i = 0; $i -lt $origLines.Count; $i++) {
    $line = $origLines[$i]
    
    if ($line -match '^# GABARITO') {
        if ($qActive -and $currentQ -gt 0) {
            $v2Lines += "
" + $comments[$currentQ] + "
"
            $qActive = $false
        }
        $inGabaritoSection = $true
        $v2Lines += $line
        continue
    }

    if (-not $inGabaritoSection) {
        if ($line -match '^\*\*Quest.o (\d+):\*\*') {
            if ($qActive -and $currentQ -gt 0) {
                $v2Lines += "
" + $comments[$currentQ] + "
"
            }
            $currentQ = [int]$matches[1]
            $qActive = $true
            $v2Lines += $line
        }
        elseif ($line -match '^---' -or $line -match '^# PARTE' -or $line -match '^`mermaid') {
            if ($qActive -and $currentQ -gt 0) {
                $v2Lines += "
" + $comments[$currentQ] + "
"
                $qActive = $false
            }
            $v2Lines += $line
        }
        else {
            $v2Lines += $line
        }
    } else {
        $v2Lines += $line
    }
}

if ($qActive -and $currentQ -gt 0 -and -not $inGabaritoSection) {
    $v2Lines += "
" + $comments[$currentQ] + "
"
}

$v2Lines -join "
" | Set-Content '.\SIMULADO_HIDRODINAMICA_PADRAO_PROFESSOR_ANTI_GRAVITY_COMENTADO_V2.md' -Encoding UTF8
Write-Host "V2 Built."
