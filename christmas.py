import tkinter as tk
import random
import math

# ================= CONFIG =================
WIDTH = 700
HEIGHT = 750
FPS_DELAY = 30  # Lebih halus (~33 FPS)

LYRICS = [
    "Last Christmas,",
    "I gave you my heart",
    "But the very next day",
    "You gave it away",
    "This year,",
    "To save me from tears",
    "I'll give it to someone special"
]

LIGHT_PALETTES = [
    ("#ff4d4d", "#661414", "#330a0a"),  # Merah (terang, redup, glow)
    ("#ffd700", "#665500", "#332b00"),  # Emas
    ("#4da6ff", "#143d66", "#0a1f33"),  # Biru
    ("#ffffff", "#666666", "#2b2b2b"),  # Putih hangat
    ("#55ff99", "#176636", "#0b331b"),  # Hijau mint
    ("#ff69b4", "#661f43", "#330f21"),  # Pink
]

# ================= WINDOW =================
root = tk.Tk()
root.title("Christmas")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.configure(bg="#050d1a")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#050d1a",
    highlightthickness=0
)
canvas.pack()

# ================= BACKGROUND & TWINKLING STARS =================
stars = []
for _ in range(110):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT - 150)
    r = random.choice([1, 1, 1.5, 2])
    star_id = canvas.create_oval(
        x - r, y - r, x + r, y + r,
        fill="#ffffff",
        outline=""
    )
    stars.append((star_id, random.uniform(0, math.pi * 2), random.uniform(0.03, 0.08)))

# Header dengan efek drop shadow
canvas.create_text(
    WIDTH // 2 + 2, 52,
    text="MERRY CHRISTMAS",
    font=("Georgia", 28, "bold"),
    fill="#02050a"
)
canvas.create_text(
    WIDTH // 2, 50,
    text="MERRY CHRISTMAS",
    font=("Georgia", 28, "bold"),
    fill="#f0f6ff"
)

canvas.create_text(
    WIDTH // 2, 88,
    text="~ a little Christmas animation ~",
    font=("Georgia", 11, "italic"),
    fill="#8da9c4"
)

# ================= GROUND & GIFTS =================
# Lapisan salju di bagian bawah
canvas.create_oval(-100, 560, WIDTH + 100, 720, fill="#112238", outline="")
canvas.create_oval(-60, 575, WIDTH + 60, 730, fill="#192f4d", outline="")

# Batang pohon dengan bayangan
TREE_CENTER = 350
canvas.create_rectangle(TREE_CENTER - 26, 535, TREE_CENTER + 26, 605, fill="#4a2e16", outline="")
canvas.create_rectangle(TREE_CENTER - 26, 535, TREE_CENTER + 4, 605, fill="#633e1f", outline="")

# Kotak kado di bawah pohon
def draw_gift(x, y, w, h, box_color, ribbon_color):
    canvas.create_rectangle(x, y, x + w, y + h, fill=box_color, outline="#081220", width=1)
    canvas.create_rectangle(x + w * 0.42, y, x + w * 0.58, y + h, fill=ribbon_color, outline="")
    canvas.create_rectangle(x, y + h * 0.4, x + w, y + h * 0.55, fill=ribbon_color, outline="")

draw_gift(255, 575, 42, 34, "#b82525", "#ffd700")
draw_gift(288, 585, 32, 26, "#1f6fb2", "#ffffff")
draw_gift(395, 578, 45, 32, "#237a4b", "#ff4d4d")
draw_gift(375, 588, 28, 22, "#d49b17", "#ffffff")

# ================= LAYERED CHRISTMAS TREE =================
# Dibuat bertumpuk dari bawah ke atas agar terlihat bervolume
tiers = [
    (430, 555, 225, "#073b24", "#0a4f30"),
    (360, 480, 185, "#09472b", "#0d5e39"),
    (295, 405, 145, "#0b5433", "#106e43"),
    (235, 330, 105, "#0e633c", "#14804e"),
    (175, 260, 65,  "#117346", "#18945b"),
]

for top_y, bot_y, half_w, dark_col, light_col in tiers:
    # Sisi gelap (kanan)
    canvas.create_polygon(
        TREE_CENTER, top_y,
        TREE_CENTER - half_w, bot_y,
        TREE_CENTER, bot_y + 12,
        TREE_CENTER + half_w, bot_y,
        fill=dark_col, outline="#052919", width=2, smooth=True
    )
    # Highlight sisi kiri (terkena cahaya)
    canvas.create_polygon(
        TREE_CENTER, top_y,
        TREE_CENTER - half_w, bot_y,
        TREE_CENTER, bot_y + 12,
        fill=light_col, outline="", smooth=True
    )

# ================= 3D SPIRAL LIGHTS =================
lights = []
NUM_LIGHTS = 115

for i in range(NUM_LIGHTS):
    t = i / (NUM_LIGHTS - 1)
    y = 195 + t * 350
    radius = 12 + t * 195
    angle = t * math.pi * 7.5  # Putaran spiral

    x = TREE_CENTER + math.sin(angle) * radius
    depth = math.cos(angle)  # +1 = paling depan, -1 = paling belakang

    palette_idx = i % len(LIGHT_PALETTES)
    bright_col, dim_col, glow_col = LIGHT_PALETTES[palette_idx]

    # Hanya gambar penuh kalau di depan, atau kecil & redup kalau di pinggir belakang
    if depth >= -0.25:
        scale = 0.7 + 0.5 * ((depth + 0.25) / 1.25)
        r = 4.2 * scale
        glow_r = r * 2.1

        glow = canvas.create_oval(
            x - glow_r, y - glow_r, x + glow_r, y + glow_r,
            fill=glow_col, outline=""
        )
        bulb = canvas.create_oval(
            x - r, y - r, x + r, y + r,
            fill=bright_col, outline=""
        )
        lights.append({
            "bulb": bulb,
            "glow": glow,
            "palette": palette_idx,
            "phase": i * 0.35,
            "is_front": True
        })
    else:
        r = 2.2
        bulb = canvas.create_oval(
            x - r, y - r, x + r, y + r,
            fill=dim_col, outline=""
        )
        lights.append({
            "bulb": bulb,
            "glow": None,
            "palette": palette_idx,
            "phase": i * 0.35,
            "is_front": False
        })

# ================= POLYGON STAR & HALO =================
def get_star_points(cx, cy, outer_r, inner_r):
    pts = []
    for i in range(10):
        ang = math.radians(i * 36 - 90)
        r = outer_r if i % 2 == 0 else inner_r
        pts.extend([cx + math.cos(ang) * r, cy + math.sin(ang) * r])
    return pts

star_halo = canvas.create_oval(
    TREE_CENTER - 28, 165 - 28, TREE_CENTER + 28, 165 + 28,
    fill="#2e2608", outline=""
)
star_poly = canvas.create_polygon(
    get_star_points(TREE_CENTER, 165, 22, 9),
    fill="#ffd700", outline="#fff5b8", width=1
)

# ================= SNOW =================
snowflakes = []
for _ in range(120):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.uniform(1.5, 3.8)
    speed = random.uniform(0.8, 2.4)
    sway_offset = random.uniform(0, math.pi * 2)
    sway_speed = random.uniform(0.02, 0.05)

    snow = canvas.create_oval(
        x, y, x + size, y + size,
        fill="#e6f2ff" if size > 2.5 else "#99b8d9",
        outline=""
    )
    snowflakes.append([snow, x, y, speed, size, sway_offset, sway_speed])

# ================= LYRICS =================
lyric_shadow = canvas.create_text(
    WIDTH // 2 + 1, 676,
    text="",
    font=("Georgia", 22, "italic"),
    fill="#03070f"
)
lyric_text = canvas.create_text(
    WIDTH // 2, 675,
    text="",
    font=("Georgia", 22, "italic"),
    fill="#ffffff"
)

# ================= ANIMATION LOOP =================
tick = 0
lyric_index = 0
lyric_timer = 0
LYRIC_DURATION = 115  # Durasi per baris lirik (dalam frame)

def animate():
    global tick, lyric_index, lyric_timer
    tick += 1

    # 1. Twinkling Background Stars
    for star_id, phase, spd in stars:
        val = int(140 + 115 * math.sin(tick * spd + phase))
        hex_col = f"#{val:02x}{val:02x}{min(255, val + 20):02x}"
        canvas.itemconfig(star_id, fill=hex_col)

    # 2. Chasing & Pulsing Spiral Lights
    for item in lights:
        wave = math.sin(tick * 0.12 - item["phase"])
        bright_col, dim_col, glow_col = LIGHT_PALETTES[item["palette"]]

        if item["is_front"]:
            if wave > 0.15:
                canvas.itemconfig(item["bulb"], fill=bright_col)
                canvas.itemconfig(item["glow"], fill=glow_col)
            else:
                canvas.itemconfig(item["bulb"], fill=dim_col)
                canvas.itemconfig(item["glow"], fill="#071526")
        else:
            canvas.itemconfig(item["bulb"], fill=dim_col if wave > 0 else "#09182b")

    # 3. Star Pulse
    pulse = math.sin(tick * 0.1)
    if pulse > 0:
        canvas.itemconfig(star_poly, fill="#fff2a6")
        canvas.itemconfig(star_halo, fill="#3d3209")
    else:
        canvas.itemconfig(star_poly, fill="#ffd700")
        canvas.itemconfig(star_halo, fill="#241d05")

    # 4. Smooth Sinusoidal Snow
    for flake in snowflakes:
        snow_id, base_x, y, speed, size, offset, sway_spd = flake
        y += speed
        offset += sway_spd
        curr_x = base_x + math.sin(offset) * 14

        if y > HEIGHT:
            y = -5
            base_x = random.randint(0, WIDTH)
            curr_x = base_x

        flake[1] = base_x
        flake[2] = y
        flake[5] = offset
        canvas.coords(snow_id, curr_x, y, curr_x + size, y + size)

    # 5. Smooth Fade-In & Fade-Out Lyrics
    lyric_timer += 1
    if lyric_timer >= LYRIC_DURATION:
        lyric_timer = 0
        lyric_index = (lyric_index + 1) % len(LYRICS)
        canvas.itemconfig(lyric_text, text=LYRICS[lyric_index])
        canvas.itemconfig(lyric_shadow, text=LYRICS[lyric_index])

    # Hitung alpha/brightness berdasarkan posisi waktu lirik
    fade_frames = 20
    if lyric_timer < fade_frames:
        alpha = lyric_timer / fade_frames
    elif lyric_timer > LYRIC_DURATION - fade_frames:
        alpha = (LYRIC_DURATION - lyric_timer) / fade_frames
    else:
        alpha = 1.0

    # Interpolasi warna dari warna background (#192f4d) ke putih (#ffffff)
    r = int(25 + (255 - 25) * alpha)
    g = int(47 + (255 - 47) * alpha)
    b = int(77 + (255 - 77) * alpha)
    canvas.itemconfig(lyric_text, fill=f"#{r:02x}{g:02x}{b:02x}")

    root.after(FPS_DELAY, animate)

# ================= START =================
canvas.itemconfig(lyric_text, text=LYRICS[0])
canvas.itemconfig(lyric_shadow, text=LYRICS[0])
animate()
root.mainloop()