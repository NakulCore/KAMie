import os

images_dir = r"C:\Users\Nakul Nandan\girlfriend-website\images"
os.makedirs(images_dir, exist_ok=True)

svgs = {
    "music-cover.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f472b6" />
      <stop offset="50%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#818cf8" />
    </linearGradient>
  </defs>
  <rect width="400" height="400" rx="24" fill="url(#grad1)" />
  <circle cx="200" cy="200" r="130" fill="#1e1b4b" opacity="0.6" />
  <circle cx="200" cy="200" r="80" fill="none" stroke="#ffffff" stroke-width="2" opacity="0.4" stroke-dasharray="6 6" />
  <circle cx="200" cy="200" r="45" fill="#f43f5e" opacity="0.8" />
  <path d="M200,215 C185,195 165,170 185,150 C197,137 203,147 200,157 C197,147 203,137 215,150 C235,170 215,195 200,215 Z" fill="#ffffff" />
  <text x="200" y="360" font-family="'Segoe UI', sans-serif" font-size="20" fill="#ffffff" font-weight="600" text-anchor="middle" opacity="0.95">Our Favorite Melody &#x1F3B6;</text>
</svg>""",

    "first-hangout.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="g-hangout" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fda4af" />
      <stop offset="50%" stop-color="#e879f9" />
      <stop offset="100%" stop-color="#6366f1" />
    </linearGradient>
  </defs>
  <rect width="600" height="600" rx="28" fill="url(#g-hangout)" />
  <rect x="30" y="30" width="540" height="540" rx="20" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="8 8" />
  <circle cx="300" cy="230" r="110" fill="rgba(255,255,255,0.2)" />
  <!-- Cute Cafe Coffee Cups -->
  <path d="M240,230 L250,290 C250,305 275,305 275,290 L285,230 Z" fill="#ffffff" opacity="0.9" />
  <path d="M285,245 C298,245 298,270 283,270" stroke="#ffffff" stroke-width="4" fill="none" stroke-linecap="round" />
  <path d="M315,230 L325,290 C325,305 350,305 350,290 L360,230 Z" fill="#ffffff" opacity="0.9" />
  <path d="M360,245 C373,245 373,270 358,270" stroke="#ffffff" stroke-width="4" fill="none" stroke-linecap="round" />
  <!-- Heart above cups -->
  <path d="M300,190 C290,175 270,180 270,195 C270,210 300,225 300,225 C300,225 330,210 330,195 C330,180 310,175 300,190 Z" fill="#f43f5e" />
  <text x="300" y="410" font-family="'Segoe UI', sans-serif" font-size="30" fill="#ffffff" font-weight="bold" text-anchor="middle">Our First Hangout &#x2728;</text>
  <text x="300" y="450" font-family="'Segoe UI', sans-serif" font-size="18" fill="rgba(255,255,255,0.9)" text-anchor="middle">That one magical day everything felt right</text>
  <text x="300" y="520" font-family="'Segoe UI', sans-serif" font-size="14" fill="rgba(255,255,255,0.7)" text-anchor="middle">[ Click to swap with your real photo ]</text>
</svg>""",

    "place1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-p1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#818cf8" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-p1)" />
  <circle cx="250" cy="150" r="65" fill="#fde047" opacity="0.9" />
  <path d="M0,280 Q125,230 250,270 T500,280 L500,400 L0,400 Z" fill="rgba(30,27,75,0.7)" />
  <path d="M0,320 Q200,280 350,330 T500,320 L500,400 L0,400 Z" fill="rgba(15,23,42,0.9)" />
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Sunset By The Shore &#x1F30A;</text>
</svg>""",

    "place2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-p2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f472b6" />
      <stop offset="100%" stop-color="#fb923c" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-p2)" />
  <polygon points="250,80 180,240 320,240" fill="rgba(255,255,255,0.3)" />
  <polygon points="180,140 100,270 260,270" fill="rgba(255,255,255,0.2)" />
  <polygon points="320,130 250,270 390,270" fill="rgba(255,255,255,0.2)" />
  <text x="250" y="350" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Viewpoints &amp; Scenic Drives &#x1F3D4;&#xFE0F;</text>
</svg>""",

    "place3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-p3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7" />
      <stop offset="100%" stop-color="#ec4899" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-p3)" />
  <circle cx="150" cy="120" r="3" fill="#ffffff" opacity="0.8" />
  <circle cx="350" cy="80" r="4" fill="#ffffff" opacity="0.9" />
  <circle cx="280" cy="160" r="2" fill="#ffffff" opacity="0.7" />
  <rect x="160" y="160" width="180" height="160" rx="12" fill="rgba(255,255,255,0.25)" />
  <polygon points="250,110 140,165 360,165" fill="rgba(255,255,255,0.4)" />
  <text x="250" y="365" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Our Secret Cozy Spot &#x2615;&#x2728;</text>
</svg>""",

    "gift1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-g1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ec4899" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-g1)" />
  <rect x="170" y="140" width="160" height="140" rx="16" fill="rgba(255,255,255,0.9)" />
  <rect x="235" y="140" width="30" height="140" fill="#fb7185" />
  <rect x="170" y="195" width="160" height="30" fill="#fb7185" />
  <ellipse cx="220" cy="125" rx="25" ry="16" fill="none" stroke="rgba(255,255,255,0.95)" stroke-width="7" />
  <ellipse cx="280" cy="125" rx="25" ry="16" fill="none" stroke="rgba(255,255,255,0.95)" stroke-width="7" />
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Handmade Keepsake Box &#x1F381;</text>
</svg>""",

    "gift2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-g2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7" />
      <stop offset="100%" stop-color="#6366f1" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-g2)" />
  <rect x="150" y="110" width="200" height="160" rx="16" fill="rgba(255,255,255,0.9)" />
  <path d="M250,150 C230,120 180,130 180,170 C180,210 250,240 250,240 C250,240 320,210 320,170 C320,130 270,120 250,150 Z" fill="#f43f5e" />
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Handwritten Letter &amp; Sketches &#x1F48C;</text>
</svg>""",

    "gift3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-g3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#ec4899" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-g3)" />
  <!-- Cute origami star / heart -->
  <circle cx="250" cy="170" r="60" fill="rgba(255,255,255,0.3)" />
  <path d="M250,135 L260,160 L285,165 L267,180 L273,205 L250,190 L227,205 L233,180 L215,165 L240,160 Z" fill="#ffffff" />
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">A Little Craft Made Just For You &#x2728;</text>
</svg>""",

    "hangout1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-h1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fb7185" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-h1)" />
  <circle cx="210" cy="180" r="50" fill="rgba(255,255,255,0.3)" />
  <circle cx="290" cy="180" r="50" fill="rgba(255,255,255,0.3)" />
  <path d="M250,165 C240,150 215,155 215,175 C215,195 250,215 250,215 C250,215 285,195 285,175 C285,155 260,150 250,165 Z" fill="#ffffff" />
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Late Night Talks &amp; Boba &#x1F9CB;</text>
</svg>""",

    "hangout2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-h2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399" />
      <stop offset="100%" stop-color="#38bdf8" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-h2)" />
  <circle cx="250" cy="160" r="70" fill="rgba(255,255,255,0.25)" />
  <circle cx="230" cy="150" r="10" fill="#ffffff" />
  <circle cx="270" cy="150" r="10" fill="#ffffff" />
  <path d="M230,185 Q250,210 270,185" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" />
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Sunset Picnic In The Park &#x1F9FA;&#x1F338;</text>
</svg>""",

    "hangout3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="g-h3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f43f5e" />
      <stop offset="100%" stop-color="#a855f7" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#g-h3)" />
  <circle cx="250" cy="170" r="60" fill="rgba(255,255,255,0.2)" />
  <!-- Film roll / camera icon -->
  <rect x="210" y="140" width="80" height="60" rx="10" fill="#ffffff" />
  <circle cx="250" cy="170" r="18" fill="#a855f7" />
  <circle cx="275" cy="150" r="4" fill="#fb7185" />
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Endless Laughter &amp; Snaps &#x1F4F8;&#x2764;&#xFE0F;</text>
</svg>"""
}

for name, content in svgs.items():
    p = os.path.join(images_dir, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip())
print(f"Generated {len(svgs)} SVG placeholders successfully!")
