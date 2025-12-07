import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random 

st.set_page_config(layout="centered")
st.title("🎅 Święty Mikołaj w Streamlit z Rozbudowanym Konfiguratorem")

# --- STAŁE (Konfiguracja kolorów w Twoim oryginalnym kodzie) ---
SKIN_COLOR = 'peachpuff'
FUR_COLOR = 'white'
FUR_TRUNK_COLOR = '#E0E0E0' 
BUCKLE_COLOR = 'gold'
BOOT_COLOR = 'black'

# --- FUNKCJE POMOCNICZE (Wymagane w Streamlit) ---
def get_random_color():
    """Generuje losowy kolor w formacie HEX."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# --- KONFIGURACJA KOLORÓW NA PASKU BOCZNYM (Dla pełności) ---
st.sidebar.header("Konfigurator Stroju")
main_color = st.sidebar.color_picker('Wybierz kolor stroju', '#FF0000', key='main_color')
belt_color = st.sidebar.color_picker('Wybierz kolor paska', '#000000', key='belt_color')

st.sidebar.header("Konfigurator Prezentów")
num_gifts = st.sidebar.slider('Liczba prezentów pod Mikołajem', min_value=0, max_value=12, value=5, step=1, key='num_gifts')
gift_shape = st.sidebar.selectbox('Wybierz kształt prezentów', ('Kwadrat', 'Koło', 'Losowy'), key='gift_shape_select')
ribbon_color_mode = st.sidebar.radio('Tryb koloru wstążek', ('Losowy', 'Stały (Złoty)'), key='ribbon_color_mode_radio')

# --- ZMODYFIKOWANA FUNKCJA RYSOWANIA ---

def draw_santa(main_color, belt_color, num_gifts, gift_shape, ribbon_color_mode):
    """
    Funkcja rysująca schematycznego Świętego Mikołaja i konfigurowalne prezenty.
    Została poprawiona, aby zapobiec nachodzeniu prezentów na buty.
    """
    fig, ax = plt.subplots(figsize=(6, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(-3.2, 9) 
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
    # BUTY Mikołaja
    but_l = patches.Rectangle((3, -3), 1.5, 1, facecolor=BOOT_COLOR, zorder=2)
    ax.add_patch(but_l)
    but_p = patches.Rectangle((5.5, -3), 1.5, 1, facecolor=BOOT_COLOR, zorder=2)
    ax.add_patch(but_p)

    # --- NOWE, ŚCIŚLE OGRANICZONE OBSZARY PREZENTÓW ---
    
    # Obszary, które NIE ZAWIERAJĄ butów Mikołaja:
    LEFT_GIFT_AREA = (0.5, 3.0) 
    RIGHT_GIFT_AREA = (7.0, 9.5) 
    Y_FLOOR = -3.0

    def draw_gifts_band(x_start_area, x_end_area, count):
        if count <= 0:
            return

        # Używamy ścisłych granic obszaru
        band_width = x_end_area - x_start_area
        slot_width = band_width / count

        for j in range(count):
            slot_x0 = x_start_area + j * slot_width

            # Losowa wysokość: Max 1.4, Min 0.9.
            h = random.uniform(0.9, 1.4) 
            
            # W: rozmiar dopasowany do slotu, aby zostawić margines
            w_min = slot_width * 0.5
            w_max = slot_width * 0.8
            w = random.uniform(w_min, w_max)

            # Pozycja X: losowo wewnątrz przydzielonego slotu
            x = slot_x0 + random.uniform(0, slot_width - w)
            
            # Pozycja Y: prezenty opierają się na podłodze (Y_FLOOR)
            y = Y_FLOOR 

            gift_color = get_random_color()
            ribbon_color = 'gold' if ribbon_color_mode == 'Stały (Złoty)' else get_random_color()

            current_shape = gift_shape
            if current_shape == 'Losowy':
                current_shape = random.choice(['Kwadrat', 'Koło'])

            # --- KORPUS PREZENTU + WZORKI ---
            if current_shape == 'Kwadrat':
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

                # pionowe pół-przezroczyste pasy
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

                # wstążki
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
                center_y = Y_FLOOR + radius

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

                # kropeczki na brzegu
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

                # wstążki przez środek
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

            # --- KOKARDA ---
            if random.choice([True, False]):
                petelka = patches.Circle(
                    (center_x, top_y - 0.05),
                    radius=0.1,
                    facecolor=ribbon_color,
                    zorder=2
                )
                ax.add_patch(petelka)

            # --- SHINE (POŁYSK) ---
            shine_color = random.choice(['white', 'yellow'])
            if current_shape == 'Kwadrat':
                # Połysk na górnym/lewym rogu
                shine_x = random.uniform(x + 0.15, x + w * 0.5)
                shine_y = random.uniform(y + h * 0.6, y + h - 0.15)
            else:
                r_limit = radius * 0.5
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

    # rozdział liczby prezentów na lewą/prawą stronę
    if num_gifts > 0:
        left_count = (num_gifts + 1) // 2
        right_count = num_gifts - left_count

        draw_gifts_band(LEFT_GIFT_AREA[0], LEFT_GIFT_AREA[1], left_count)
        draw_gifts_band(RIGHT_GIFT_AREA[0], RIGHT_GIFT_AREA[1], right_count)

    st.pyplot(fig)


# Uruchomienie aplikacji Streamlit
draw_santa(main_color, belt_color, num_gifts, gift_shape, ribbon_color_mode)
