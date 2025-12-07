    # --- PREZENTY: ZAWSZE OBOK MIKOŁAJA (LEWO + PRAWO) ---

    # Lewa i prawa „strefa prezentów”
    LEFT_X_START, LEFT_X_END = 0.5, 2.8    # przed lewą ręką/butem
    RIGHT_X_START, RIGHT_X_END = 7.2, 9.5  # przed prawą ręką/butem
    Y_BASE = -2.8                          # wysokość „podłogi” dla prezentów

    def draw_gifts_band(x_start, x_end, count):
        """Rysuje `count` prezentów w jednym rzędzie między x_start a x_end."""
        if count <= 0:
            return

        band_width = x_end - x_start
        slot_width = band_width / count

        for i in range(count):
            slot_x0 = x_start + i * slot_width
            slot_x1 = slot_x0 + slot_width

            # rozmiary tak, żeby nie nachodziły na siebie
            w_min = slot_width * 0.5
            w_max = slot_width * 0.8
            w = random.uniform(w_min, w_max)
            h = random.uniform(0.8, 1.2)

            x = slot_x0 + (slot_width - w) / 2
            y = Y_BASE

            gift_color = get_random_color()
            ribbon_color = 'gold' if ribbon_color_mode == 'Stały (Złoty)' else get_random_color()

            current_shape = gift_shape
            if current_shape == 'Losowy':
                current_shape = random.choice(['Kwadrat', 'Koło'])

            # --- korpus prezentu ---
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

                # delikatne pionowe pasy (wzorek)
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

                # wstążki na kole
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

            # kokarda
            if random.choice([True, False]):
                petelka = patches.Circle(
                    (center_x, top_y - 0.05),
                    radius=0.1,
                    facecolor=ribbon_color,
                    zorder=2
                )
                ax.add_patch(petelka)

            # shine
            shine_color = random.choice(['white', 'yellow'])
            if current_shape == 'Kwadrat':
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

    # Podział liczby prezentów na lewą i prawą stronę
    if num_gifts > 0:
        left_count = num_gifts // 2
        right_count = num_gifts - left_count

        draw_gifts_band(LEFT_X_START, LEFT_X_END, left_count)
        draw_gifts_band(RIGHT_X_START, RIGHT_X_END, right_count)
