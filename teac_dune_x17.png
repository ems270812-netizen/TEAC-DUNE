import numpy as np
import matplotlib.pyplot as plt

# Parâmetros TEAC - valores finais corrigidos
m_K = 493.677  # MeV
m_pi = 139.570 # MeV
m_X = 16.94    # MeV
g_X = 6e-4
BR = g_X**2    # 3.6e-7
flux_K = 2.1e20 # K+/ano DUNE Phase-II
N_sig_total = BR * flux_K # 7.6e13 eventos/ano

# Cinemática
E_pi = (m_K**2 + m_pi**2 - m_X**2) / (2*m_K) # 266.3 MeV
p_pi_sig = np.sqrt(E_pi**2 - m_pi**2)        # 226.8 MeV/c
p_pi_bkg = 205.3 # MeV/c para K+ -> pi+ pi0
sigma_p = 0.8    # MeV/c resolução DUNE

# Eixo X
p_range = np.linspace(200, 235, 1000)

# Sinal: Gaussiana normalizada para N_sig_total
signal = N_sig_total / (sigma_p * np.sqrt(2*np.pi)) * np.exp(-0.5 * ((p_range - p_pi_sig)/sigma_p)**2)

# Background: N_bkg < 1e3, espalhado. Para visualização, uso 1e3
N_bkg_total = 1e3 
background = N_bkg_total / (sigma_p * np.sqrt(2*np.pi)) * np.exp(-0.5 * ((p_range - p_pi_bkg)/sigma_p)**2)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(p_range, signal + background, 'k-', label='Total: Sinal + Bkg', lw=2)
plt.plot(p_range, background, 'r--', label=r'Background $K^+ \to \pi^+ \pi^0$', lw=1.5)
plt.fill_between(p_range, 0, signal, color='orange', alpha=0.7, label='Sinal X(17)')
plt.axvline(p_pi_sig, color='b', ls=':', label=f'Pico TEAC: {p_pi_sig:.1f} MeV/c')

# Caixa de texto com LaTeX para evitar bug do ~
plt.text(227.5, 3.0e13, f'$\\approx${N_sig_total:.1e} eventos/ano\nSignificância > $10^{{12}}$ σ', 
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

plt.title('Predição TEAC: X(17) no DUNE Phase-II', fontsize=14)
plt.xlabel(r'Momento do $\pi^+$ [MeV/c]', fontsize=12)
plt.ylabel('Eventos / MeV / ano', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.xlim(205, 235)
plt.ylim(0, 4.0e13)
plt.tight_layout()
plt.savefig('teac_dune_x17.png', dpi=300)
plt.show()
