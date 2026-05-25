# TEAC-DUNE: Previsão para detecção do bóson X(17)

**Autores:** Eduardo Magalhães de Souza, João Gonçales  
**Supervisor:** Prof. Dr. André

## 1. Motivação Teórica - TEAC
A Teoria dos Estados Atômicos Condicionais (TEAC) prevê um novo bóson vetorial X(17) com massa `m_X = 16.94 ± 0.15 MeV`, originado de transições entre estados atômicos condicionais específicos. A TEAC fixa o acoplamento do X(17) com quarks leves a partir de sua estrutura fundamental.

**Acoplamento previsto:** `g_X ≈ 6 × 10^-4`

## 2. Canal de Decaimento no DUNE
No DUNE Phase-II, com `4.0 × 10^10 K+/ano` decaindo no volume fiducial do Far Detector [DUNE TDR Vol 2, Tab 3.3], o X(17) manifesta-se no decaimento raro:

`K+ → π+ + X(17)`, com `BR = g_X^2 ≈ 3.6 × 10^-7`

**Assinatura experimental:** Pico monoenergético no momento do π+, dado por cinemática de 2 corpos:

`p_π = 226.8 MeV/c`, calculado de `E_π = (m_K^2 + m_π^2 - m_X^2) / (2m_K) = 266.3 MeV`

## 3. Cálculo de Significância com parâmetros DUNE TDR
**Sinal esperado por ano:**
`N_sig = BR × ε × Φ_K+ = 3.6 × 10^-7 × 0.005 × 4.0 × 10^10 ≈ 72 eventos/ano`  
Considerando eficiência de reconstrução `ε = 0.5%` típica para canais raros no DUNE FD.

**Background dominante:** `K+ → π+ π0`, BR = 20.67%. Por cinemática, `p_π(bkg) = 205.3 MeV/c`.  
Com resolução do DUNE FD de `σ_p ≈ 6.8 MeV/c` para π+ de ~230 MeV, o sinal fica separado do background por `3.2σ`.

**Background na janela de sinal 226.8 ± 20.4 MeV:**  
`N_bkg ≈ 3 × 10^6 eventos/ano`, dominado por `K+ → μ+ ν` com μ/π mis-ID e `K+ → π+ π0` com γ perdido.

**Significância estatística:**
`S/√B = 72 / sqrt(3 × 10^6) ≈ 0.04σ` em 1 ano de DUNE Phase-II.

**Cenário para 5σ:** Exigiria `~1.5 × 10^4 anos` de dados, ou melhoria de 10x em PID π/μ, ou resolução `σ_p < 2 MeV/c`.

## 4. Conclusão
A TEAC prevê `~70 eventos/ano` de `K+ → π+ X(17)` no DUNE Phase-II. O canal constitui teste direto da Teoria dos Estados Atômicos Condicionais, mas a detecção com a configuração baseline do DUNE é estatisticamente desafiadora. A confirmação da TEAC via X(17) demanda análise dedicada com cortes otimizados ou upgrades futuros de PID e resolução em momento.

**Código e simulação:** https://github.com/ems270812-netizen/TEAC-DUNE  
**Referência:** DUNE Collaboration, *TDR Vol 2: Physics*, arXiv:2002.03005
