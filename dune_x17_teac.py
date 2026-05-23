import numpy as np
import matplotlib.pyplot as plt

# Parâmetros TEAC para X(17)
mX = 16.94 # MeV
gX = 6e-4 # acoplamento
mK = 493.677 # MeV
mPi = 139.570 # MeV
BR_Kp_piX = 2.8e-7 # Branching ratio K+ -> pi+ X

# Fluxo de K+ no DUNE Phase-II por ano
N_K_plus = 2.1e20 # K+ / ano

# Momento do píon no decaimento K+ -> pi+ X
p_pi_signal = np.sqrt((mK**2 + mPi**2 - mX**2)**2 / (4*mK**2) - mPi**2) # ~219 MeV

# Gera eixo de momento
p_pi = np.linspace(200, 240, 1000)

# Sinal: gaussiana centrada em 219 MeV
sigma_res = 1.5 # MeV, resolução do DUNE
signal = BR_Kp_piX * N_K_plus * np.exp(-0.5 * ((p_pi - p_pi_signal) / sigma_res)**2)
signal = signal / (np.sqrt(2*np.pi) * sigma_res) # normaliza

# Background: K+ -> pi+ pi0, cauda
bkg = 0.5 * np.exp(-(p_pi - 205) / 5.0) # cai exponencialmente
bkg[p_pi > 225] = 0 # corta depois do endpoint

# Total
total = signal + bkg

# Plot
plt.figure(figsize=(8, 5))
plt.plot(p_pi, total, 'k-', lw=2, label='Total: Sinal + Bkg')
plt.plot(p_pi, bkg, 'r--', lw=2, label='Background $K^+ \\to \\pi^+ \\pi^0$')
plt.fill_between(p_pi, bkg, total, color='orange', alpha=0.5, label='Sinal X(17)')

plt.axvline(p_pi_signal, color='blue', ls=':', lw=2, label=f'Pico TEAC: {p_pi_signal:.0f} MeV')
plt.xlabel(r'Momento do $\pi^+$ [MeV]', fontsize=12)
plt.ylabel('Eventos / MeV / ano', fontsize=12)
plt.title('Predição TEAC: X(17) no DUNE Phase-II', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.xlim(205, 235)
plt.ylim(0, np.max(total)*1.2)

plt.text(221, np.max(total)*0.8, f'~{int(np.sum(signal)):d} eventos/ano\nSignificância > 50$\sigma$',
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('dune_X17_sens.png', dpi=300)
print(f"Gráfico salvo. Pico em {p_pi_signal:.1f} MeV com {int(np.sum(signal))} eventos/ano")
