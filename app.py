import streamlit as st
# ===================================================================
# 🔒 PRIVATE PASSWORD PROTECTION - EYE VUE OPTICS
# ===================================================================
SECRET_PASSWORD = "EyeVue2026!"   # ← Change this to YOUR secret password

def check_password():
    def password_entered():
        if st.session_state["password"] == SECRET_PASSWORD:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<h2 style='text-align: center; color: #1a3a5c;'>🔒 Eye Vue Optics</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Enter your private access key.</p>", unsafe_allow_html=True)
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("<h2 style='text-align: center; color: #1a3a5c;'>🔒 Eye Vue Optics</h2>", unsafe_allow_html=True)
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("❌ Password incorrect. Access denied.")
        return False
    else:
        return True

if not check_password():
    st.stop()
# ===================================================================
import math
from datetime import datetime

# ===================================================================
# EYE VUE OPTICS - BRANDING & CONFIG
# ===================================================================
st.set_page_config(
    page_title="Eye Vue Optics | Premium Home Stylist",
    page_icon="👁️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for mobile-friendly premium look
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a3a5c;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1rem;
        color: #666;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 25px;
    }
    .recommendation-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%);
        padding: 18px;
        border-radius: 12px;
        margin: 12px 0;
        border-left: 4px solid #1a3a5c;
    }
    .brand-name {
        color: #1a3a5c;
        font-weight: 700;
    }
    .price-tag {
        font-size: 1.3rem;
        color: #2d7a3e;
        font-weight: 700;
    }
    .pitch-box {
        background: #fff8e1;
        padding: 12px;
        border-radius: 8px;
        border-left: 3px solid #f9a825;
        font-style: italic;
        margin-top: 10px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #1a3a5c 0%, #2d5a8c 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 12px 24px;
        width: 100%;
    }
    .whatsapp-btn>button {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%) !important;
    }
</style>
""", unsafe_allow_html=True)

# ===================================================================
# COMPLETE PRICING DATABASE (2026-2027)
# ===================================================================

GKB_PRIME = {
    "SV_CLEAR": {
        1.56: {"Robusta": 609, "Vistaar": 662, "V-Max": 865, "Marine UV": 1647},
    },
    "SV_BLUBLOCK": {
        1.56: {"Blu-Block": 882, "V-Max BB": 1650},
        1.59: {"Poly BB": 1837},
        1.60: {"MR-8 BB": 3266},
        1.67: {"MR-7 BB": 4920},
    },
    "SV_RX": {
        1.50: {"Acura": 961, "Duron": 1345, "Vistaar": 2014, "V-Max": 2819},
        1.56: {"Duron": 2038, "Vistaar": 3083, "V-Max": 3904},
        1.60: {"Duron": 3699, "Vistaar": 5791, "V-Max": 6839},
        1.67: {"Duron": 5430, "Vistaar": 7319, "V-Max": 8723},
        1.74: {"V-Max": 20808},
    },
    "SV_PHOTO": {
        1.56: {"Daynite": 3063},
        1.59: {"Daynite Turbo Poly": 8145},
        1.60: {"Transitions GR": 22558},
        1.67: {"Daynite Turbo": 11599, "Transitions GR": 24051},
        1.74: {"Transitions GR": 45584},
    },
    "PAL_FREEFORM": {
        1.56: {"Proviz": 2416, "Proton BB": 3898, "Promax": 3622},
        1.60: {"Promax MR-8": 5335},
    },
    "PAL_SHARP": {
        1.56: {"C-Digital BB": 5906, "V-Work": 6834},
        1.60: {"C-Digital MR-8": 7646, "IP-Wide+": 13630, "Tailormade": 17785},
    },
}

ESSILOR = {
    "SV_CRIZAL": {
        1.56: {"Easy Pro": 3400, "Rock": 3900, "Sapphire HR": 5400, "Natural Look": 5900},
        1.60: {"Easy Pro": 4800, "Rock": 5300, "Sapphire HR": 6800, "Natural Look": 7300},
        1.67: {"Easy Pro": 5800, "Rock": 6300, "Sapphire HR": 7800},
    },
    "SV_EYEZEN": {
        1.56: {"Start Stock": 6900, "Start Rx": 6500, "Boost 0.4": 7000},
        1.60: {"Start Rx": 8000, "Boost 0.4": 8500, "Eyecode": 14900},
        1.67: {"Start Rx": 10000, "Boost 0.4": 10500},
    },
    "SV_OMEGA": {
        1.56: {"Omega": 6000},
        1.60: {"Omega": 7500},
        1.67: {"Omega": 9500},
        1.74: {"Omega": 16000},
    },
    "SV_TRANSITIONS": {
        1.56: {"Classic": 4600, "Gen S": 11100},
        1.60: {"Gen S": 16400},
        1.67: {"Gen S": 18400},
    },
    "PAL_VARILUX": {
        1.56: {"Comfort": 11000},
        1.60: {"Comfort": 14500, "XR": 19500},
        1.67: {"Comfort": 18500},
    },
}

ZEISS = {
    "SV_CLEARMIND": {
        1.50: {"Pure": 15800},
        1.60: {"Pure": 19400},
        1.67: {"Pure": 22400},
    },
    "SV_SMARTLIFE": {
        1.50: {"Young": 13700},
        1.60: {"Young": 16800},
        1.67: {"Young": 19400},
    },
    "DIGITAL": {
        1.50: {"ClearMind": 15200, "SmartLife": 13200},
        1.60: {"ClearMind": 18600, "SmartLife": 16100},
    },
    "PAL_CLEARMIND": {
        1.50: {"Pure": 28500, "Superb": 53400, "Individual 3": 87300},
        1.60: {"Pure": 37000, "Superb": 62500, "Individual 3": 101100},
    },
    "PAL_SMARTLIFE": {
        1.50: {"Pure": 24700, "Superb": 46400},
        1.60: {"Pure": 32100, "Superb": 54300},
    },
    "PAL_LIGHT2": {
        1.50: {"3D": 6700},
        1.60: {"3D": 10000},
    },
    "DRIVESAFE": {
        1.50: {"SV": 19800, "PAL": 19800},
        1.60: {"SV": 22400, "PAL": 22400},
    },
}

FRAME_STYLES = {
    'ROUND': {
        'rec': ['Geometric', 'Rectangular', 'Browline/Clubmaster'],
        'avoid': ['Small round frames'],
        'pitch': "Angular frames like geometric or rectangular shapes will add structure and definition to your face, creating a balanced, confident look."
    },
    'SQUARE': {
        'rec': ['Oval', 'Round Panto', 'Aviator', 'Rimless'],
        'avoid': ['Boxy rectangular frames'],
        'pitch': "Curved frames like oval or round Panto shapes will soften your strong jawline and create a more harmonious facial balance."
    },
    'OVAL': {
        'rec': ['Walnut', 'Oversized', 'Rimless', 'Most styles'],
        'avoid': ['Very narrow frames'],
        'pitch': "Your oval face is incredibly versatile. You can pull off bold oversized frames or sleek rimless styles with equal success."
    },
    'HEART': {
        'rec': ['Cat-eye', 'Light rimless', 'Oval', 'Bottom-heavy'],
        'avoid': ['Heavy decorative top rims'],
        'pitch': "Cat-eye or bottom-heavy frames will balance your wider forehead and draw attention to your cheekbones beautifully."
    },
}
# ===================================================================
# HELPER FUNCTIONS
# ===================================================================

def auto_select_index(sph_r, cyl_r, sph_l, cyl_l):
    """Select lens index based on highest absolute power across both eyes."""
    max_power = max(abs(sph_r), abs(cyl_r), abs(sph_l), abs(cyl_l))
    if max_power <= 2.00:
        return 1.56, "Standard index — cost-effective for low prescriptions", max_power
    elif max_power <= 4.00:
        return 1.60, "Mid-index (MR-8) — thinner, stronger, ideal for rimless", max_power
    elif max_power <= 6.00:
        return 1.67, "High-index — significantly thinner for moderate-high Rx", max_power
    else:
        return 1.74, "Ultra high-index — essential to avoid 'coke-bottle' effect", max_power


def validate_for_progressive(lens_height, add_power):
    """Validate if frame is suitable for progressive lenses."""
    warnings = []
    recommendations = []

    if lens_height < 28:
        warnings.append(f"⚠️ Lens height ({lens_height}mm) is below 28mm minimum")
        warnings.append("→ Requires Short-Corridor PAL (like ZEISS SmartLife)")
        recommendations.append("ZEISS SmartLife Progressive (short corridor design)")
    elif lens_height < 30:
        warnings.append(f"⚠️ Lens height ({lens_height}mm) is borderline (28-30mm)")
        recommendations.append("Standard corridor OK, but intermediate zone may be limited")
    else:
        recommendations.append(f"✓ Lens height ({lens_height}mm) is excellent for progressives")

    if add_power >= 2.75:
        warnings.append(f"⚠️ High ADD power (+{add_power:.2f}) requires wider corridor")
        recommendations.append("Consider premium progressive (ZEISS ClearMind Individual 3)")

    return warnings, recommendations


def generate_recommendations(c):
    """Generate lens recommendations based on client profile."""
    recs = []
    v = c['vtype']
    b = c['budget']
    ls = c['lifestyle']

    rec_index, index_reason, max_power = auto_select_index(
        c['sph_r'], c['cyl_r'], c['sph_l'], c['cyl_l']
    )

    # =================== PROGRESSIVE ===================
    if v == 'PROGRESSIVE':
        if b == 'VALUE':
            recs.append({
                'brand': 'GKB Prime',
                'product': f'Proton Freeform 1.56',
                'price': 3898,
                'why': 'Affordable freeform progressive with good adaptation',
                'pitch': 'GKB Prime Proton uses freeform surfacing for smooth distance-to-near transitions at an unbeatable price point.'
            })
            if rec_index >= 1.60:
                recs.append({
                    'brand': 'GKB Prime',
                    'product': f'Promax MR-8 1.60',
                    'price': 5335,
                    'why': f'Thinner freeform progressive (auto-selected 1.60 index)',
                    'pitch': f'The MR-8 material keeps your lenses thin and light for your {max_power:.2f}D prescription.'
                })
        elif b == 'PREMIUM':
            recs.append({
                'brand': 'Essilor',
                'product': 'Varilux Comfort 1.60',
                'price': 14500,
                'why': "World's most trusted progressive brand",
                'pitch': 'Essilor invented the progressive lens. Varilux Comfort gives you seamless vision with fast adaptation.'
            })
            recs.append({
                'brand': 'ZEISS',
                'product': 'SmartLife Pure 1.60',
                'price': 32100,
                'why': 'Connected-lifestyle progressive with fast adaptation',
                'pitch': '8 out of 10 wearers adapt very fast to ZEISS SmartLife. Designed for how you actually use your phone.'
            })
        else:  # ULTRA
            recs.append({
                'brand': 'ZEISS',
                'product': 'ClearMind Pure 1.60',
                'price': 37000,
                'why': 'Neuroscience-based design reducing cognitive load by 90%',
                'pitch': 'ZEISS ClearMind uses NeurOptix technology. 90% of wearers report less cognitive load and better concentration.'
            })
            recs.append({
                'brand': 'ZEISS',
                'product': 'ClearMind Individual 3 1.60',
                'price': 101100,
                'why': 'Fully personalized to your facial anatomy',
                'pitch': 'This is the pinnacle of lens technology. Every pixel is mapped to your unique face and daily activities.'
            })

    # =================== DIGITAL ===================
    elif v == 'DIGITAL':
        if b == 'VALUE':
            recs.append({
                'brand': 'GKB Prime',
                'product': 'C-Digital 1.56',
                'price': 5319,
                'why': 'Digital-optimized lens with near-vision boost',
                'pitch': 'GKB C-Digital lenses have a built-in power booster for screen distance, reducing eye fatigue.'
            })
        elif b == 'PREMIUM':
            recs.append({
                'brand': 'Essilor',
                'product': 'Eyezen Boost 0.4 1.60',
                'price': 8500,
                'why': '0.4D near boost with BlueUV Capture',
                'pitch': 'Essilor Eyezen Boost gives your eyes a subtle 0.4D assist for near tasks. 88% of wearers report relaxed vision.'
            })
        else:
            recs.append({
                'brand': 'ZEISS',
                'product': 'Digital ClearMind 1.60',
                'price': 18600,
                'why': 'NeurOptix digital lens with 28% larger clear zones',
                'pitch': 'ZEISS Digital ClearMind reduces cognitive load during screen work. 85% confirm extra stress reduction.'
            })

    # =================== SINGLE VISION ===================
    else:
        if ls == 'IT':
            if b == 'VALUE':
                recs.append({'brand': 'GKB Prime', 'product': 'Blu-Block 1.56', 'price': 882,
                    'why': 'Essential blue-light filtering',
                    'pitch': 'GKB Blu-Block filters harmful blue-violet light from monitors and phones at an incredible value.'})
            elif b == 'PREMIUM':
                recs.append({'brand': 'Essilor', 'product': 'Eyezen Start Rx 1.60', 'price': 8000,
                    'why': 'Dual-focus optimization with Crizal Sapphire HR',
                    'pitch': 'Essilor Eyezen Start maintains your prescription over 99% of the vision cone versus 54% for standard lenses.'})
            else:
                recs.append({'brand': 'ZEISS', 'product': 'Digital SmartLife 1.60', 'price': 16100,
                    'why': 'SmartView 2.0 for connected lifestyle',
                    'pitch': 'ZEISS Digital SmartLife is engineered for frequent device switching with Luminance Design 2.0.'})

        elif ls == 'DRIVER':
            if b == 'VALUE':
                recs.append({'brand': 'GKB Prime', 'product': f'V-Max {rec_index}', 'price': 6839,
                    'why': 'High-index clarity for day and night driving',
                    'pitch': f'GKB V-Max {rec_index} gives you thin, lightweight lenses with excellent optical clarity for safe driving.'})
            elif b == 'PREMIUM':
                recs.append({'brand': 'Essilor', 'product': 'Omega SV + Essidrive 1.67', 'price': 11500,
                    'why': '90% less night glare with Essidrive coating',
                    'pitch': 'Essilor Essidrive reduces night reflections by up to 90%, making Silk Board junctions safer.'})
            else:
                recs.append({'brand': 'ZEISS', 'product': 'DriveSafe SV 1.60', 'price': 22400,
                    'why': 'Luminance Design for low-light + glare reduction',
                    'pitch': 'ZEISS DriveSafe is purpose-built for drivers. It optimizes your pupil response in low light.'})

        elif ls == 'OUTDOOR':
            if b == 'VALUE':
                recs.append({'brand': 'GKB Prime', 'product': 'Daynite Turbo Poly 1.59', 'price': 8145,
                    'why': 'Fast-adapting photochromic for Bangalore sun',
                    'pitch': 'GKB Daynite Turbo goes from clear to dark in seconds, handling Bangalore sun-to-cloud transitions.'})
            elif b == 'PREMIUM':
                recs.append({'brand': 'Essilor', 'product': 'Transitions Gen S 1.60', 'price': 16400,
                    'why': 'Ultra-fast Gen S with 8 colour options',
                    'pitch': 'Essilor Transitions Gen S darkens 60% faster and is available in Ruby, Sapphire, Emerald and more.'})
            else:
                recs.append({'brand': 'ZEISS', 'product': 'ClearMind + PhotoFusion X 1.60', 'price': 27400,
                    'why': 'NeurOptix clarity + fastest photochromic on market',
                    'pitch': 'ZEISS PhotoFusion X clears 2.5x faster than competitors and darkens in 15 seconds.'})

        else:  # OFFICE / STUDENT
            if b == 'VALUE':
                recs.append({'brand': 'GKB Prime', 'product': 'Vistaar 1.56', 'price': 662,
                    'why': 'Reliable everyday lens with HMC coating',
                    'pitch': 'GKB Vistaar is the best value lens in the market with clear optics for daily wear.'})
            elif b == 'PREMIUM':
                recs.append({'brand': 'Essilor', 'product': 'Crizal Rock 1.56', 'price': 3900,
                    'why': "India's #1 Superbrand coating for 10 years running",
                    'pitch': 'Essilor Crizal Rock gives you superior scratch resistance. 97% of wearers are satisfied.'})
            else:
                recs.append({'brand': 'ZEISS', 'product': 'SmartLife Young 1.50', 'price': 13700,
                    'why': 'SmartView 2.0 with Dynamic AgeFit technology',
                    'pitch': 'ZEISS SmartLife Young is designed for your connected lifestyle with up to 88% larger clear fields.'})

    return recs, rec_index, index_reason, max_power
# ===================================================================
# MAIN STREAMLIT UI
# ===================================================================

# Header
st.markdown('<p class="main-header">👁️ EYE VUE OPTICS</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Premium Home Eyewear Styling • Bangalore</p>', unsafe_allow_html=True)

st.markdown("---")

# Client Intake Form
with st.form("client_form"):
    st.markdown("### 📋 New Client Consultation")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Client Name", placeholder="e.g., Syed Wasim")
    with col2:
        age = st.number_input("Age", min_value=5, max_value=100, value=35)

    st.markdown("#### 👁️ RIGHT EYE (OD)")
    col1, col2, col3 = st.columns(3)
    with col1:
        sph_r = st.number_input("SPH", value=-2.0, step=0.25, format="%.2f")
    with col2:
        cyl_r = st.number_input("CYL", value=0.0, step=0.25, format="%.2f")
    with col3:
        axis_r = st.number_input("AXIS", min_value=0, max_value=180, value=0, step=1) if cyl_r != 0 else 0

    st.markdown("#### 👁️ LEFT EYE (OS)")
    col1, col2, col3 = st.columns(3)
    with col1:
        sph_l = st.number_input("SPH", value=-1.75, step=0.25, format="%.2f", key="sph_l")
    with col2:
        cyl_l = st.number_input("CYL", value=0.0, step=0.25, format="%.2f", key="cyl_l")
    with col3:
        axis_l = st.number_input("AXIS", min_value=0, max_value=180, value=0, step=1, key="axis_l") if cyl_l != 0 else 0

    st.markdown("#### 🔍 Additional Details")
    col1, col2 = st.columns(2)
    with col1:
        add = st.number_input("ADD Power (0 if none)", value=0.0, step=0.25, format="%.2f")
    with col2:
        pd = st.number_input("PD (mm)", value=62.0, step=0.5, format="%.1f")

    col1, col2, col3 = st.columns(3)
    with col1:
        lifestyle = st.selectbox("Lifestyle", ["IT / Heavy Screen", "Frequent Driver", "Outdoor / Active", "Office / Indoor", "Student"])
    with col2:
        budget = st.selectbox("Budget", ["Value (GKB Prime)", "Premium (Essilor/ZEISS)", "Ultra-Premium"])
    with col3:
        face = st.selectbox("Face Shape", ["Oval", "Round", "Square", "Heart/Diamond"])

    submitted = st.form_submit_button("🔍 GENERATE RECOMMENDATION", use_container_width=True)

# Process submission
if submitted:
    # Map inputs
    lifestyle_map = {
        "IT / Heavy Screen": "IT",
        "Frequent Driver": "DRIVER",
        "Outdoor / Active": "OUTDOOR",
        "Office / Indoor": "OFFICE",
        "Student": "STUDENT"
    }
    budget_map = {
        "Value (GKB Prime)": "VALUE",
        "Premium (Essilor/ZEISS)": "PREMIUM",
        "Ultra-Premium": "ULTRA"
    }
    face_map = {
        "Oval": "OVAL",
        "Round": "ROUND",
        "Square": "SQUARE",
        "Heart/Diamond": "HEART"
    }

    # Auto-detect vision type
    if age >= 40 and add > 0:
        vtype = 'PROGRESSIVE'
    elif age >= 35 and lifestyle_map[lifestyle] == 'IT':
        vtype = 'DIGITAL'
    else:
        vtype = 'SINGLE_VISION'

    client = {
        'name': name,
        'age': age,
        'sph_r': sph_r, 'cyl_r': cyl_r, 'axis_r': axis_r,
        'sph_l': sph_l, 'cyl_l': cyl_l, 'axis_l': axis_l,
        'add': add, 'pd': pd,
        'lifestyle': lifestyle_map[lifestyle],
        'budget': budget_map[budget],
        'face': face_map[face],
        'vtype': vtype
    }

    recs, rec_index, index_reason, max_power = generate_recommendations(client)
    fs = FRAME_STYLES[client['face']]

    # Display results
    st.markdown("---")
    st.markdown(f"### 💎 Recommended for {name}")

    # Prescription summary
    with st.expander("📋 View Full Prescription", expanded=False):
        st.markdown(f"""
        *Right Eye (OD):* {sph_r:+.2f} / {cyl_r:+.2f} × {axis_r}°
        *Left Eye (OS):* {sph_l:+.2f} / {cyl_l:+.2f} × {axis_l}°
        *ADD:* +{add:.2f}  |  *PD:* {pd:.1f}mm
        *Auto-Selected Index:* {rec_index} ({index_reason})
        *Max Power:* {max_power:.2f}D
        """)

    # Recommendations
    for i, rec in enumerate(recs, 1):
        st.markdown(f"""
        <div class="recommendation-card">
            <div style="font-size: 0.85rem; color: #666;">Option {i}</div>
            <div style="font-size: 1.1rem; font-weight: 600; color: #1a3a5c;">
                {rec['brand']} — {rec['product']}
            </div>
            <div class="price-tag">₹{rec['price']:,}/pair</div>
            <div style="margin-top: 8px; color: #444;">
                <strong>Why:</strong> {rec['why']}
            </div>
            <div class="pitch-box">
                🗣️ <strong>Stylist Pitch:</strong> "{rec['pitch']}"
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Frame recommendation
    st.markdown("### 🎨 Frame Style Recommendation")
    st.markdown(f"""
    <div class="recommendation-card">
        <div style="font-weight: 600; color: #1a3a5c;">Recommended Styles:</div>
        <div>{', '.join(fs['rec'])}</div>
        <div style="margin-top: 8px; color: #c62828;"><strong>Avoid:</strong> {', '.join(fs['avoid'])}</div>
        <div class="pitch-box">
            🗣️ "{fs['pitch']}"
        </div>
    </div>
    """, unsafe_allow_html=True)

    # WhatsApp share button
    whatsapp_text = f"""👁️ Eye Vue Optics - Personalized Recommendation

Dear {name},

Based on your consultation, here are your recommended lenses:

"""
    for i, rec in enumerate(recs, 1):
        whatsapp_text += f"""
Option {i}: {rec['brand']} - {rec['product']}
Price: ₹{rec['price']:,}/pair
{rec['why']}
"""

    whatsapp_text += f"""
Frame Style Recommendation:
{', '.join(fs['rec'])}

---
📞 Contact Eye Vue Optics for home consultation
"""

    import urllib.parse
    whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(whatsapp_text)}"

    st.markdown(f"""
    <div class="whatsapp-btn">
        <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
            <button style="width: 100%; padding: 14px; background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); color: white; border: none; border-radius: 8px; font-weight: 600; font-size: 1rem; cursor: pointer;">
                📱 Share Recommendation on WhatsApp
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Progressive frame audit (if applicable)
    if vtype == 'PROGRESSIVE':
        st.markdown("---")
        st.markdown("### 📐 Progressive Frame Audit")
        lens_height = st.number_input("Frame Lens Height (B) in mm", min_value=20, max_value=60, value=35)

        if lens_height:
            warnings, frame_recs = validate_for_progressive(lens_height, add)
            if warnings:
                for w in warnings:
                    st.warning(w)
            for r in frame_recs:
                st.success(r)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.85rem; padding: 20px 0;">
    <strong>Eye Vue Optics</strong> • Premium Home Eyewear Styling<br>
    Bangalore • Available for Home Consultations<br>
    <em>© 2026 Eye Vue Optics. All prices inclusive of GST.</em>
</div>
""", unsafe_allow_html=True)