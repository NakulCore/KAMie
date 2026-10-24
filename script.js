/**
 * ===================================================================
 * A Romantic Website for My Girlfriend ✨
 * Interactive Core Script
 * ===================================================================
 */

// Configuration defaults (Easily customisable)
const CONFIG = {
  // Milestone Date: 11th June 2026 (User's special date)
  targetDate: '2026-06-11T00:00:00',
  songTitle: "Stargazing",
  songArtist: "Kygo & Justin Jesso • Dedicated For Kamie ✨",
  firstHangoutImg: 'images/first-hangout-map.jpeg',
};

// State
let isPlaying = false;
let isMuted = false;
let currentProgress = 0;
let songInterval = null;
let currentTuneIndex = 0;

/* ===================================================================
   1. ROMANTIC MUSIC ENGINE (Web Audio API Synthesizer + Audio Tag)
   Creates a sweet, dreamy music-box / lo-fi piano chord progression
   so music plays smoothly without relying on external mp3 files!
   =================================================================== */

let audioCtx = null;
let synthGainNode = null;
let synthTimer = null;

// Cute romantic chord progressions (Music Box / Dreamy Chimes)
const TUNE_PROGRESSIONS = [
  // Progression 1: Stargazing (Melodic Chime Progression: F - C - Dm - Bb)
  [
    { notes: [174.61, 261.63, 349.23, 440.00, 523.25], name: "Stargazing (Bruno Mars Melody)" }, // F maj
    { notes: [130.81, 261.63, 329.63, 392.00, 523.25], name: "Stargazing (Bruno Mars Melody)" }, // C maj
    { notes: [146.83, 220.00, 293.66, 349.23, 440.00], name: "Stargazing (Bruno Mars Melody)" }, // D min
    { notes: [116.54, 233.08, 293.66, 349.23, 466.16], name: "Stargazing (Bruno Mars Melody)" }, // Bb maj
  ],
  // Progression 2: Starlit Night
  [
    { notes: [220.00, 261.63, 329.63, 392.00], name: "Starlit Memories" },  // Am7
    { notes: [174.61, 220.00, 261.63, 329.63], name: "Starlit Memories" },  // Fmaj7
    { notes: [261.63, 329.63, 392.00, 493.88], name: "Starlit Memories" },  // Cmaj7
    { notes: [196.00, 246.94, 293.66, 392.00], name: "Starlit Memories" },  // G
  ]
];

function initAudioContext() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    audioCtx = new AudioContext();
    synthGainNode = audioCtx.createGain();
    synthGainNode.gain.setValueAtTime(isMuted ? 0 : 0.15, audioCtx.currentTime);
    synthGainNode.connect(audioCtx.destination);
  }
}

// Play a single soft bell/music-box chime
function playSoftChime(freq, delaySeconds = 0) {
  if (!audioCtx || isMuted) return;

  const osc = audioCtx.createOscillator();
  const noteGain = audioCtx.createGain();

  // Warm chime: Sine mixed with slight Triangle
  osc.type = 'sine';
  osc.frequency.setValueAtTime(freq, audioCtx.currentTime + delaySeconds);

  const startTime = audioCtx.currentTime + delaySeconds;
  const duration = 1.4;

  noteGain.gain.setValueAtTime(0.001, startTime);
  noteGain.gain.exponentialRampToValueAtTime(0.2, startTime + 0.04);
  noteGain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

  osc.connect(noteGain);
  noteGain.connect(synthGainNode);

  osc.start(startTime);
  osc.stop(startTime + duration + 0.1);
}

// Play an arpeggiated romantic chord
function playRomanticStep(stepIdx) {
  const currentProg = TUNE_PROGRESSIONS[currentTuneIndex % TUNE_PROGRESSIONS.length];
  const chordObj = currentProg[stepIdx % currentProg.length];
  const notes = chordObj.notes;

  // Arpeggiate the chord notes gently
  notes.forEach((freq, idx) => {
    playSoftChime(freq, idx * 0.28);
  });
}

function startSynthesizer() {
  initAudioContext();
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }

  let step = 0;
  playRomanticStep(step);
  synthTimer = setInterval(() => {
    step++;
    playRomanticStep(step);
  }, 1600);
}

function stopSynthesizer() {
  if (synthTimer) {
    clearInterval(synthTimer);
    synthTimer = null;
  }
}

/* ===================================================================
   2. MUSIC CONTROLLER (UI, VINYL & AUDIO SYNC)
   =================================================================== */

const playPauseBtn = document.getElementById('play-pause-btn');
const playIcon = document.getElementById('play-icon');
const miniPlayBtn = document.getElementById('mini-play-btn');
const miniDisc = document.getElementById('mini-disc');
const mainVinyl = document.getElementById('main-vinyl');
const soundWaves = document.getElementById('sound-waves');
const progressFill = document.getElementById('progress-fill');
const currentTimeEl = document.getElementById('current-time');
const seekContainer = document.getElementById('seek-container');
const volumeToggleBtn = document.getElementById('volume-toggle-btn');
const volIcon = document.getElementById('vol-icon');
const audioSource = document.getElementById('audio-source');
const totalDurationEl = document.getElementById('total-duration');

// Wire HTML5 audio events for seamless playback & real progress sync
if (audioSource) {
  audioSource.addEventListener('loadedmetadata', () => {
    if (totalDurationEl && !isNaN(audioSource.duration)) {
      const dMins = Math.floor(audioSource.duration / 60);
      const dSecs = Math.floor(audioSource.duration % 60);
      totalDurationEl.textContent = `${dMins}:${dSecs < 10 ? '0' : ''}${dSecs}`;
    }
  });

  audioSource.addEventListener('timeupdate', () => {
    if (!isNaN(audioSource.duration) && audioSource.duration > 0) {
      const percent = (audioSource.currentTime / audioSource.duration) * 100;
      if (progressFill) progressFill.style.width = `${percent}%`;
      const mins = Math.floor(audioSource.currentTime / 60);
      const secs = Math.floor(audioSource.currentTime % 60);
      if (currentTimeEl) currentTimeEl.textContent = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }
  });

  audioSource.addEventListener('play', () => {
    isPlaying = true;
    updateMusicUI(true);
  });

  audioSource.addEventListener('pause', () => {
    isPlaying = false;
    updateMusicUI(false);
  });

  audioSource.addEventListener('ended', () => {
    audioSource.currentTime = 0;
    audioSource.play().catch(() => {});
  });
}

function toggleMusic() {
  initAudioContext();

  const hasExternalAudio = audioSource && audioSource.src && !audioSource.src.endsWith('#');

  if (!isPlaying) {
    isPlaying = true;
    updateMusicUI(true);

    if (hasExternalAudio) {
      audioSource.play().catch((err) => {
        console.warn('Audio play failed, falling back to synthesizer:', err);
        startSynthesizer();
        startProgressTracker();
      });
    } else {
      startSynthesizer();
      startProgressTracker();
    }
  } else {
    isPlaying = false;
    updateMusicUI(false);

    if (audioSource) {
      audioSource.pause();
    }
    stopSynthesizer();
    stopProgressTracker();
  }
}

function updateMusicUI(playing) {
  if (playing) {
    playIcon.className = 'fa-solid fa-pause';
    miniPlayBtn.innerHTML = '<i class="fa-solid fa-pause"></i>';
    mainVinyl.classList.add('spinning');
    miniDisc.classList.add('spinning');
    soundWaves.classList.add('active');
  } else {
    playIcon.className = 'fa-solid fa-play';
    miniPlayBtn.innerHTML = '<i class="fa-solid fa-play"></i>';
    mainVinyl.classList.remove('spinning');
    miniDisc.classList.remove('spinning');
    soundWaves.classList.remove('active');
  }
}

function startProgressTracker() {
  if (songInterval) clearInterval(songInterval);
  songInterval = setInterval(() => {
    currentProgress += 0.5;
    if (currentProgress > 194) {
      currentProgress = 0; // Loop after ~3 mins
    }
    updateProgressDisplay();
  }, 500);
}

function stopProgressTracker() {
  if (songInterval) {
    clearInterval(songInterval);
    songInterval = null;
  }
}

function updateProgressDisplay() {
  const percent = (currentProgress / 194) * 100;
  progressFill.style.width = `${percent}%`;

  const mins = Math.floor(currentProgress / 60);
  const secs = Math.floor(currentProgress % 60);
  currentTimeEl.textContent = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
}

// Seek bar click
if (seekContainer) {
  seekContainer.addEventListener('click', (e) => {
    const rect = seekContainer.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const width = rect.width;
    const clickPercent = Math.max(0, Math.min(1, clickX / width));
    if (audioSource && !isNaN(audioSource.duration) && audioSource.duration > 0) {
      audioSource.currentTime = clickPercent * audioSource.duration;
    } else {
      currentProgress = clickPercent * 194;
      updateProgressDisplay();
    }
  });
}

// Volume Mute/Unmute
function toggleVolume() {
  isMuted = !isMuted;
  if (volIcon) {
    volIcon.className = isMuted ? 'fa-solid fa-volume-xmark' : 'fa-solid fa-volume-high';
  }
  if (synthGainNode && audioCtx) {
    synthGainNode.gain.setValueAtTime(isMuted ? 0 : 0.15, audioCtx.currentTime);
  }
  if (audioSource) {
    audioSource.muted = isMuted;
  }
}

// Next/Prev theme or skip 15s in the song
function nextTune() {
  if (audioSource && !isNaN(audioSource.duration) && audioSource.duration > 0) {
    audioSource.currentTime = Math.min(audioSource.duration, audioSource.currentTime + 15);
  } else {
    currentTuneIndex++;
    currentProgress = 0;
    updateProgressDisplay();
  }
}

function prevTune() {
  if (audioSource && !isNaN(audioSource.duration) && audioSource.duration > 0) {
    audioSource.currentTime = Math.max(0, audioSource.currentTime - 15);
  } else {
    currentTuneIndex = Math.max(0, currentTuneIndex - 1);
    currentProgress = 0;
    updateProgressDisplay();
  }
}

// Event Listeners for Music
if (playPauseBtn) playPauseBtn.addEventListener('click', toggleMusic);
if (miniPlayBtn) miniPlayBtn.addEventListener('click', toggleMusic);
if (miniDisc) miniDisc.addEventListener('click', toggleMusic);
if (mainVinyl) mainVinyl.addEventListener('click', toggleMusic);
if (volumeToggleBtn) volumeToggleBtn.addEventListener('click', toggleVolume);

const nextTuneBtn = document.getElementById('next-tune-btn');
const prevTuneBtn = document.getElementById('prev-tune-btn');
if (nextTuneBtn) nextTuneBtn.addEventListener('click', nextTune);
if (prevTuneBtn) prevTuneBtn.addEventListener('click', prevTune);

/* ===================================================================
   3. COUNTDOWN / COUNTUP TIMER (11th June 2026)
   =================================================================== */

const tDays = document.getElementById('t-days');
const tHours = document.getElementById('t-hours');
const tMins = document.getElementById('t-mins');
const tSecs = document.getElementById('t-secs');
const timerLabel = document.getElementById('timer-label');
const timerSubtext = document.getElementById('timer-subtext');

function updateLoveTimer() {
  const targetDate = new Date(CONFIG.targetDate).getTime();
  const now = new Date().getTime();
  const diff = now - targetDate;

  if (diff >= 0) {
    // Target date has arrived or passed: Display time elapsed since June 11, 2026
    if (timerLabel) timerLabel.textContent = "Time With You Since 11th June 2026";
    if (timerSubtext) timerSubtext.textContent = "Every single second since you said YES at the ice cream place has been the greatest gift in my life ✨";

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    tDays.textContent = days < 10 ? '0' + days : days;
    tHours.textContent = hours < 10 ? '0' + hours : hours;
    tMins.textContent = minutes < 10 ? '0' + minutes : minutes;
    tSecs.textContent = seconds < 10 ? '0' + seconds : seconds;
  } else {
    // Future date: Countdown remaining to June 11, 2026
    const remaining = Math.abs(diff);
    if (timerLabel) timerLabel.textContent = "Counting Down To June 11, 2026";
    if (timerSubtext) timerSubtext.textContent = "Counting down every second till our special milestone day ✨";

    const days = Math.floor(remaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((remaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((remaining % (1000 * 60)) / 1000);

    tDays.textContent = days < 10 ? '0' + days : days;
    tHours.textContent = hours < 10 ? '0' + hours : hours;
    tMins.textContent = minutes < 10 ? '0' + minutes : minutes;
    tSecs.textContent = seconds < 10 ? '0' + seconds : seconds;
  }
}

// Run timer every second
setInterval(updateLoveTimer, 1000);
updateLoveTimer();

/* ===================================================================
   4. SLIDE NAVIGATION & STICKY MINI-PLAYER
   =================================================================== */

const navDots = document.querySelectorAll('.nav-dot');
const floatingMusicBar = document.getElementById('floating-music-bar');
const slides = document.querySelectorAll('.slide');

// Smooth scroll to slide
function scrollToSlide(slideId) {
  const target = document.getElementById(slideId);
  if (target) {
    target.scrollIntoView({ behavior: 'smooth' });
  }
}

navDots.forEach(dot => {
  dot.addEventListener('click', () => {
    const targetId = dot.getAttribute('data-target');
    scrollToSlide(targetId);
  });
});

// Intersection Observer for active nav dot & floating mini-player
const observerOptions = {
  root: null,
  threshold: 0.4
};

const slideObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const activeId = entry.target.id;

      // Update nav dots
      navDots.forEach(dot => {
        if (dot.getAttribute('data-target') === activeId) {
          dot.classList.add('active');
        } else {
          dot.classList.remove('active');
        }
      });

      // Show/hide floating mini-player
      if (activeId !== 'slide-1') {
        floatingMusicBar.classList.add('visible');
      } else {
        floatingMusicBar.classList.remove('visible');
      }
    }
  });
}, observerOptions);

slides.forEach(slide => slideObserver.observe(slide));

/* ===================================================================
   5. INTERACTIVE LOVE LETTER (SLIDE 6)
   =================================================================== */

function toggleLoveLetter() {
  const envelope = document.getElementById('love-envelope');
  const letterCard = document.getElementById('letter-card');
  const waxSeal = document.getElementById('wax-seal');
  const promptText = document.getElementById('seal-prompt-text');

  if (letterCard.classList.contains('open')) {
    letterCard.classList.remove('open');
    if (envelope) {
      envelope.classList.remove('open');
      envelope.setAttribute('aria-expanded', 'false');
    }
    if (waxSeal) {
      waxSeal.innerHTML = '<div class="wax-seal-emboss"><i class="fa-solid fa-heart"></i></div>';
    }
    if (promptText) {
      promptText.textContent = 'Click seal to open 💌';
    }
  } else {
    letterCard.classList.add('open');
    if (envelope) {
      envelope.classList.add('open');
      envelope.setAttribute('aria-expanded', 'true');
    }
    if (waxSeal) {
      waxSeal.innerHTML = '<div class="wax-seal-emboss"><i class="fa-solid fa-envelope-open"></i></div>';
    }
    if (promptText) {
      promptText.textContent = 'Letter Unfolded ✨';
    }

    // Spawn cheerful celebration hearts
    spawnHeartsAroundElement(envelope, 14);

    // Smoothly scroll letter into view if needed
    setTimeout(() => {
      letterCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 200);
  }
}

/* ===================================================================
   6. INTERACTIVE REASONS CARDS (SLIDE 7)
   =================================================================== */

function flipCard(cardEl) {
  cardEl.classList.toggle('flipped');
  spawnHeartsAroundElement(cardEl, 4);
}

/* ===================================================================
   7. FLOATING HEARTS & CELEBRATION EFFECTS
   =================================================================== */

const HEART_ICONS = ['❤️', '💙', '✨', '💫', '🍷', '🤍', '⭐', '🥰', '💖'];

function createHeartParticle(x, y) {
  const heart = document.createElement('div');
  heart.className = 'floating-heart';
  heart.textContent = HEART_ICONS[Math.floor(Math.random() * HEART_ICONS.length)];
  
  const size = Math.random() * 20 + 16;
  heart.style.fontSize = `${size}px`;
  heart.style.left = `${x}px`;
  heart.style.top = `${y}px`;
  const glowList = [
    'rgba(106, 46, 53, 0.65)',   /* Wine Plum */
    'rgba(27, 152, 224, 0.7)',    /* Blue Bell */
    'rgba(36, 123, 160, 0.65)',   /* Cerulean */
    'rgba(217, 140, 110, 0.7)'    /* Warm Linen */
  ];
  heart.style.filter = `drop-shadow(0 4px 12px ${glowList[Math.floor(Math.random() * glowList.length)]})`;

  document.body.appendChild(heart);

  setTimeout(() => {
    heart.remove();
  }, 2000);
}

// Click anywhere to burst hearts
document.addEventListener('click', (e) => {
  // Don't trigger on buttons or inputs directly to avoid clutter
  if (['BUTTON', 'INPUT', 'A'].includes(e.target.tagName)) return;
  createHeartParticle(e.clientX, e.clientY);
});

// Burst from an element
function spawnHeartsAroundElement(element, count = 8) {
  const rect = element.getBoundingClientRect();
  for (let i = 0; i < count; i++) {
    const rx = rect.left + Math.random() * rect.width;
    const ry = rect.top + Math.random() * rect.height;
    setTimeout(() => {
      createHeartParticle(rx, ry);
    }, i * 70);
  }
}

// Memory reaction button
function sendHeartBurst(e) {
  e.stopPropagation();
  const btn = e.currentTarget;
  spawnHeartsAroundElement(btn, 10);
  btn.style.transform = 'scale(1.2)';
  setTimeout(() => {
    btn.style.transform = '';
  }, 250);
}

// Grand Finale Love Explosion
function triggerGrandCelebration() {
  const celebrateBtn = document.getElementById('celebrate-btn');
  if (celebrateBtn) {
    celebrateBtn.style.transform = 'scale(1.15)';
    setTimeout(() => { celebrateBtn.style.transform = ''; }, 300);
  }

  // Massive burst across screen
  for (let i = 0; i < 60; i++) {
    setTimeout(() => {
      const rx = Math.random() * window.innerWidth;
      const ry = window.innerHeight * 0.4 + Math.random() * (window.innerHeight * 0.5);
      createHeartParticle(rx, ry);
    }, i * 35);
  }
}

/* ===================================================================
   8. BACKGROUND SPARKLE CANVAS
   =================================================================== */

const canvas = document.getElementById('sparkle-canvas');
let ctx = canvas ? canvas.getContext('2d') : null;
let particles = [];

function resizeCanvas() {
  if (!canvas) return;
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

class SparkleParticle {
  constructor() {
    this.reset();
  }

  reset() {
    this.x = Math.random() * (canvas ? canvas.width : window.innerWidth);
    this.y = Math.random() * (canvas ? canvas.height : window.innerHeight);
    this.size = Math.random() * 2.2 + 0.5;
    this.alpha = Math.random() * 0.8 + 0.2;
    this.alphaSpeed = (Math.random() * 0.02 + 0.005) * (Math.random() > 0.5 ? 1 : -1);
    this.speedY = Math.random() * -0.4 - 0.1;
    const glowColors = [
      'rgba(106, 46, 53, 0.65)',   /* Wine Plum */
      'rgba(27, 152, 224, 0.75)',  /* Blue Bell */
      'rgba(36, 123, 160, 0.7)',    /* Cerulean */
      'rgba(217, 140, 110, 0.75)'   /* Warm Linen */
    ];
    this.glowColor = glowColors[Math.floor(Math.random() * glowColors.length)];
  }

  update() {
    this.y += this.speedY;
    this.alpha += this.alphaSpeed;

    if (this.alpha <= 0.1 || this.alpha >= 0.9) {
      this.alphaSpeed = -this.alphaSpeed;
    }

    if (this.y < 0) {
      this.reset();
      this.y = canvas.height;
    }
  }

  draw() {
    if (!ctx) return;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fillStyle = this.glowColor;
    ctx.shadowBlur = 8;
    ctx.shadowColor = this.glowColor;
    ctx.fill();
    ctx.shadowBlur = 0;
  }
}

function initSparkles() {
  if (!canvas || !ctx) return;
  resizeCanvas();
  particles = [];
  const count = Math.floor(window.innerWidth / 20);
  for (let i = 0; i < count; i++) {
    particles.push(new SparkleParticle());
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      p.update();
      p.draw();
    });
    requestAnimationFrame(animate);
  }
  animate();
}

window.addEventListener('resize', () => {
  resizeCanvas();
});

initSparkles();

/* ===================================================================
   9. QUICK IN-BROWSER CUSTOMIZER MODAL
   Allows testing photo links and text right in the browser!
   =================================================================== */

const customizerModal = document.getElementById('customizer-modal');
const customizerBtn = document.getElementById('customizer-btn');

function toggleCustomizerModal() {
  if (!customizerModal) return;
  customizerModal.classList.toggle('open');
}

if (customizerBtn) {
  customizerBtn.addEventListener('click', toggleCustomizerModal);
}

function applyCustomSettings() {
  const dateInput = document.getElementById('custom-date-input').value.trim();
  const photoInput = document.getElementById('input-first-hangout').value.trim();
  const songTitleInput = document.getElementById('input-song-title').value.trim();
  const songArtistInput = document.getElementById('input-song-artist').value.trim();

  if (dateInput) {
    CONFIG.targetDate = dateInput;
    updateLoveTimer();
    localStorage.setItem('love_target_date', dateInput);
  }

  if (photoInput) {
    const hangoutImg = document.getElementById('first-hangout-img');
    if (hangoutImg) hangoutImg.src = photoInput;
    localStorage.setItem('love_first_photo', photoInput);
  }

  if (songTitleInput) {
    document.getElementById('display-song-title').textContent = songTitleInput;
    document.getElementById('mini-title').textContent = songTitleInput;
    localStorage.setItem('love_song_title', songTitleInput);
  }

  if (songArtistInput) {
    document.getElementById('display-song-artist').textContent = songArtistInput;
    localStorage.setItem('love_song_artist', songArtistInput);
  }

  toggleCustomizerModal();
  triggerGrandCelebration();
}

function resetCustomSettings() {
  localStorage.clear();
  location.reload();
}

// Restore saved edits from localStorage on load
window.addEventListener('DOMContentLoaded', () => {
  const savedDate = localStorage.getItem('love_target_date');
  const savedPhoto = localStorage.getItem('love_first_photo');
  const savedSongTitle = localStorage.getItem('love_song_title');
  const savedSongArtist = localStorage.getItem('love_song_artist');

  if (savedDate) {
    CONFIG.targetDate = savedDate;
    const dateInput = document.getElementById('custom-date-input');
    if (dateInput) dateInput.value = savedDate;
    updateLoveTimer();
  }

  if (savedPhoto) {
    const hangoutImg = document.getElementById('first-hangout-img');
    if (hangoutImg) hangoutImg.src = savedPhoto;
    const photoInput = document.getElementById('input-first-hangout');
    if (photoInput) photoInput.value = savedPhoto;
  }

  if (savedSongTitle) {
    document.getElementById('display-song-title').textContent = savedSongTitle;
    document.getElementById('mini-title').textContent = savedSongTitle;
    const titleInput = document.getElementById('input-song-title');
    if (titleInput) titleInput.value = savedSongTitle;
  }

  if (savedSongArtist) {
    document.getElementById('display-song-artist').textContent = savedSongArtist;
    const artistInput = document.getElementById('input-song-artist');
    if (artistInput) artistInput.value = savedSongArtist;
  }

  // Initialize Lightbox for full photo and video view
  initLightbox();
});

/* ===================================================================
   10. LIGHTBOX FULL VIEW HANDLER
   =================================================================== */
function openLightbox(src, type, caption) {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-img');
  const vid = document.getElementById('lightbox-video');
  const cap = document.getElementById('lightbox-caption');
  if (!modal) return;

  if (type === 'video') {
    if (img) img.style.display = 'none';
    if (vid) {
      vid.style.display = 'block';
      vid.src = src;
      vid.play().catch(() => {});
    }
  } else {
    if (vid) {
      vid.pause();
      vid.style.display = 'none';
      vid.src = '';
    }
    if (img) {
      img.style.display = 'block';
      img.src = src;
    }
  }

  if (cap) cap.textContent = caption || '';
  modal.classList.add('active');
}

function closeLightbox(e) {
  if (e && e.target && (e.target.id === 'lightbox-img' || e.target.id === 'lightbox-video')) {
    return;
  }
  const modal = document.getElementById('lightbox-modal');
  const vid = document.getElementById('lightbox-video');
  if (vid) {
    vid.pause();
    vid.src = '';
  }
  if (modal) modal.classList.remove('active');
}

function initLightbox() {
  const phoneVideo = document.getElementById('football-video');
  if (phoneVideo) {
    phoneVideo.title = 'Full View Phone Player • Double click for theater view 📱';
    phoneVideo.addEventListener('dblclick', () => {
      openLightbox(phoneVideo.src || phoneVideo.currentSrc, 'video', 'Her cheering at football matches ⚽💖');
    });
  }
}
