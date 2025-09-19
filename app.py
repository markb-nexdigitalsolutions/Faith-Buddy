import random
from textwrap import dedent
import streamlit as st

st.set_page_config(page_title="🙏 Faith Buddy", page_icon="🕊️", layout="centered")

# ---------- Data (adapted from your HTML version) ----------
BIBLE_VERSES = {
    "anxious": [
        ("Be careful for nothing; but in every thing by prayer and supplication with thanksgiving let your requests be made known unto God. "
         "And the peace of God, which passeth all understanding, shall keep your hearts and minds through Christ Jesus.",
         "Philippians 4:6-7 KJV"),
        ("Casting all your care upon him; for he careth for you.", "1 Peter 5:7 KJV"),
        ("In the multitude of my thoughts within me thy comforts delight my soul.", "Psalm 94:19 KJV"),
        ("Fear thou not; for I am with thee: be not dismayed; for I am thy God: I will strengthen thee; yea, I will help thee; yea, I will uphold thee with the right hand of my righteousness.",
         "Isaiah 41:10 KJV"),
    ],
    "sad": [
        ("The Lord is nigh unto them that are of a broken heart; and saveth such as be of a contrite spirit.", "Psalm 34:18 KJV"),
        ("He healeth the broken in heart, and bindeth up their wounds.", "Psalm 147:3 KJV"),
        ("Weeping may endure for a night, but joy cometh in the morning.", "Psalm 30:5 KJV"),
        ("Come unto me, all ye that labour and are heavy laden, and I will give you rest.", "Matthew 11:28 KJV"),
    ],
    "grateful": [
        ("O give thanks unto the Lord; for he is good: for his mercy endureth for ever.", "Psalm 107:1 KJV"),
        ("In every thing give thanks: for this is the will of God in Christ Jesus concerning you.", "1 Thessalonians 5:18 KJV"),
        ("O come, let us sing unto the Lord... make a joyful noise unto him with psalms.", "Psalm 95:1-2 KJV"),
        ("Enter into his gates with thanksgiving... be thankful unto him, and bless his name.", "Psalm 100:4 KJV"),
    ],
    "overwhelmed": [
        ("Come unto me, all ye that labour and are heavy laden, and I will give you rest.", "Matthew 11:28 KJV"),
        ("Cast thy burden upon the Lord, and he shall sustain thee...", "Psalm 55:22 KJV"),
        ("My grace is sufficient for thee: for my strength is made perfect in weakness.", "2 Corinthians 12:9 KJV"),
        ("They that wait upon the Lord shall renew their strength... they shall run, and not be weary...", "Isaiah 40:31 KJV"),
    ],
    "lonely": [
        ("Be strong and of a good courage... for the Lord thy God, he it is that doth go with thee; he will not fail thee, nor forsake thee.",
         "Deuteronomy 31:6 KJV"),
        ("Yea, though I walk through the valley... for thou art with me; thy rod and thy staff they comfort me.", "Psalm 23:4 KJV"),
        ("God setteth the solitary in families...", "Psalm 68:6 KJV"),
        ("I will never leave thee, nor forsake thee.", "Hebrews 13:5 KJV"),
    ],
    "default": [
        ("For I know the thoughts that I think toward you... to give you an expected end.", "Jeremiah 29:11 KJV"),
        ("Trust in the Lord with all thine heart; and lean not unto thine own understanding.", "Proverbs 3:5 KJV"),
        ("I can do all things through Christ which strengtheneth me.", "Philippians 4:13 KJV"),
        ("All things work together for good to them that love God...", "Romans 8:28 KJV"),
    ],
}

MOTIVATIONAL = {
    "anxious": [
        "Remember, God has not given you a spirit of fear, but of power, love, and a sound mind. Take one breath at a time—He’s working for your good.",
        "Anxiety whispers about tomorrow, but God speaks truth over today. You are loved, protected, and not alone.",
    ],
    "sad": [
        "Your tears are seen. Joy comes in the morning—this season will pass, and you will emerge stronger.",
        "It’s okay to not be okay. God meets you at your lowest with unfailing love.",
    ],
    "grateful": [
        "Your grateful heart reflects God’s goodness. Gratitude turns ordinary moments into gifts.",
        "Gratitude aligns our hearts with God’s. Your thankful spirit becomes light for others.",
    ],
    "overwhelmed": [
        "God’s strength is made perfect in weakness. Cast your burdens on Him and find rest.",
        "Being overwhelmed is human; let it remind you to lean on God—one moment at a time.",
    ],
    "lonely": [
        "God is your constant companion. You are never truly alone.",
        "Loneliness can be sacred space—draw close to God and let Him comfort you.",
    ],
    "default": [
        "God has amazing plans even when you can’t see them. Trust His timing and love.",
        "You are fearfully and wonderfully made. His grace is sufficient today.",
    ],
}

MINI_SERMONS = {
    "anxious": [{
        "title": "Finding Peace in the Storm",
        "content": dedent("""\
            Anxiety can feel like crashing waves—but Jesus calmed storms with a word.
            Anchor your thoughts not in “what if” but “even if.” Even if plans change, God is still good; even if you can’t see the path, He is still leading.
            Your anxiety is not stronger than His love for you."""),
    }],
    "sad": [{
        "title": "Beauty from Ashes",
        "content": dedent("""\
            Sadness isn’t the enemy of faith; it’s often the birthplace of deeper trust.
            God doesn’t waste pain—He transforms it, like a pearl formed through irritation.
            Let Him turn mourning into dancing in due season."""),
    }],
    "grateful": [{
        "title": "The Power of a Thankful Heart",
        "content": dedent("""\
            Gratitude doesn’t deny problems; it spotlights God’s faithfulness in them.
            Your thanks today is a seed for tomorrow’s joy. Keep remembering His goodness."""),
    }],
    "overwhelmed": [{
        "title": "One Step at a Time",
        "content": dedent("""\
            God gives grace for today, not tomorrow’s entire load. Pray for daily bread.
            Breathe, ask for the next right step, and trust that tomorrow’s grace meets tomorrow’s need."""),
    }],
    "lonely": [{
        "title": "Never Truly Alone",
        "content": dedent("""\
            Loneliness can become holy ground where we discover God’s companionship.
            He never leaves nor forsakes—you are seen, known, and loved."""),
    }],
    "default": [{
        "title": "God’s Perfect Timing",
        "content": dedent("""\
            Delays aren’t denials. God prepares us while He prepares the blessing.
            Trust the One who orchestrates what you cannot yet see."""),
    }],
}

def detect_emotion(text: str) -> str:
    t = text.lower()
    if any(w in t for w in ["anxious", "worried", "nervous", "stress"]): return "anxious"
    if any(w in t for w in ["sad", "depressed", "down", "hurt"]): return "sad"
    if any(w in t for w in ["grateful", "thankful", "blessed", "appreciate"]): return "grateful"
    if any(w in t for w in ["overwhelmed", "too much", "burden", "exhausted"]): return "overwhelmed"
    if any(w in t for w in ["lonely", "alone", "isolated", "disconnected"]): return "lonely"
    return "default"

def pick_verses(emotion: str, k: int = 3):
    pool = BIBLE_VERSES.get(emotion, BIBLE_VERSES["default"])
    random.shuffle(pool)
    return pool[:min(k, len(pool))]

def pick_message(emotion: str):
    pool = MOTIVATIONAL.get(emotion, MOTIVATIONAL["default"])
    return random.choice(pool)

def pick_sermon(emotion: str):
    pool = MINI_SERMONS.get(emotion, MINI_SERMONS["default"])
    return random.choice(pool)

# ---------- UI ----------
st.markdown(
    """
    <div style="padding:1.6rem;border-radius:16px;
         background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff;text-align:center;">
      <h1 style="margin:0;font-weight:800;">🙏 Faith Buddy</h1>
      <p style="margin-top:.4rem;opacity:.95;">Your daily companion for spiritual guidance and encouragement</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.subheader("📝 How are you feeling today?")
text = st.text_area(
    "Share what's on your heart…",
    placeholder="e.g., “I’m feeling anxious about work” or “I’m grateful but need strength.”",
    height=140,
    label_visibility="collapsed",
)

if st.button("✨ Get Spiritual Guidance", use_container_width=True):
    if not text.strip():
        st.error("Please type how you feel first.")
    else:
        emotion = detect_emotion(text)
        verses = pick_verses(emotion, k=3)
        message = pick_message(emotion)
        sermon = pick_sermon(emotion)

        st.success("Guidance generated for you. Scroll down. 🙏")
        st.write("---")

        # Bible Verses
        st.markdown("### 📖 Bible Verses for You")
        for v, ref in verses:
            st.markdown(
                f"> *{v}*\n\n— **{ref}**"
            )

        # Encouragement
        st.markdown("### 💪 Encouragement")
        st.write(message)

        # Mini Sermon
        st.markdown("### 🕊️ Mini Sermon")
        st.markdown(f"**{sermon['title']}**")
        for para in sermon["content"].split("\n\n"):
            st.write(para)

        # Share (copy) / New guidance
        st.write("")
        share_text = "\n\n".join([f"“{v}” — {ref}" for v, ref in verses]) + f"\n\n{message}\n\n{sermon['title']}\n{sermon['content']}\n\nShared from Faith Buddy 🙏"
        st.download_button("📤 Copy/Download Guidance (.txt)", share_text, file_name="faith_buddy_guidance.txt", use_container_width=True)

        if st.button("🔄 Get New Guidance", use_container_width=True):
            st.experimental_rerun()

# Footer
st.write("")
st.markdown(
    "<div style='text-align:center;opacity:.7;'>May God’s peace be with you today and always 🤍</div>",
    unsafe_allow_html=True,
)
