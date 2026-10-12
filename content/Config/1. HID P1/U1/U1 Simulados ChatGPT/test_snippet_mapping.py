import re

# Table of conversions for subscripts:
SUB_MAP = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
    '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
    'x': 'ₓ', 'y': 'ᵧ', 'z': '₂', # z has no standard sub in latin, but let's see how subscripts are handled
    'm': 'ₘ', 'e': 'ₑ', 'i': 'ᵢ', 'j': 'ⱼ'
}

SUP_MAP = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    '+': '⁺', '-': '⁻'
}

def to_sub(s):
    res = []
    for c in s:
        if c == '0': res.append('₀')
        elif c == '1': res.append('₁')
        elif c == '2': res.append('₂')
        elif c == '3': res.append('₃')
        elif c == '4': res.append('₄')
        elif c == '5': res.append('₅')
        elif c == '6': res.append('₆')
        elif c == '7': res.append('₇')
        elif c == '8': res.append('₈')
        elif c == '9': res.append('₉')
        elif c == 'x': res.append('ₓ')
        elif c == 'y': res.append('ᵧ')
        elif c == 'z': res.append('z')
        elif c == 'm': res.append('ₘ')
        elif c == 'e': res.append('ₑ')
        elif c == 'i': res.append('ᵢ')
        elif c == 'j': res.append('ⱼ')
        else: res.append(c)
    return ''.join(res)

def to_sup(s):
    res = []
    for c in s:
        if c == '0': res.append('⁰')
        elif c == '1': res.append('¹')
        elif c == '2': res.append('²')
        elif c == '3': res.append('³')
        elif c == '4': res.append('⁴')
        elif c == '5': res.append('⁵')
        elif c == '6': res.append('⁶')
        elif c == '7': res.append('⁷')
        elif c == '8': res.append('⁸')
        elif c == '9': res.append('⁹')
        elif c == '+': res.append('⁺')
        elif c == '-': res.append('⁻')
        else: res.append(c)
    return ''.join(res)

# Let's test specific conversions against the 109 snippets:
SNIPPET_MAP = {
    # Derivative operators and vectors
    r'\nabla\cdot\mathbf V=0': '∇·V = 0',
    r'\nabla\cdot\mathbf V=1': '∇·V = 1',
    r'\dot m': 'ṁ',
    r'\dot m=': 'ṁ =',
    r'\dot m=\rho uA': 'ṁ = ρuA',
    r'\dot m=\rho A/u': 'ṁ = ρA/u',
    r'\dot m=\rho u': 'ṁ = ρu',
    r'\dot m=\rho+u+A': 'ṁ = ρ + u + A',
    r'\dot m=u/A': 'ṁ = u/A',
    r'\dot{E}': 'Ė',
    r'\dot{W}': 'Ẇ',
    r'\dot{W}=\dot{W}_m+\dot{W}_e': 'Ẇ = Ẇₘ + Ẇₑ',
    r'V\cdot': 'V·',
    r'\frac{1}{2}V^2': '(1/2)V²',
    r'\frac{D(\rho V)}{Dt}=0': 'D(ρV)/Dt = 0',
    r'\frac{D(mV)}{Dt}=F': 'D(mV)/Dt = F',
    r'\frac{F_{yx}}{Vol}=\mu\frac{\partial^2u}{\partial y^2}': 'F_yx/Vol = μ(∂²u/∂y²)',
    r'0=\mu\frac{\partial^2u}{\partial y^2}': '0 = μ(∂²u/∂y²)',
    r'\mu\frac{\partial^2 u}{\partial y^2}': 'μ(∂²u/∂y²)',
    r'\mu\frac{\partial u}{\partial t}': 'μ(∂u/∂t)',
    r'-\frac{\partial p}{\partial x}': '-∂p/∂x',
    r'\frac{\partial p}{\partial x}=0': '∂p/∂x = 0',
    r'\frac{\partial p}{\partial x}=\mu\frac{\partial^2 u}{\partial y^2}': '∂p/∂x = μ(∂²u/∂y²)',
    r'\frac{\partial u}{\partial t}=': '∂u/∂t =',
    r'\frac{\partial u}{\partial t}=0': '∂u/∂t = 0',
    r'\frac{\partial u}{\partial t}=p+\rho': '∂u/∂t = p + ρ',
    r'\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}=': '∂u/∂x + ∂v/∂y + ∂w/∂z =',
    r'\frac{\partial u}{\partial x}=': '∂u/∂x =',
    r'\frac{\partial u}{\partial x}=0': '∂u/∂x = 0',
    r'\frac{\partial u}{\partial x}=V_0': '∂u/∂x = V₀',
    r'\frac{\partial u}{\partial y}=': '∂u/∂y =',
    r'\frac{\partial u}{\partial y}=0': '∂u/∂y = 0',
    r'\frac{\partial u}{\partial y}=C_1': '∂u/∂y = C₁',
    r'\frac{\partial u}{\partial y}=V_0': '∂u/∂y = V₀',
    r'\frac{\partial v}{\partial y}=': '∂v/∂y =',
    r'\frac{\partial v}{\partial y}=0': '∂v/∂y = 0',
    r'\frac{\partial(\,.\,)}{\partial z}=0': '∂(·)/∂z = 0',
    r'\frac{\partial(\rho u)}{\partial x}+\frac{\partial(\rho v)}{\partial y}+\frac{\partial(\rho w)}{\partial z}+\frac{\partial\rho}{\partial t}=0': '∂(ρu)/∂x + ∂(ρv)/∂y + ∂(ρw)/∂z + ∂ρ/∂t = 0',
    r'\frac{\partial(\rho+gh)}{\partial y}': '∂(ρ + gh)/∂y',
    r'\frac{\partial(p+\rho gh)}{\partial x}': '∂(p + ρgh)/∂x',
    r'\frac{\partial(p-\mu)}{\partial t}': '∂(p - μ)/∂t',
    r'\frac{\partial\rho}{\partial t}=1': '∂ρ/∂t = 1',
    r'\frac{\partial^2 p}{\partial y^2}=0': '∂²p/∂y² = 0',
    r'\frac{\partial^2u}{\partial y^2}=0': '∂²u/∂y² = 0',
    r'-\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}': '-∂u/∂x = ∂v/∂y',
    r'-\partial u/\partial x=\partial v/\partial y': '-∂u/∂x = ∂v/∂y',
    r'\partial u/\partial t=0': '∂u/∂t = 0',
    r'\partial u/\partial x=0': '∂u/∂x = 0',
    r'\partial u/\partial y=C_1': '∂u/∂y = C₁',
    r'\partial v/\partial t': '∂v/∂t',
    r'\partial v/\partial y=0': '∂v/∂y = 0',
    r'\partial w/\partial z=0': '∂w/∂z = 0',
    r'\partial y/\partial t': '∂y/∂t',
    r'\partial\rho/\partial t': '∂ρ/∂t',
    r'\partial^2u/\partial y^2=0': '∂²u/∂y² = 0',
    r'u\frac{\partial u}{\partial x}': 'u(∂u/∂x)',
    r'v\frac{\partial u}{\partial y}': 'v(∂u/∂y)',
    r'\Delta^2u': 'Δ²u',
    
    # Material derivatives and density equations
    r'\rho \frac{D(V)}{Dt}=F\,Vol': 'ρ(DV/Dt) = F·Vol',
    r'\rho \frac{D(V)}{Dt}=Vol/F': 'ρ(DV/Dt) = Vol/F',
    r'\rho \frac{D(V)}{Dt}=\frac{F}{Vol}': 'ρ(DV/Dt) = F/Vol',
    r'\rho\frac{D(V)}{Dt}=\frac{F}{Vol}': 'ρ(DV/Dt) = F/Vol',
    r'\rho\frac{Du}{Dt}': 'ρ(Du/Dt)',
    r'\rho g_x': 'ρg_x',
    r'\rho g_x=\mu': 'ρg_x = μ',
    r'\rho u': 'ρu',
    r'\rho v': 'ρv',
    r'\rho w': 'ρw',
    r'\rho=0': 'ρ = 0',
    r'\rho=F/Vol': 'ρ = F/Vol',
    r'\rho=\text{constante}': 'ρ = constante',
    r'\rho=m/Vol': 'ρ = m/Vol',
    r'\rho_1=': 'ρ₁ =',
    r'\rho_1\ne\rho_2': 'ρ₁ ≠ ρ₂',
    
    # Shear stress and forces
    r'\sigma_{ij}': 'σᵢⱼ',
    r'\tau': 'τ',
    r'\tau_{ij}': 'τᵢⱼ',
    r'\tau_{yx}=\frac{A}{F}': 'τ_yx = A/F',
    r'\tau_{yx}=\frac{\Delta p}{\Delta x}': 'τ_yx = Δp/Δx',
    r'\tau_{yx}=\mu\Delta y': 'τ_yx = μΔy',
    r'\tau_{yx}=\mu\frac{\Delta u}{\Delta y}': 'τ_yx = μ(Δu/Δy)',
    r'\tau_{yx}=\rho g': 'τ_yx = ρg',
    r'F_x=(p_2+p_1)\Delta y\Delta z': 'F_x = (p₂ + p₁)ΔyΔz',
    r'F_x=(p_2-p_1)\Delta x\Delta y\Delta z': 'F_x = (p₂ - p₁)ΔxΔyΔz',
    r'F_x=(p_2-p_1)\Delta y\Delta z': 'F_x = (p₂ - p₁)ΔyΔz',
    r'F_x=\Delta p/\Delta x': 'F_x = Δp/Δx',
    r'F_x=p_1/p_2': 'F_x = p₁/p₂',
    r'A_1=A_2=\Delta y\Delta z': 'A₁ = A₂ = ΔyΔz',
    r'A_1>A_2': 'A₁ > A₂',
    r'-(p - V.n)dA': '-(p - V·n)dA',
    r'F=pA': 'F = pA',
    r'F=': 'F =',
    
    # Velocity expressions and profiles
    r'u_2A_2=': 'u₂A₂ =',
    r'u_2A_2=u_1A_1': 'u₂A₂ = u₁A₁',
    r'u_2>u_1': 'u₂ > u₁',
    r'u_1=0': 'u₁ = 0',
    r'u_1=u_2': 'u₁ = u₂',
    r'u_2=0': 'u₂ = 0',
    r'u_1': 'u₁',
    r'u_2': 'u₂',
    r'V_0': 'V₀',
    r'C_1=V_0/a': 'C₁ = V₀/a',
    r'C_2=0': 'C₂ = 0',
    r'C_1': 'C₁',
    r'C_2': 'C₂',
    r'C_1y+C_2': 'C₁y + C₂',
    r'u(0)=0': 'u(0) = 0',
    r'u(0)=V_0': 'u(0) = V₀',
    r'u(0)=u(a)=0': 'u(0) = u(a) = 0',
    r'u(0)=u(a)=V_0': 'u(0) = u(a) = V₀',
    r'u(a)=0': 'u(a) = 0',
    r'u(a)=V_0': 'u(a) = V₀',
    r'u(y=0)=': 'u(y=0) =',
    r'u(y=0)=0': 'u(y=0) = 0',
    r'u(y=a)=': 'u(y=a) =',
    r'u(y=a)=0': 'u(y=a) = 0',
    r'u=': 'u =',
    r'u=0': 'u = 0',
    r'u=C_1y+C_2': 'u = C₁y + C₂',
    r'u=C_1y^2+C_2': 'u = C₁y² + C₂',
    r'u=V_0': 'u = V₀',
    r'u=V_0/a': 'u = V₀/a',
    r'u=V_0y^2/a^2': 'u = V₀y²/a²',
    r'u=\frac{V_0}{a}y': 'u = (V₀/a)y',
    r'u=\frac{V_0}{a}y^2': 'u = (V₀/a)y²',
    r'u=(V_0/a)y': 'u = (V₀/a)y',
    r'u=v=w': 'u = v = w',
    r'v(0)=V_0': 'v(0) = V₀',
    r'v(a)=0': 'v(a) = 0',
    r'v=': 'v =',
    r'v=0': 'v = 0',
    r'v=V_0': 'v = V₀',
    r'w=': 'w =',
    r'w=0': 'w = 0',
    r'w=V_0': 'w = V₀',
    
    # Acceleration
    r'a_x': 'a_x',
    r'a_y': 'a_y',
    r'a_x=\frac{\partial \rho}{\partial t}': 'a_x = ∂ρ/∂t',
    r'a_x=\frac{\partial u}{\partial t}': 'a_x = ∂u/∂t',
    r'a_x=\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}+v\frac{\partial u}{\partial y}+w\frac{\partial u}{\partial z}': 'a_x = ∂u/∂t + u(∂u/∂x) + v(∂u/∂y) + w(∂u/∂z)',
    r'a_x=\rho uA': 'a_x = ρuA',
    r'a_x=u+v+w': 'a_x = u + v + w',
    
    # Gravity and angles
    r'\sin\theta': 'sen θ',
    r'\theta': 'θ',
    r'\phi': 'ϕ',
    r'g\sin': 'g sen',
    r'g\sin\theta': 'g sen θ',
    r'g_x=0': 'g_x = 0',
    r'g_x=\mu g': 'g_x = μg',
    r'g_x=\rho g': 'g_x = ρg',
    r'g_x=g': 'g_x = g',
    r'g_x=g\cos\theta': 'g_x = g cos θ',
    r'g_x=g\sin\theta': 'g_x = g sen θ',
    
    # Energy, work, mass
    r'E=Q+W': 'E = Q + W',
    r'E=Q-W': 'E = Q - W',
    r'E=W-Q': 'E = W - Q',
    r'E=\rho V': 'E = ρV',
    r'E=pA': 'E = pA',
    r'e=Q-W': 'e = Q - W',
    r'e=\hat{u}+V+gz': 'e = û + V + gz',
    r'e=\hat{u}+\frac{1}{2}V^2+gz': 'e = û + (1/2)V² + gz',
    r'e=\rho+\frac{1}{2}V^2+gz': 'e = ρ + (1/2)V² + gz',
    r'e=p+\mu+gz': 'e = p + μ + gz',
    r'e\rho': 'eρ',
    r'e_{outros}': 'e_outros',
    r'\hat{u}': 'û',
    r'm=': 'm =',
    r'm=V/\rho': 'm = V/ρ',
    r'm=\rho V': 'm = ρV',
    r'm=\rho V^2': 'm = ρV²',
    r'm=\rho+V': 'm = ρ + V',
    r'm=\rho/V': 'm = ρ/V',
    r'p+\rho gh': 'p + ρgh',
    r'p_1 < p_2': 'p₁ < p₂',
    r'p_1 = p_2': 'p₁ = p₂',
    r'p_1 > p_2': 'p₁ > p₂',
    r'p_1=p_2': 'p₁ = p₂',
    r'p_1>p_2': 'p₁ > p₂',
    r'p_1': 'p₁',
    r'p_2': 'p₂',
    
    # Coordinates and constants
    r'y=0': 'y = 0',
    r'y=a': 'y = a',
    r'y=': 'y =',
    
    # Standalone single variables
    r'\mu': 'μ',
    r'\rho': 'ρ',
    r'gz': 'gz',
    r'u': 'u',
    r'v': 'v',
    r'w': 'w',
    r'x': 'x',
    r'y': 'y',
    r'z': 'z',
    r'h': 'h',
    r'm': 'm',
    r'n': 'n',
    r'p': 'p',
    r'e': 'e',
    r'a': 'a',
    r'A': 'A',
    r'E': 'E',
    r'F': 'F',
    r'V': 'V',
    r'W': 'W',
    r'>': '>',
    r'0': '0'
}

raw_snippets = open('all_snippets_raw.txt', encoding='utf-8').read().splitlines()
missing = []
for s in raw_snippets:
    if s not in SNIPPET_MAP:
        missing.append(s)

print(f"Total raw snippets: {len(raw_snippets)}")
print(f"Mapped snippets: {len(raw_snippets) - len(missing)}")
print(f"Missing snippets: {len(missing)}")
for m in missing:
    print("  MISSING:", repr(m))
