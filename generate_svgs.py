import os

images_dir = r"C:\Users\Nakul Nandan\KamieKAM\images"
os.makedirs(images_dir, exist_ok=True)

svgs = {
    # 1. First Hangout: MAP Museum of Art & Photography + Diet Coke + KJ
    "first-hangout.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600">
  <defs>
    <linearGradient id="bg-map" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="40%" stop-color="#312e81" />
      <stop offset="100%" stop-color="#4c1d95" />
    </linearGradient>
    <linearGradient id="gold-frame" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24" />
      <stop offset="50%" stop-color="#fef08a" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
    <linearGradient id="coke-red" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444" />
      <stop offset="100%" stop-color="#991b1b" />
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.4" />
    </filter>
  </defs>
  <rect width="600" height="600" rx="28" fill="url(#bg-map)" />
  <circle cx="500" cy="120" r="180" fill="#ec4899" opacity="0.15" />
  <circle cx="100" cy="480" r="140" fill="#38bdf8" opacity="0.12" />

  <!-- Museum Classical / Modern Gallery Arch & Frame -->
  <rect x="70" y="60" width="460" height="330" rx="16" fill="rgba(255,255,255,0.06)" stroke="url(#gold-frame)" stroke-width="3" filter="url(#shadow)" />
  
  <!-- Museum Gallery Wall with Painting and Statuesque Modern Art -->
  <line x1="70" y1="340" x2="530" y2="340" stroke="rgba(255,255,255,0.2)" stroke-width="2" />
  
  <!-- Museum Pillars & Architecture -->
  <path d="M120,340 L120,120 M140,340 L140,120" stroke="rgba(255,255,255,0.25)" stroke-width="2" />
  <path d="M460,340 L460,120 M480,340 L480,120" stroke="rgba(255,255,255,0.25)" stroke-width="2" />

  <!-- Art Canvas inside Museum -->
  <rect x="180" y="100" width="240" height="150" rx="8" fill="#1e1b4b" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
  <!-- Abstract Art on Wall -->
  <circle cx="300" cy="165" r="45" fill="#f43f5e" opacity="0.7" />
  <polygon points="260,190 300,125 340,190" fill="#38bdf8" opacity="0.75" />
  <path d="M250,175 Q300,110 350,175" stroke="#fde047" stroke-width="3" fill="none" />

  <!-- Diet Coke Can -->
  <g transform="translate(240, 245)">
    <rect x="0" y="10" width="38" height="65" rx="6" fill="url(#coke-red)" stroke="#ffffff" stroke-width="1.5" />
    <rect x="4" y="5" width="30" height="7" rx="3" fill="#e5e7eb" />
    <rect x="0" y="32" width="38" height="16" fill="#ffffff" opacity="0.9" />
    <text x="19" y="44" font-family="'Segoe UI', sans-serif" font-size="9" font-weight="900" fill="#b91c1c" text-anchor="middle">DIET</text>
  </g>

  <!-- KJ Drink / Coffee Cup -->
  <g transform="translate(320, 240)">
    <path d="M0,15 L6,70 C6,76 36,76 36,70 L42,15 Z" fill="#ffffff" stroke="rgba(255,255,255,0.8)" stroke-width="2" />
    <rect x="-2" y="10" width="46" height="8" rx="4" fill="#a855f7" />
    <!-- Straw -->
    <line x1="28" y1="0" x2="22" y2="25" stroke="#f43f5e" stroke-width="3" stroke-linecap="round" />
    <!-- Heart sticker on cup -->
    <path d="M21,46 C18,42 12,43 12,48 C12,53 21,58 21,58 C21,58 30,53 30,48 C30,43 24,42 21,46 Z" fill="#ec4899" />
    <text x="21" y="36" font-family="'Segoe UI', sans-serif" font-size="9" font-weight="bold" fill="#6b21a8" text-anchor="middle">KJ</text>
  </g>

  <!-- Sweet Sparkles and Hearts -->
  <path d="M300,225 C292,210 274,213 274,226 C274,240 300,252 300,252 C300,252 326,240 326,226 C326,213 308,210 300,225 Z" fill="#f43f5e" filter="url(#shadow)" />

  <!-- Typography & Badges -->
  <rect x="150" y="415" width="300" height="34" rx="17" fill="rgba(244, 114, 182, 0.2)" stroke="#f472b6" stroke-width="1.5" />
  <text x="300" y="437" font-family="'Segoe UI', sans-serif" font-size="14" fill="#fbcfe8" font-weight="600" text-anchor="middle">&#x2728; FIRST MEETUP &bull; MAP MUSEUM &#x2728;</text>

  <text x="300" y="485" font-family="'Segoe UI', sans-serif" font-size="28" fill="#ffffff" font-weight="bold" text-anchor="middle">MAP &bull; Art &amp; Photography</text>
  <text x="300" y="520" font-family="'Segoe UI', sans-serif" font-size="16" fill="rgba(255,255,255,0.85)" text-anchor="middle">Diet Coke, KJ &amp; The Smile That Started Everything</text>
  <text x="300" y="555" font-family="'Segoe UI', sans-serif" font-size="13" fill="#cbd5e1" font-style="italic" text-anchor="middle">"Surrounded by masterpieces, yet you were the only view."</text>
</svg>""",

    # 2. Place 1: Corner House DBC (2nd Hangout)
    "place1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-dbc" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#451a03" />
      <stop offset="50%" stop-color="#78350f" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <linearGradient id="fudge" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#271106" />
      <stop offset="100%" stop-color="#180a03" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-dbc)" />
  <circle cx="420" cy="80" r="110" fill="#fbbf24" opacity="0.15" />

  <!-- Glass Dessert Bowl -->
  <path d="M170,200 Q250,290 330,200 L320,180 L180,180 Z" fill="rgba(255,255,255,0.3)" stroke="rgba(255,255,255,0.8)" stroke-width="2" />
  <!-- Bowl Base -->
  <path d="M245,255 L245,290 L220,300 L280,300 L255,290 L255,255" fill="rgba(255,255,255,0.4)" stroke="rgba(255,255,255,0.7)" stroke-width="2" />

  <!-- Brownie base layer -->
  <rect x="190" y="175" width="120" height="25" rx="6" fill="#381c0d" />
  
  <!-- Ice Cream Scoops -->
  <circle cx="220" cy="155" r="35" fill="#fef3c7" />
  <circle cx="280" cy="155" r="35" fill="#fffbeb" />
  <circle cx="250" cy="130" r="38" fill="#fef08a" />

  <!-- Hot Molten Chocolate Fudge Drizzle -->
  <path d="M225,120 Q240,150 240,180 Q255,140 265,175 Q275,130 290,165" stroke="url(#fudge)" stroke-width="12" fill="none" stroke-linecap="round" />
  
  <!-- Cherry on Top -->
  <circle cx="250" cy="92" r="14" fill="#dc2626" />
  <path d="M254,82 Q270,65 285,75" stroke="#16a34a" stroke-width="3" fill="none" stroke-linecap="round" />

  <!-- Two Spoons for Sharing -->
  <path d="M150,140 L210,185" stroke="#e2e8f0" stroke-width="4" stroke-linecap="round" />
  <ellipse cx="145" cy="135" rx="10" ry="14" transform="rotate(-35 145 135)" fill="#e2e8f0" />
  <path d="M350,140 L290,185" stroke="#e2e8f0" stroke-width="4" stroke-linecap="round" />
  <ellipse cx="355" cy="135" rx="10" ry="14" transform="rotate(35 355 135)" fill="#e2e8f0" />

  <!-- Title & Text -->
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Corner House &bull; Grabbing DBC &#x1F368;&#x1F36B;</text>
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="14" fill="#fde68a" text-anchor="middle">Hangout #2 &bull; Hot Fudge, Two Spoons &amp; Endless Laughs</text>
</svg>""",

    # 3. Place 2: Sankey Tank Duck Watching (Usual Hangout)
    "place2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-sankey" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="60%" stop-color="#0d9488" />
      <stop offset="100%" stop-color="#065f46" />
    </linearGradient>
    <linearGradient id="water-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-sankey)" />

  <!-- Sun & Warm Ambient Sky -->
  <circle cx="380" cy="110" r="50" fill="#fde047" opacity="0.6" />
  
  <!-- Distant Trees Shoreline -->
  <path d="M0,210 Q100,185 200,205 T400,195 T500,205 L500,400 L0,400 Z" fill="#064e3b" />
  
  <!-- Lake Water Surface -->
  <path d="M0,230 Q125,225 250,230 T500,228 L500,400 L0,400 Z" fill="url(#water-grad)" opacity="0.85" />
  
  <!-- Water Ripples -->
  <path d="M50,260 Q90,255 130,260" stroke="#bae6fd" stroke-width="2" fill="none" opacity="0.7" />
  <path d="M220,280 Q270,275 320,280" stroke="#bae6fd" stroke-width="2" fill="none" opacity="0.7" />
  <path d="M360,250 Q400,246 440,250" stroke="#bae6fd" stroke-width="2" fill="none" opacity="0.7" />

  <!-- Mama Duck -->
  <g transform="translate(180, 220)">
    <!-- Body -->
    <ellipse cx="40" cy="30" rx="28" ry="18" fill="#ffffff" />
    <!-- Wing -->
    <path d="M30,22 Q50,20 58,28 Q45,34 30,30" fill="#e2e8f0" />
    <!-- Head -->
    <circle cx="62" cy="16" r="14" fill="#ffffff" />
    <!-- Eye -->
    <circle cx="66" cy="14" r="2" fill="#0f172a" />
    <!-- Beak -->
    <path d="M74,15 L86,18 L74,21 Z" fill="#f97316" />
    <!-- Ripple below -->
    <ellipse cx="45" cy="46" rx="35" ry="4" fill="none" stroke="#bae6fd" stroke-width="2" opacity="0.8" />
  </g>

  <!-- Baby Duck -->
  <g transform="translate(285, 235)">
    <!-- Body -->
    <ellipse cx="20" cy="18" rx="16" ry="11" fill="#fef08a" />
    <!-- Head -->
    <circle cx="33" cy="10" r="9" fill="#fef08a" />
    <!-- Eye -->
    <circle cx="36" cy="8" r="1.5" fill="#0f172a" />
    <!-- Beak -->
    <path d="M41,9 L49,11 L41,13 Z" fill="#ea580c" />
    <!-- Ripple below -->
    <ellipse cx="22" cy="28" rx="20" ry="3" fill="none" stroke="#bae6fd" stroke-width="2" opacity="0.8" />
  </g>

  <!-- Title & Text -->
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Sankey Tank &bull; Duck Watching &#x1F986;&#x1F33F;</text>
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="14" fill="#a7f3d0" text-anchor="middle">Our Usual Peaceful Haven &bull; Lakeside Breezes &amp; Calm Talks</text>
</svg>""",

    # 4. Place 3: The Aquarium Date
    "place3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-aqua" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#082f49" />
      <stop offset="50%" stop-color="#0369a1" />
      <stop offset="100%" stop-color="#0c4a6e" />
    </linearGradient>
    <radialGradient id="light-ray" cx="50%" cy="0%" r="80%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0" />
    </radialGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-aqua)" />
  <rect width="500" height="400" fill="url(#light-ray)" />

  <!-- Sea Anemones & Coral -->
  <path d="M50,400 Q70,300 85,400 Q105,320 120,400" stroke="#f472b6" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.7" />
  <path d="M380,400 Q400,290 415,400 Q435,310 450,400" stroke="#a78bfa" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.7" />

  <!-- Tropical Clownfish 1 -->
  <g transform="translate(150, 140)">
    <ellipse cx="40" cy="25" rx="36" ry="22" fill="#ea580c" />
    <path d="M72,25 L92,10 L92,40 Z" fill="#ea580c" />
    <!-- White Stripes -->
    <path d="M28,8 Q35,25 28,42 L34,42 Q41,25 34,8 Z" fill="#ffffff" />
    <path d="M52,6 Q57,25 52,44 L58,44 Q63,25 58,6 Z" fill="#ffffff" />
    <!-- Fin -->
    <path d="M40,28 Q48,38 40,42 Z" fill="#ffffff" />
    <!-- Eye -->
    <circle cx="18" cy="20" r="3" fill="#ffffff" />
    <circle cx="17" cy="20" r="1.5" fill="#000000" />
  </g>

  <!-- Blue Tang Fish 2 -->
  <g transform="translate(280, 190)">
    <ellipse cx="40" cy="25" rx="34" ry="20" fill="#2563eb" />
    <path d="M70,25 L88,12 L88,38 Z" fill="#facc15" />
    <!-- Yellow Fin -->
    <path d="M38,20 Q52,15 58,26 Q46,30 38,20 Z" fill="#facc15" />
    <circle cx="20" cy="22" r="2.5" fill="#000000" />
  </g>

  <!-- Glowing Water Bubbles -->
  <circle cx="120" cy="220" r="8" fill="none" stroke="#bae6fd" stroke-width="1.5" opacity="0.7" />
  <circle cx="260" cy="110" r="12" fill="none" stroke="#bae6fd" stroke-width="1.5" opacity="0.7" />
  <circle cx="390" cy="180" r="6" fill="none" stroke="#bae6fd" stroke-width="1.5" opacity="0.7" />

  <!-- Title & Text -->
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Our Aquarium Date &bull; Deep Blue Magic &#x1F420;&#x1FAE7;</text>
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="14" fill="#7dd3fc" text-anchor="middle">Glowing Marine Life &amp; Holding Hands Under Aquatic Lights</text>
</svg>""",

    # 5. Place 4: The Rainy Trek, Peacocks & Mysore Express Mutton Biriyani
    "place4.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-rain-trek" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="40%" stop-color="#0f766e" />
      <stop offset="100%" stop-color="#14532d" />
    </linearGradient>
    <linearGradient id="peacock-fan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4" />
      <stop offset="50%" stop-color="#10b981" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-rain-trek)" />

  <!-- Rolling Misty Mountains -->
  <path d="M0,230 Q120,130 240,210 T480,160 L500,200 L500,400 L0,400 Z" fill="#064e3b" opacity="0.7" />
  <path d="M0,260 Q150,180 300,240 T500,220 L500,400 L0,400 Z" fill="#022c22" />

  <!-- Rain Strands Falling -->
  <g stroke="#93c5fd" stroke-width="1.8" opacity="0.55" stroke-linecap="round">
    <line x1="60" y1="50" x2="40" y2="110" />
    <line x1="120" y1="80" x2="100" y2="140" />
    <line x1="200" y1="40" x2="180" y2="100" />
    <line x1="320" y1="70" x2="300" y2="130" />
    <line x1="420" y1="50" x2="400" y2="110" />
    <line x1="160" y1="130" x2="140" y2="190" />
    <line x1="370" y1="120" x2="350" y2="180" />
  </g>

  <!-- Mysore Express Hot Mutton Biriyani Pot on Left -->
  <g transform="translate(80, 195)">
    <ellipse cx="40" cy="65" rx="35" ry="14" fill="#d97706" stroke="#92400e" stroke-width="2" />
    <path d="M5,65 Q40,95 75,65" fill="#b45309" />
    <!-- Steam -->
    <path d="M25,48 Q30,30 25,18" stroke="#ffffff" stroke-width="2.5" fill="none" opacity="0.8" stroke-linecap="round" />
    <path d="M40,45 Q45,26 40,12" stroke="#ffffff" stroke-width="2.5" fill="none" opacity="0.8" stroke-linecap="round" />
    <path d="M55,48 Q60,30 55,18" stroke="#ffffff" stroke-width="2.5" fill="none" opacity="0.8" stroke-linecap="round" />
    <!-- Badge -->
    <rect x="0" y="75" width="80" height="20" rx="10" fill="#991b1b" />
    <text x="40" y="89" font-family="'Segoe UI', sans-serif" font-size="9" fill="#fef08a" font-weight="bold" text-anchor="middle">MYSORE EXP</text>
  </g>

  <!-- Elegant Wild Peacock on Right -->
  <g transform="translate(320, 170)">
    <!-- Fan of Feathers -->
    <path d="M50,70 Q10,20 40,-10 Q80,10 65,70" fill="url(#peacock-fan)" opacity="0.9" />
    <path d="M55,70 Q70,-20 100,-15 Q105,25 65,70" fill="url(#peacock-fan)" opacity="0.85" />
    <circle cx="45" cy="5" r="7" fill="#fbbf24" />
    <circle cx="45" cy="5" r="4" fill="#0284c7" />
    <circle cx="85" cy="0" r="7" fill="#fbbf24" />
    <circle cx="85" cy="0" r="4" fill="#0284c7" />
    <!-- Peacock Body -->
    <path d="M55,75 Q50,45 65,35 Q75,45 68,75 Z" fill="#1d4ed8" />
    <!-- Head & Crest -->
    <circle cx="68" cy="30" r="8" fill="#1e40af" />
    <line x1="68" y1="22" x2="68" y2="14" stroke="#fbbf24" stroke-width="2" />
    <circle cx="68" cy="13" r="2.5" fill="#06b6d4" />
    <!-- Beak -->
    <path d="M74,30 L82,32 L74,34 Z" fill="#f97316" />
  </g>

  <!-- Title & Text -->
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="21" fill="#ffffff" font-weight="bold" text-anchor="middle">Rainy Trek &amp; Peacocks &bull; Mysore Express &#x1F99A;&#x1F327;&#xFE0F;</text>
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="13" fill="#6ee7b7" text-anchor="middle">Mutton Biriyani Feast, Unprepared In The Pouring Rain &amp; Wild Peacocks</text>
</svg>""",

    # 6. Gift 1: Handmade Lilies (crafted to never fade)
    "gift1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-lily" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#831843" />
      <stop offset="50%" stop-color="#be185d" />
      <stop offset="100%" stop-color="#db2777" />
    </linearGradient>
    <linearGradient id="petal-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="70%" stop-color="#fdf2f8" />
      <stop offset="100%" stop-color="#f472b6" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-lily)" />
  <circle cx="250" cy="170" r="120" fill="rgba(255,255,255,0.1)" />

  <!-- Stems -->
  <path d="M250,290 Q240,220 220,160" stroke="#15803d" stroke-width="6" fill="none" stroke-linecap="round" />
  <path d="M250,290 Q265,230 280,170" stroke="#16a34a" stroke-width="5" fill="none" stroke-linecap="round" />
  <!-- Leaves -->
  <path d="M242,240 Q210,240 195,225 Q220,220 242,240" fill="#22c55e" />
  <path d="M255,225 Q285,220 305,205 Q285,210 255,225" fill="#22c55e" />

  <!-- Left Lily Flower Blossom -->
  <g transform="translate(160, 90)">
    <!-- Petals -->
    <path d="M60,70 Q30,10 50,0 Q70,40 60,70" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <path d="M60,70 Q10,40 0,60 Q40,75 60,70" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <path d="M60,70 Q40,110 65,115 Q75,85 60,70" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <path d="M60,70 Q100,50 115,70 Q80,85 60,70" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <path d="M60,70 Q80,15 100,10 Q85,45 60,70" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <!-- Stamens / Pistil -->
    <line x1="60" y1="70" x2="52" y2="35" stroke="#fef08a" stroke-width="2" />
    <circle cx="52" cy="35" r="3" fill="#ca8a04" />
    <line x1="60" y1="70" x2="68" y2="38" stroke="#fef08a" stroke-width="2" />
    <circle cx="68" cy="38" r="3" fill="#ca8a04" />
  </g>

  <!-- Right Lily Flower Blossom -->
  <g transform="translate(235, 100)">
    <path d="M50,65 Q30,10 45,0 Q65,35 50,65" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <path d="M50,65 Q5,35 0,55 Q35,70 50,65" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <path d="M50,65 Q35,100 55,105 Q65,80 50,65" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <path d="M50,65 Q85,45 100,65 Q70,75 50,65" fill="url(#petal-grad)" stroke="#fbcfe8" stroke-width="1.5" />
    <!-- Stamens -->
    <line x1="50" y1="65" x2="42" y2="32" stroke="#fef08a" stroke-width="2" />
    <circle cx="42" cy="32" r="2.5" fill="#ca8a04" />
  </g>

  <!-- Craft Ribbon Tie -->
  <path d="M250,290 C235,280 220,300 240,305 C250,307 265,307 275,305 C295,300 280,280 265,290 Z" fill="#fde047" />

  <!-- Title & Text -->
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Handmade Lilies &bull; Crafted To Last &#x1F338;&#x2728;</text>
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="13.5" fill="#fce7f3" text-anchor="middle">"Because real lilies fade, but handmade lilies bloom forever."</text>
</svg>""",

    # 7. Gift 2: Batman Sketch (Birthday — 31st March 2026)
    "gift2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-batman" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09090b" />
      <stop offset="50%" stop-color="#18181b" />
      <stop offset="100%" stop-color="#27272a" />
    </linearGradient>
    <linearGradient id="sketch-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fdfbf7" />
      <stop offset="100%" stop-color="#f4eedb" />
    </linearGradient>
    <filter id="canvas-shadow">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000" flood-opacity="0.6" />
    </filter>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-batman)" />

  <!-- Ambient Yellow Bat-Signal Glow in Background -->
  <circle cx="250" cy="160" r="105" fill="#eab308" opacity="0.18" />

  <!-- Artist's Sketch Pad / Paper -->
  <rect x="140" y="55" width="220" height="235" rx="8" fill="url(#sketch-canvas)" filter="url(#canvas-shadow)" />
  <!-- Sketchbook Spiral Rings -->
  <g fill="#71717a">
    <circle cx="170" cy="62" r="3" /><circle cx="210" cy="62" r="3" /><circle cx="250" cy="62" r="3" /><circle cx="290" cy="62" r="3" /><circle cx="330" cy="62" r="3" />
  </g>

  <!-- Hand-drawn Batman Emblem / Cowl Silhouette -->
  <g transform="translate(180, 95)">
    <!-- Iconic Batman Logo Path -->
    <path d="M70,25 L78,5 L88,18 C100,10 115,10 135,18 L140,25 C132,45 110,65 70,85 C30,65 8,45 0,25 L5,18 C25,10 40,10 52,18 L62,5 Z" fill="#09090b" />
    
    <!-- Pencil Sketch shading lines -->
    <path d="M20,35 L40,50 M30,30 L55,45 M85,45 L110,30 M100,50 L120,35" stroke="#3f3f46" stroke-width="1.5" stroke-linecap="round" />
    <!-- Heart next to sketch -->
    <path d="M70,95 C65,88 54,90 54,97 C54,105 70,113 70,113 C70,113 86,105 86,97 C86,90 75,88 70,95 Z" fill="#e11d48" />
  </g>

  <!-- Pencil lying on paper -->
  <g transform="translate(325, 200) rotate(35)">
    <rect x="0" y="0" width="70" height="7" fill="#fbbf24" stroke="#d97706" stroke-width="1" />
    <polygon points="70,0 80,3.5 70,7" fill="#fde68a" />
    <polygon points="77,2.5 80,3.5 77,4.5" fill="#18181b" />
  </g>

  <!-- Handwritten Birthday Note on sketchpad -->
  <text x="250" y="245" font-family="'Caveat', cursive, sans-serif" font-size="16" fill="#18181b" font-weight="bold" text-anchor="middle">For your birthday &bull; 31st March 2026 &#x2764;&#xFE0F;</text>

  <!-- Title & Text -->
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">The Batman Sketch &bull; 31st March 2026 &#x1F987;&#x1F5A4;</text>
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="14" fill="#facc15" text-anchor="middle">Birthday Gift Deeply Close To My Heart &bull; Pure Thoughtfulness</text>
</svg>""",

    # 8. Gift 3: Hot Wheels Surprise (Astonished & Loved)
    "gift3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-hotwheels" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b91c1c" />
      <stop offset="50%" stop-color="#c2410c" />
      <stop offset="100%" stop-color="#ea580c" />
    </linearGradient>
    <linearGradient id="car-body" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>
    <linearGradient id="flame" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fde047" />
      <stop offset="100%" stop-color="#ef4444" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-hotwheels)" />

  <!-- Speed Motion Lines -->
  <line x1="50" y1="120" x2="180" y2="120" stroke="#fef08a" stroke-width="3" stroke-linecap="round" opacity="0.8" />
  <line x1="80" y1="140" x2="220" y2="140" stroke="#fef08a" stroke-width="4" stroke-linecap="round" opacity="0.9" />
  <line x1="40" y1="230" x2="150" y2="230" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.7" />

  <!-- Hot Wheels Styled Flame Trail -->
  <path d="M120,200 Q180,180 240,195 Q200,165 280,185" fill="none" stroke="url(#flame)" stroke-width="8" stroke-linecap="round" />

  <!-- Hot Wheels Sports Car -->
  <g transform="translate(160, 130)">
    <!-- Main Chassis -->
    <path d="M10,65 Q30,40 70,38 L120,38 Q155,20 185,38 L230,55 Q245,60 240,75 L10,75 Z" fill="url(#car-body)" />
    <!-- Cabin Glass / Windshield -->
    <path d="M75,38 L115,38 L145,28 L110,28 Z" fill="#93c5fd" opacity="0.9" />
    <path d="M118,38 L160,38 L150,28 L120,28 Z" fill="#bae6fd" opacity="0.9" />
    <!-- Racing Stripe & Flame Decal -->
    <path d="M30,60 L210,50 L200,55 L20,65 Z" fill="#facc15" />
    <!-- Rear Spoiler -->
    <path d="M5,45 L25,45 L20,55 L10,55 Z" fill="#1e3a8a" />
    <!-- Wheels -->
    <circle cx="65" cy="75" r="18" fill="#18181b" stroke="#71717a" stroke-width="4" />
    <circle cx="65" cy="75" r="8" fill="#e2e8f0" />
    <circle cx="195" cy="75" r="18" fill="#18181b" stroke="#71717a" stroke-width="4" />
    <circle cx="195" cy="75" r="8" fill="#e2e8f0" />
  </g>

  <!-- Heart badge -->
  <path d="M250,90 C242,75 224,78 224,91 C224,105 250,117 250,117 C250,117 276,105 276,91 C276,78 258,75 250,90 Z" fill="#ffffff" />

  <!-- Title & Text -->
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">The Hot Wheels Surprise &#x1F3CE;&#xFE0F;&#x2764;&#xFE0F;</text>
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="14" fill="#fef08a" text-anchor="middle">Astonished, Overjoyed &amp; Genuinely Loved &bull; Inner Child Rejoicing</text>
</svg>""",

    # 9. Hangout 1: Football Matches & Sideline Support
    "hangout1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-football" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14532d" />
      <stop offset="50%" stop-color="#15803d" />
      <stop offset="100%" stop-color="#166534" />
    </linearGradient>
    <radialGradient id="floodlight" cx="50%" cy="10%" r="70%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#14532d" stop-opacity="0" />
    </radialGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-football)" />
  <rect width="500" height="400" fill="url(#floodlight)" />

  <!-- Pitch White Lines -->
  <circle cx="250" cy="200" r="75" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="3" />
  <line x1="50" y1="200" x2="450" y2="200" stroke="rgba(255,255,255,0.4)" stroke-width="3" />
  <circle cx="250" cy="200" r="6" fill="rgba(255,255,255,0.6)" />

  <!-- Classic Football -->
  <g transform="translate(190, 115)">
    <circle cx="45" cy="45" r="40" fill="#ffffff" stroke="#18181b" stroke-width="2.5" />
    <!-- Pentagons -->
    <polygon points="45,30 32,38 36,52 54,52 58,38" fill="#18181b" />
    <polygon points="45,15 38,5 52,5" fill="#18181b" />
    <polygon points="18,35 7,32 10,45" fill="#18181b" />
    <polygon points="72,35 83,32 80,45" fill="#18181b" />
    <polygon points="25,65 20,78 32,78" fill="#18181b" />
    <polygon points="65,65 70,78 58,78" fill="#18181b" />
  </g>

  <!-- Cheering Megaphone / Heart on Sidelines -->
  <g transform="translate(300, 110)">
    <path d="M10,25 L35,10 L35,40 Z" fill="#f43f5e" />
    <ellipse cx="35" cy="25" rx="5" ry="15" fill="#fb7185" />
    <rect x="0" y="20" width="10" height="10" rx="3" fill="#ffffff" />
    <!-- Sound Waves of Love -->
    <path d="M48,15 Q55,25 48,35" stroke="#fde047" stroke-width="3" fill="none" stroke-linecap="round" />
    <path d="M56,8 Q68,25 56,42" stroke="#fde047" stroke-width="3" fill="none" stroke-linecap="round" />
  </g>

  <!-- Floating Heart for Her Presence -->
  <path d="M165,115 C158,102 142,105 142,116 C142,128 165,138 165,138 C165,138 188,128 188,116 C188,105 172,102 165,115 Z" fill="#f43f5e" />

  <!-- Title & Text -->
  <text x="250" y="340" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">Showing Up For My Football Matches &#x26BD;&#x1F496;</text>
  <text x="250" y="370" font-family="'Segoe UI', sans-serif" font-size="14" fill="#bbf7d0" text-anchor="middle">My Favorite Sideline Supporter &bull; Deeply Grateful For Your Presence</text>
</svg>""",

    # 10. Hangout 2: Movie Dates & Spider-Man
    "hangout2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-movies" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18181b" />
      <stop offset="50%" stop-color="#31101f" />
      <stop offset="100%" stop-color="#581c87" />
    </linearGradient>
    <linearGradient id="spidey-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444" />
      <stop offset="100%" stop-color="#1e40af" />
    </linearGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-movies)" />

  <!-- Cinema Ticket Stubs -->
  <g transform="translate(90, 80) rotate(-12)">
    <rect x="0" y="0" width="130" height="75" rx="8" fill="#fde047" stroke="#ca8a04" stroke-width="2" />
    <line x1="45" y1="0" x2="45" y2="75" stroke="#ca8a04" stroke-width="2" stroke-dasharray="5 5" />
    <text x="22" y="44" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold" fill="#854d0e" text-anchor="middle">ADMIT 1</text>
    <text x="88" y="35" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#713f12" text-anchor="middle">SPIDER-MAN</text>
    <text x="88" y="52" font-family="'Segoe UI', sans-serif" font-size="9" fill="#854d0e" text-anchor="middle">CINEMA DATE</text>
  </g>

  <!-- Popcorn Box -->
  <g transform="translate(290, 95)">
    <!-- Popcorn Kernels -->
    <circle cx="25" cy="18" r="12" fill="#fef08a" />
    <circle cx="45" cy="12" r="14" fill="#ffffff" />
    <circle cx="65" cy="16" r="13" fill="#fef08a" />
    <circle cx="35" cy="5" r="12" fill="#ffffff" />
    <circle cx="55" cy="4" r="11" fill="#fef08a" />
    <!-- Tub -->
    <polygon points="15,25 30,95 70,95 85,25" fill="#dc2626" />
    <polygon points="26,25 37,95 48,95 40,25" fill="#ffffff" />
    <polygon points="56,25 52,95 63,95 70,25" fill="#ffffff" />
  </g>

  <!-- Spider-Man Mask / Web Center Badge -->
  <g transform="translate(210, 150)">
    <circle cx="40" cy="40" r="38" fill="url(#spidey-grad)" stroke="#ffffff" stroke-width="2" />
    <!-- Web lines -->
    <path d="M40,2 L40,78 M2,40 L78,40 M14,14 L66,66 M14,66 L66,14" stroke="#ffffff" stroke-width="1.2" opacity="0.6" />
    <circle cx="40" cy="40" r="16" fill="none" stroke="#ffffff" stroke-width="1.2" opacity="0.6" />
    <circle cx="40" cy="40" r="28" fill="none" stroke="#ffffff" stroke-width="1.2" opacity="0.6" />
    <!-- Spidey Eyes -->
    <polygon points="25,32 37,42 22,46" fill="#ffffff" stroke="#000000" stroke-width="2" />
    <polygon points="55,32 43,42 58,46" fill="#ffffff" stroke="#000000" stroke-width="2" />
  </g>

  <!-- Title & Quote -->
  <text x="250" y="325" font-family="'Segoe UI', sans-serif" font-size="21" fill="#ffffff" font-weight="bold" text-anchor="middle">Top Notch Movie Dates &bull; Popcorn &amp; Thrills &#x1F37F;&#x1F577;&#xFE0F;</text>
  <text x="250" y="353" font-family="'Caveat', cursive, sans-serif" font-size="19" fill="#f472b6" font-weight="bold" text-anchor="middle">"At the end of the day, it's the one you saw Spider-Man with."</text>
  <text x="250" y="378" font-family="'Segoe UI', sans-serif" font-size="12" fill="#cbd5e1" text-anchor="middle">Dhurandhar 2 &bull; Obsession &bull; Insidious 3 &bull; Spider-Man</text>
</svg>""",

    # 11. Hangout 3: Asking Her Out - June 11th, 2026 at the Ice Cream Place
    "hangout3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 400">
  <defs>
    <linearGradient id="bg-propose" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#831843" />
      <stop offset="50%" stop-color="#be185d" />
      <stop offset="100%" stop-color="#6366f1" />
    </linearGradient>
    <radialGradient id="glow-circle" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fde047" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#fde047" stop-opacity="0" />
    </radialGradient>
  </defs>
  <rect width="500" height="400" rx="24" fill="url(#bg-propose)" />
  <circle cx="250" cy="160" r="130" fill="url(#glow-circle)" />

  <!-- Calendar Page: June 11th, 2026 -->
  <g transform="translate(90, 85)">
    <rect x="0" y="0" width="100" height="110" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="2" />
    <rect x="0" y="0" width="100" height="28" rx="10" fill="#e11d48" />
    <text x="50" y="20" font-family="'Segoe UI', sans-serif" font-size="12" fill="#ffffff" font-weight="bold" text-anchor="middle">JUNE 2026</text>
    <text x="50" y="75" font-family="'Segoe UI', sans-serif" font-size="40" fill="#18181b" font-weight="900" text-anchor="middle">11</text>
    <!-- Heart around 11 -->
    <path d="M50,92 C45,86 36,88 36,94 C36,101 50,107 50,107 C50,107 64,101 64,94 C64,88 55,86 50,92 Z" fill="#e11d48" />
  </g>

  <!-- Ice Cream Waffle Cones -->
  <g transform="translate(230, 90)">
    <!-- Left Cone -->
    <polygon points="30,70 15,130 45,130" fill="#d97706" />
    <circle cx="30" cy="65" r="20" fill="#fda4af" />
    <circle cx="30" cy="45" r="16" fill="#f43f5e" />
    <!-- Right Cone -->
    <polygon points="70,70 55,130 85,130" fill="#d97706" />
    <circle cx="70" cy="65" r="20" fill="#fef08a" />
    <circle cx="70" cy="45" r="16" fill="#a855f7" />
  </g>

  <!-- Ring / Sparkle of Proposal -->
  <g transform="translate(345, 95)">
    <circle cx="35" cy="45" r="22" fill="none" stroke="#fde047" stroke-width="4" />
    <polygon points="35,12 45,23 35,26 25,23" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
    <circle cx="35" cy="18" r="4" fill="#ffffff" />
  </g>

  <!-- Big "SHE SAID YES!" Banner -->
  <rect x="130" y="225" width="240" height="40" rx="20" fill="#ffffff" />
  <text x="250" y="252" font-family="'Segoe UI', sans-serif" font-size="18" fill="#be185d" font-weight="900" text-anchor="middle">&#x1F48D; SHE SAID YES! &#x1F48D;</text>

  <!-- Title & Text -->
  <text x="250" y="325" font-family="'Segoe UI', sans-serif" font-size="22" fill="#ffffff" font-weight="bold" text-anchor="middle">The Ice Cream Place &bull; June 11th, 2026 &#x1F366;&#x2764;&#xFE0F;</text>
  <text x="250" y="355" font-family="'Segoe UI', sans-serif" font-size="14" fill="#fbcfe8" text-anchor="middle">The Moment You Said Yes &bull; The Best Day of My Entire Life</text>
  <text x="250" y="380" font-family="'Segoe UI', sans-serif" font-size="12" fill="#e0e7ff" font-style="italic" text-anchor="middle">"Choosing you was the easiest question I will ever answer."</text>
</svg>"""
}

for name, content in svgs.items():
    p = os.path.join(images_dir, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip())
print(f"Generated {len(svgs)} custom romantic SVGs successfully in {images_dir}!")
