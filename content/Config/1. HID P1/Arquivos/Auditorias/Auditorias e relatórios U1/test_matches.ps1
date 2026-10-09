$sim1 = [System.IO.File]::ReadAllText('SIMULADO_U1_CAPITULO_1.md', [System.Text.Encoding]::UTF8)

$q5_question_pattern = '(?s)### 5. Quest.o.*?seis passos fundamentais\.'
$q5_gabarito_pattern = '(?s)### Quest.o 5 - An.lise Dimensional.*'

$q5_question_sim1 = [regex]::Match($sim1, $q5_question_pattern).Value
$q5_gabarito_sim1 = [regex]::Match($sim1, $q5_gabarito_pattern).Value

Write-Output "Q5 Question length: $($q5_question_sim1.Length)"
Write-Output "Q5 Gabarito length: $($q5_gabarito_sim1.Length)"

foreach ($i in 2..4) {
    $file = "SIMULADO_U1_CAPITULO_$i.md"
    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    
    $q5_question_match = [regex]::Match($content, $q5_question_pattern)
    $q5_gabarito_match = [regex]::Match($content, $q5_gabarito_pattern)
    
    Write-Output "File $file:"
    Write-Output "  Matched Question: $($q5_question_match.Success) (Length: $($q5_question_match.Length))"
    Write-Output "  Matched Gabarito: $($q5_gabarito_match.Success) (Length: $($q5_gabarito_match.Length))"
}
