import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random 

st.set_page_config(layout="centered")
st.title("🎅 Święty Mikołaj w Streamlit z Rozbudowanym Konfiguratorem")

# --- KONFIGURACJA KOLORÓW, PREZENTÓW I KSZTAŁTÓW NA PASKU BOCZNYM ---
st.sidebar.header("Konfigurator Stroju")

main_color = st.sidebar.color_picker(
    'Wybierz kolor stroju',
    '#FF0000',  # Domyślny Czerwony
    key='main_color'
)

belt_color = st.sidebar.color_picker(
    'Wybierz kolor paska',
    '#000000',  # Domyślny Czarny
    key='belt_color'
)

# Stałe kolory
SKIN_COLOR = 'peachpuff'
FUR_COLOR = 'white'
FUR_TRUNK_COLOR = '#E0E0E0'
BUCKLE_COLOR = 'gold'
BOOT_COLOR = 'black'

# --- Konfiguracja Prezentów ---
st.sidebar.header("Konfigurator Prezentów")
num_gifts = st.sidebar.slider(
    'Liczba prezentów pod Mikołajem',
    min_value=0,
    max_value=12,
    value=5,
    step=1,
    key='num_gifts'
)

gift_shape = st.sidebar.selectbox(
    'Wybierz kształt prezentów',
    ('Kwadrat', 'Koło', 'Losowy'),
    key='gift_shape_select'
)

ribbon_color_mode = st.sidebar.radio(
    'Tryb koloru wstążek',
    ('Losowy', 'Stały (Złoty)'),
    key='ribbon_color_mode_radio'
)


# --- FUNKCJA GENERUJĄCA LOSOWY KOLOR (HEX) ---
def get_random_color():
    """Generuje losowy kolor w formacie HEX."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'


# --- FUNKCJA GŁÓWNA RYSOWANIA ---
def draw_santa(main_color, belt_color, num_gifts, gift_shape, ribbon_color_mode):
    """
    Funkcja rysująca schematycznego Świętego Mikołaja i konfigurowalne prezenty.
    """
    fig, ax = plt.subplots(figsize=(6, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(-3, 9)
    ax.set_aspect('equal')
    ax.axis('off')

    # --- GŁOWA I CZAPKA ---
    kaptur_dol = patches.Rectangle((3.5, 6.5), 3, 1, facecolor=main_color, zorder=3)
    ax.add_patch(kaptur_dol)
    czapka_x = np.array([4, 6, 5])
    czapka_y = np.array([7.5, 7.5, 9])
    ax.fill(czapka_x, czapka_y, color=main_color, zorder=3)
    kulka = patches.Circle((5, 9), radius=0.3, facecolor=FUR_COLOR, zorder=4)
    ax.add_patch(kulka)
    futerko = patches.Rectangle((3, 6.3), 4, 0.4, facecolor=FUR_COLOR, zorder=4)
    ax.add_patch(futerko)
    glowa = patches.Circle((5, 5), radius=1.3, facecolor=SKIN_COLOR, zorder=2)
    ax.add_patch(glowa)
    ax.plot(4.4, 5.5, 'o', markersize=4, color='black', zorder=5)
    ax.plot(5.6, 5.5, 'o', markersize=4, color='black', zorder=5)
    nos = patches.Circle((5, 5), radius=0.2, facecolor='brown', zorder=5)
    ax.add_patch(nos)
    broda_x = np.array([3.5, 6.5, 5])
    broda_y = np.array([4, 4, 2])
    ax.fill(broda_x, broda_y, color=FUR_COLOR, zorder=1)

    # --- TUŁÓW, RĘCE I NOGI ---
    tulow = patches.Rectangle((3, 0), 4, 4, facecolor=main_color, zorder=1)
    ax.add_patch(tulow)

    futerko_tulow = patches.Rectangle(
        (3, 3.5),
        4,
        0.5,
        facecolor=FUR_TRUNK_COLOR,
        edgecolor='#B0B0B0',
        linewidth=0.5,
        zorder=2
    )
    ax.add_patch(futerko_tulow)

    pasek = patches.Rectangle((3, 2.8), 4, 0.5, facecolor=belt_color, zorder=3)
    ax.add_patch(pasek)

    klamra = patches.Rectangle((4.5, 2.9), 1, 0.3, facecolor=BUCKLE_COLOR, zorder=4)
    ax.add_patch(klamra)

    reka_l = patches.Rectangle((1, 2.5), 2, 0.8, facecolor=main_color, zorder=1)
    ax.add_patch(reka_l)
    reka_p = patches.Rectangle((7, 2.5), 2, 0.8, facecolor=main_color, zorder=1)
    ax.add_patch(reka_p)
    rekawiczka_l = patches.Circle((1, 2.9), radius=0.4, facecolor=FUR_COLOR, zorder=5)
    ax.add_patch(rekawiczka_l)
    rekawiczka_p = patches.Circle((9, 2.9), radius=0.4, facecolor=FUR_COLOR, zorder=5)
    ax.add_patch(rekawiczka_p)

    noga_l = patches.Rectangle((3.5, -2), 1, 2, facecolor=main_color, zorder=1)
    ax.add_patch(noga_l)
    noga_p = patches.Rectangle((5.5, -2), 1, 2, facecolor=main_color, zorder=1)
    ax.add_patch(noga_p)
    but_l = patches.Rectangle((3, -3), 1.5, 1, facecolor=BOOT_COLOR, zorder=2)
    ax.add_patch(but_l)
    but_p = patches.Rectangle((5.5, -3), 1.5, 1, facecolor=BOOT_COLOR, zorder=2)
    ax.add_patch(but_p)

    # --- PREZENTY: ZAWSZE OBOK SIEBIE + DODATKOWE SZCZEGÓŁY ---
    X_START, X_END = 0.5, 9.5
    Y_BASE = -2.8  # stała linia, na której stoją prezenty

    if num_gifts > 0:
        total_width = X_END - X_START
        slot_width = total_width / num_gifts  # każdy prezent dostaje "slot" w rzędzie

        for i in range(num_gifts):
            # SLOT na prezent
            slot_x0 = X_START + i * slot_width
            slot_x1 = slot_x0 + slot_width

            # losowy, ale ograniczony rozmiar w slocie (żeby nie nachodziły na siebie)
            w_min = slot_width * 0.5
            w_max = slot_width * 0.8
            w = random.uniform(w_min, w_max)
            h = random.uniform(0.8, 1.4)

            # centrowanie w slocie
            x = slot_x0 + (slot_width - w) / 2
            y = Y_BASE

            gift_color = get_random_color()
            ribbon_color = 'gold' if ribbon_color_mode == 'Stały (Złoty)' else get_random_color()

            current_shape = gift_shape
            if current_shape == 'Losowy':
                current_shape = random.choice(['Kwadrat', 'Koło'])

            # --- RYSOWANIE PREZENTU ---
            if current_shape == 'Kwadrat':
                # Podstawowy korpus prezentu
                prezent = patches.Rectangle(
                    (x, y),
                    w,
                    h,
                    facecolor=gift_color,
                    edgecolor='black',
                    linewidth=1,
                    zorder=0
                )
                ax.add_patch(prezent)

                center_x = x + w / 2
                center_y = y + h / 2
                top_y = y + h

                # Drobny wzorek: pionowe pasy o lekkim połysku
                num_stripes = random.choice([2, 3, 4])
                for s in range(num_stripes):
                    stripe_x = x + (s + 0.5) * w / num_stripes - (w / (num_stripes * 4))
                    stripe = patches.Rectangle(
                        (stripe_x, y + 0.1),
                        w / (num_stripes * 2),
                        h - 0.2,
                        facecolor='white',
                        alpha=0.12,
                        edgecolor=None,
                        zorder=0.5
                    )
                    ax.add_patch(stripe)

                # Wstążki
                wstazka_v = patches.Rectangle(
                    (center_x - 0.08, y),
                    0.16,
                    h,
                    facecolor=ribbon_color,
                    zorder=1
                )
                ax.add_patch(wstazka_v)
                wstazka_h = patches.Rectangle(
                    (x, center_y - 0.08),
                    w,
                    0.16,
                    facecolor=ribbon_color,
                    zorder=1
                )
                ax.add_patch(wstazka_h)

            else:  # Koło
                radius = min(w, h) / 2
                center_x = x + w / 2
                center_y = y + radius + 0.05

                prezent = patches.Circle(
                    (center_x, center_y),
                    radius=radius,
                    facecolor=gift_color,
                    edgecolor='black',
                    linewidth=1,
                    zorder=0
                )
                ax.add_patch(prezent)

                top_y = center_y + radius

                # Drobny wzorek na obwodzie: kropki
                num_dots = random.choice([10, 12, 14])
                for k in range(num_dots):
                    angle = 2 * np.pi * k / num_dots
                    dot_r = radius * 0.92
                    dot_x = center_x + dot_r * np.cos(angle)
                    dot_y = center_y + dot_r * np.sin(angle)
                    dot = patches.Circle(
                        (dot_x, dot_y),
                        radius=0.03,
                        facecolor='white',
                        alpha=0.5,
                        edgecolor=None,
                        zorder=0.5
                    )
                    ax.add_patch(dot)

                # Wstążki przecinające środek
                wstazka_v = patches.Rectangle(
                    (center_x - 0.08, center_y - radius),
                    0.16,
                    2 * radius,
                    facecolor=ribbon_color,
                    zorder=1
                )
                ax.add_patch(wstazka_v)
                wstazka_h = patches.Rectangle(
                    (center_x - radius, center_y - 0.08),
                    2 * radius,
                    0.16,
                    facecolor=ribbon_color,
                    zorder=1
                )
                ax.add_patch(wstazka_h)

            # --- Kokarda / Pętelka na górze ---
            if random.choice([True, False]):
                petelka = patches.Circle(
                    (center_x, top_y - 0.05),
                    radius=0.1,
                    facecolor=ribbon_color,
                    zorder=2
                )
                ax.add_patch(petelka)

            # --- Mały "shine" (połysk) na powierzchni ---
            shine_color = random.choice(['white', 'yellow'])

            if current_shape == 'Kwadrat':
                shine_x = random.uniform(x + 0.15, x + w * 0.5)
                shine_y = random.uniform(y + h * 0.6, y + h - 0.15)
            else:
                r_limit = (min(w, h) / 2) * 0.5
                angle = random.uniform(0, 2 * np.pi)
                dist = random.uniform(0, r_limit)
                shine_x = center_x + dist * np.cos(angle)
                shine_y = center_y + dist * np.sin(angle)

            shine = patches.Circle(
                (shine_x, shine_y),
                radius=0.06,
                facecolor=shine_color,
                alpha=0.85,
                edgecolor=None,
                zorder=2
            )
            ax.add_patch(shine)

            # --- Zawieszka / etykietka prezentu ---
            if random.choice([True, False]):
                if current_shape == 'Kwadrat':
                    tag_x = x + w - 0.35
                    tag_y = top_y + 0.05
                else:
                    tag_x = center_x + radius * 0.6
                    tag_y = center_y + radius * 0.2

                # nitka
                ax.plot(
                    [center_x, tag_x + 0.12],
                    [top_y, tag_y + 0.08],
                    linewidth=0.6,
                    color='black',
                    zorder=2.5
                )

                tag = patches.Rectangle(
                    (tag_x, tag_y),
                    0.25,
                    0.16,
                    facecolor='#FFF8DC',
                    edgecolor='black',
                    linewidth=0.5,
                    zorder=3
                )
                ax.add_patch(tag)

                # "linie tekstu" na etykietce
                ax.plot(
                    [tag_x + 0.03, tag_x + 0.20],
                    [tag_y + 0.11, tag_y + 0.11],
                    linewidth=0.5,
                    color='gray',
                    zorder=3.1
                )
                ax.plot(
                    [tag_x + 0.03, tag_x + 0.16],
                    [tag_y + 0.06, tag_y + 0.06],
                    linewidth=0.5,
                    color='gray',
                    zorder=3.1
                )

    # Wyświetlenie rysunku w Streamlit
    st.pyplot(fig)


# Uruchomienie funkcji
draw_santa(main_color, belt_color, num_gifts, gift_shape, ribbon_color_mode)
