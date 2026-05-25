import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas - PDG 2024
m_K = 493.677 # MeV
m_pi = 139.570 # MeV
m_pi0 = 134.977 # MeV

# Parâmetros TEAC
m_X = 16.94 # MeV, X(17) TEAC
g_X = 6e-4 # Acoplamento TEAC
BR_sig = g_X**2 # BR(K+ -> pi+ X) = 3.6e-7

# Parâmetros DUNE Phase-II - TDR Vol 2 Tab 3.3
flux_K = 4.0e10 # K+ que decaem/ano no FD DUNE
eff = 0.005 # 0.5% eficiência reconstrução canal raro
N_sig_total = BR_sig * flux_K * eff # ~72 eventos/ano

# Cinemática 2 corpos
def p_two_body(m_parent, m1, m2):
    E1 = (m_parent**2 + m1**2 - m2**2) / (2 * m_parent)
    return np.sqrt(E1**2 - m1**2)

p_pi_sig = p_two_body(m_K, m_pi, m_X) # 226.81 MeV/c
p_pi_bkg = p_two_body(m_K, m_pi, m_pi0) # 205.31 MeV/c

# Resolução DUNE FD - TDR Vol 4, Fig 7.20
sigma_p = 6.8 # MeV/c, 3% para pi+ de 230 MeV

# Background realista na janela ±3σ = ±20.4 MeV
N_bkg_total = 3e6 # eventos/ano, K->munu mis-ID + K->pipi0 gamma perdido

# Gerar dados
p = np.linspace(180, 250, 1000)
sinal = N_sig_total * np.exp(-0.5 * ((p - p_pi_sig) / sigma_p)**2)
background = N_bkg_total * np.exp(-0.5 * ((p - p_pi_bkg) / sigma_p)**2)
total = sinal + background

# Plot
plt.figure(figsize=(10, 6))
plt.plot(p, total, 'k-', lw=2, label='Total DUNE Phase-II')
plt.plot(p, background, 'r--', lw=2, label=r'Background $K^+ \to \pi^+ \pi^0$ + $\mu\nu$')
plt.plot(p, sinal, color='orange', lw=2, label='Sinal X(17) TEAC')
plt.axvline(p_pi_sig, color='blue', ls=':', lw=1.5, label=f'Pico TEAC: {p_pi_sig:.1f} MeV/c')

plt.xlabel(r'Momento do $\pi^+$ [MeV/c]')
plt.ylabel(r'Eventos / 0.07 MeV/c / ano')
plt.title(r'Previsão TEAC: $K^+ \to \pi^+ X(17)$ no DUNE Phase-II')
plt.legend()
plt.grid(alpha=0.3)
plt.ylim(0, 3.5e6)

# Caixa de texto com valores corretos
textstr = '\n'.join([
    r'$m_X = 16.94$ MeV, $g_X = 6 \times 10^{-4}$',
    r'$N_{sig} \approx 72$ eventos/ano, $\varepsilon = 0.5\%$',
    r'$N_{bkg} \approx 3 \times 10^6$ eventos/ano',
    r'Separação: $3.2\sigma$, Significância: $0.04\sigma$'
])
plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('teac_dune_x17.png', dpi=300)
plt.show()

# Print para conferir
S_sqrtB = N_sig_total / np.sqrt(N_bkg_total)
print(f"N_sig = {N_sig_total:.1f} eventos/ano")
print(f"N_bkg = {N_bkg_total:.1e} eventos/ano")
print(f"S/√B = {S_sqrtB:.2f} sigma")
print(f"Separação = {(p_pi_sig - p_pi_bkg)/sigma_p:.1f} sigma")
