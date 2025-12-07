import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(layout="centered")
st.title("🎅 Święty Mikołaj w Streamlit z Konfiguratorem Kolorów")

# --- KONFIGURACJA KOLORÓW NA PASKU BOCZNYM ---
st.sidebar.header("Konfigurator Stroju")

# Wybór Głównego Koloru (domyślnie Czerwony)
main_color = st.sidebar.color_picker(
    'Wybierz kolor stroju',
    '#FF0000', # Domyślny kolor (Czerwony)
    key='main_color'
)

# Wybór Koloru Paska (domyślnie Czarny)
belt_color = st.sidebar.color_picker(
    'Wybierz kolor paska',
    '#000000', # Domyślny kolor (Czarny)
    key='belt_color'
)

# Kolor skóry i futra pozostają stałe (dla prostoty)
SKIN_COLOR = 'peachpuff'
FUR_COLOR = 'white'
BUCKLE_COLOR = 'gold'
BOOT_COLOR = 'black'


def draw_santa(main_color, belt_color):
    """
    Funkcja rysująca schematycznego Świętego Mikołaja.
    Przyjmuje argumenty main_color i belt_color.
    """
    
    fig, ax = plt.subplots(figsize=(6, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(-3, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    # --- ELEMENTY GŁOWY I CZAPKI ---

    # Czapka (Kaptur - Dół) -> Używa main_color
    kaptur_dol = patches.Rectangle((3.5, 6.5), 3, 1, color=main_color, zorder=3)
    ax.add_patch(kaptur_dol)

    # Szczyt czapki (Trójkąt) -> Używa main_color
    czapka_x = np.array([4, 6, 5])
    czapka_y = np.array([7.5, 7.5, 9])
    ax.fill(czapka_x, czapka_y, color=main_color, zorder=3)

    # Puszysta kulka na czapce (stały kolor)
    kulka = patches.Circle((5, 9), radius=0.3, color=FUR_COLOR, zorder=4)
    ax.add_patch(kulka)

    # Puszyste futerko czapki (stały kolor)
    futerko = patches.Rectangle((3, 6.3), 4, 0.4, color=FUR_COLOR, zorder=4)
    ax.add_patch(futerko)

    # Głowa, Oczy, Nos, Broda (stałe kolory)
    glowa = patches.Circle((5, 5), radius=1.3, color=SKIN_COLOR, zorder=2)
    ax.add_patch(glowa)
    ax.plot(4.4, 5.5, 'o', markersize=4, color='black', zorder=5)
    ax.plot(5.6, 5.5, 'o', markersize=4, color='black', zorder=5)
    nos = patches.Circle((5, 5), radius=0.2, color='brown', zorder=5)
    ax.add_patch(nos)
    broda_x = np.array([3.5, 6.5, 5])
    broda_y = np.array([4, 4, 2])
    ax.fill(broda_x, broda_y, color=FUR_COLOR, zorder=1)

    # --- TUŁÓW, RĘCE I NOGI ---

    # 1. TUŁÓW -> Używa main_color
    tulow = patches.Rectangle((3, 0), 4, 4, color=main_color, zorder=1)
    ax.add_patch(tulow)

    # 2. FUTRO NA TUŁOWIU (stały kolor)
    futerko_tulow = patches.Rectangle((3, 3.5), 4, 0.5, color=FUR_COLOR, zorder=2)
    ax.add_patch(futerko_tulow)

    # 3. PASEK -> Używa belt_color
    pasek = patches.Rectangle((3, 2.8), 4, 0.5, color=belt_color, zorder=3)
    ax.add_patch(pasek)

    # 4. KLAMRA PASKA (stały kolor)
    klamra = patches.Rectangle((4.5, 2.9), 1, 0.3, color=BUCKLE_COLOR, zorder=4)
    ax.add_patch(klamra)

    # 5. RĘCE -> Używa main_color
    reka_l = patches.Rectangle((1, 2.5), 2, 0.8, color=main_color, zorder=1)
    ax.add_patch(reka_l)
    reka_p = patches.Rectangle((7, 2.5), 2, 0.8, color=main_color, zorder=1)
    ax.add_patch(reka_p)

    # 6. RĘKAWICZKI (stały kolor)
    rekawiczka_l = patches.Circle((1, 2.9), radius=0.4, color=FUR_COLOR, zorder=5)
    ax.add_patch(rekawiczka_l)
    rekawiczka_p = patches.Circle((9, 2.9), radius=0.4, color=FUR_COLOR, zorder=5)
    ax.add_patch(rekawiczka_p)

    # 7. NOGI (Spodnie) -> Używa main_color (dla spójności ze strojem)
    noga_l = patches.Rectangle((3.5, -2), 1, 2, color=main_color, zorder=1)
    ax.add_patch(noga_l)
    noga_p = patches.Rectangle((5.5, -2), 1, 2, color=main_color, zorder=1)
    ax.add_patch(noga_p)

    # 8. BUTY (stały kolor)
    but_l = patches.Rectangle((3, -3), 1.5, 1, color=BOOT_COLOR, zorder=2)
    ax.add_patch(but_l)
    but_p = patches.Rectangle((5.5, -3), 1.5, 1, color=BOOT_COLOR, zorder=2)
    ax.add_patch(but_p)

    # Wyświetlenie rysunku w Streamlit
    st.pyplot(fig)


# Uruchomienie funkcji rysującej Mikołaja z wybranymi kolorami
draw_santa(main_color, belt_color)
