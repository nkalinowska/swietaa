    # --- PREZENTY: STAŁE WSPÓŁRZĘDNE, ZAWSZE OBOK MIKOŁAJA ---

    # Każdy element: (x_lewy_dół, y_lewy_dół)
    # 6 slotów po lewej, 6 po prawej – max 12 prezentów
    gift_slots = [
        (0.6, -3.0), (1.6, -3.0), (2.4, -3.0),  # lewy dół rząd
        (0.6, -2.0), (1.6, -2.0), (2.4, -2.0),  # lewy górny rząd
        (7.4, -3.0), (8.4, -3.0), (9.2, -3.0),  # prawy dół rząd
        (7.4, -2.0), (8.4, -2.0), (9.2, -2.0),  # prawy górny rząd
    ]

    # rozmiar każdego prezentu (identyczny)
    GIFT_W = 0.7
    GIFT_H = 0.7

    max_gifts = min(num_gifts, len(gift_slots))

    for i in range(max_gifts):
        x, y = gift_slots[i]

        gift_color = get_random_color()
        ribbon_color = 'gold' if ribbon_color_mode == 'Stały (Złoty)' else get_random_color()

        current_shape = gift_shape
        if current_shape == 'Losowy':
            current_shape = random.choice(['Kwadrat', 'Koło'])

        # --- korpus prezentu ---
        if current_shape == 'Kwadrat':
            prezent = patches.Rectangle(
                (x, y),
                GIFT_W,
                GIFT_H,
                facecolor=gift_color,
                edgecolor='black',
                linewidth=1,
                zorder=0
            )
            ax.add_patch(prezent)

            center_x = x + GIFT_W / 2
            center_y = y + GIFT_H / 2
            top_y = y + GIFT_H

            # prosty wzorek – dwa pionowe, półprzezroczyste pasy
            for s in range(2):
                stripe_x = x + (s + 0.5) * GIFT_W / 2 - (GIFT_W / 8)
                stripe = patches.Rectangle(
                    (stripe_x, y + 0.05),
                    GIFT_W / 4,
                    GIFT_H - 0.1,
                    facecolor='white',
                    alpha=0.12,
                    edgecolor=None,
                    zorder=0.5
                )
                ax.add_patch(stripe)

            # wstążki
            wstazka_v = patches.Rectangle(
                (center_x - 0.06, y),
                0.12,
                GIFT_H,
                facecolor=ribbon_color,
                zorder=1
            )
            ax.add_patch(wstazka_v)
            wstazka_h = patches.Rectangle(
                (x, center_y - 0.06),
                GIFT_W,
                0.12,
                facecolor=ribbon_color,
                zorder=1
            )
            ax.add_patch(wstazka_h)

        else:  # Koło
            radius = GIFT_W / 2
            center_x = x + GIFT_W / 2
            center_y = y + radius + 0.05
            top_y = center_y + radius

            prezent = patches.Circle(
                (center_x, center_y),
                radius=radius,
                facecolor=gift_color,
                edgecolor='black',
                linewidth=1,
                zorder=0
            )
            ax.add_patch(prezent)

            # drobne kropeczki na brzegu
            for k in range(10):
                angle = 2 * np.pi * k / 10
                dot_r = radius * 0.9
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

            # wstążki przez środek koła
            wstazka_v = patches.Rectangle(
                (center_x - 0.06, center_y - radius),
                0.12,
                2 * radius,
                facecolor=ribbon_color,
                zorder=1
            )
            ax.add_patch(wstazka_v)
            wstazka_h = patches.Rectangle(
                (center_x - radius, center_y - 0.06),
                2 * radius,
                0.12,
                facecolor=ribbon_color,
                zorder=1
            )
            ax.add_patch(wstazka_h)

        # --- kokarda ---
        petelka = patches.Circle(
            (center_x, top_y - 0.04),
            radius=0.08,
            facecolor=ribbon_color,
            zorder=2
        )
        ax.add_patch(petelka)

        # --- shine (połysk) ---
        shine = patches.Circle(
            (center_x - 0.12, top_y - 0.18),
            radius=0.05,
            facecolor='white',
            alpha=0.85,
            edgecolor=None,
            zorder=2
        )
        ax.add_patch(shine)
