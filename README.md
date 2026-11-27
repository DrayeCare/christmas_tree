<div align="center">

# 🎄 Christmas Tree Animation

*A lightweight, zero-dependency procedural Christmas animation built purely with Python's `tkinter` Canvas.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2C5E3B?style=flat-square)
![Dependencies](https://img.shields.io/badge/Dependencies-None-success?style=flat-square)

</div>

---

## ✨ Features

* **3D Spiral String Lights:** 115 multi-colored bulbs (`Red`, `Gold`, `Blue`, `Warm White`, `Mint Green`, `Pink`) arranged along a trigonometric spiral with depth-based scaling (`cos(angle)`) and chasing wave pulses.
* **Layered Foliage & Lighting:** 5-tier Christmas tree with dual-tone shading to simulate directional light and depth, topped with a pulsing 10-point polygon star and halo.
* **Atmospheric Particle System:** 110 twinkling background stars and 120 snowflakes falling with randomized speeds and sinusoidal horizontal sway.
* **Synchronized Lyrics Display:** Smooth alpha-interpolated fade-in and fade-out transitions cycling through *"Last Christmas"* lyrics at ~33 FPS (`30ms` frame delay).
* **Zero External Dependencies:** Uses only Python's built-in standard libraries (`tkinter`, `random`, `math`).

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** (with `tkinter` included—standard on Windows and macOS installations).
  > *Linux users (Ubuntu/Debian/Mint):* If `tkinter` is not pre-installed, run `sudo apt install python3-tk`.

### Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/DrayeCare/christmas_tree.git](https://github.com/DrayeCare/christmas_tree.git)
   cd christmas_tree
