# TEAC-DUNE: Predição do Bóson X(17) no DUNE

**Proposta de projeto de Iniciação Científica / TCC**

Este repositório contém o código para reproduzir a predição da Teoria dos Estados Atômicos Condicionais (TEAC) para descoberta do bóson X(17) de 16.94 MeV no experimento DUNE Phase-II.

## Resultado Principal
Usando parâmetros físicos do DUNE e acoplamento $g_X = 6 \times 10^{-4}$ da TEAC, prevemos um sinal claro de **~5.9 × 10¹³ eventos/ano** em $p_{\pi^+} = 227$ MeV. O background é desprezível, gerando **significância > 50σ**.

Este é um canal de descoberta "golden" para o DUNE.

## Como reproduzir
```bash
git clone https://github.com/SEU-USUARIO/teac-dune.git
cd teac-dune
python dune_x17_teac.py
