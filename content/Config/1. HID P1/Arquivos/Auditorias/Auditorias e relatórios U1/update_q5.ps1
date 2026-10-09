$sim1 = [System.IO.File]::ReadAllText('SIMULADO_U1_CAPITULO_1.md', [System.Text.Encoding]::UTF8)
$q5_question_block = [regex]::Match($sim1, '(?s)### 5.*?seis passos fundamentais\.').Value
$q5_gabarito_block = [regex]::Match($sim1, '(?s)### Quest.o 5.*').Value

Write-Output "Extracted Question Block: $($q5_question_block.Length) chars"
Write-Output "Extracted Gabarito Block: $($q5_gabarito_block.Length) chars"

foreach ($i in 2..4) {
    # 1. Update Simulado file
    $file = "SIMULADO_U1_CAPITULO_$i.md"
    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    
    $split = $content -split '(?=# Gabarito Comentado)'
    $partA = $split[0]
    $partB = $split[1]
    
    $matchA = [regex]::Match($partA, '(?s)### 5.*?seis passos fundamentais\.')
    if ($matchA.Success) {
        $partA_new = $partA.Substring(0, $matchA.Index) + $q5_question_block + $partA.Substring($matchA.Index + $matchA.Length)
    } else {
        $partA_new = $partA
        Write-Output "WARNING: Q5 Question not found in $file"
    }
    
    $matchB = [regex]::Match($partB, '(?s)### (Quest.o 5|5. Quest.o).*')
    if ($matchB.Success) {
        $partB_new = $partB.Substring(0, $matchB.Index) + $q5_gabarito_block
    } else {
        $partB_new = $partB
        Write-Output "WARNING: Q5 Gabarito not found in $file"
    }
    
    $content_new = $partA_new + $partB_new
    if ($content -ne $content_new) {
        [System.IO.File]::WriteAllText($file, $content_new, [System.Text.Encoding]::UTF8)
        Write-Output "Updated $file"
    } else {
        Write-Output "No changes needed for $file"
    }
    
    # 2. Update Gabarito file
    $fileG = "GABARITO_COMENTADO_U1_CAPITULO_$i.md"
    $contentG = [System.IO.File]::ReadAllText($fileG, [System.Text.Encoding]::UTF8)
    $matchG = [regex]::Match($contentG, '(?s)### (Quest.o 5|5. Quest.o).*')
    if ($matchG.Success) {
        $contentG_new = $contentG.Substring(0, $matchG.Index) + $q5_gabarito_block
        if ($contentG -ne $contentG_new) {
            [System.IO.File]::WriteAllText($fileG, $contentG_new, [System.Text.Encoding]::UTF8)
            Write-Output "Updated $fileG"
        } else {
            Write-Output "No changes needed for $fileG"
        }
    } else {
        Write-Output "WARNING: Q5 Gabarito not found in $fileG"
    }
}
