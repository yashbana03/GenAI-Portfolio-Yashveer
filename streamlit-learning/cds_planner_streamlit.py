import streamlit as st
from datetime import datetime
import requests
import json

# 🌟 STREAMLIT DASHBOARD CONFIGURATION SETUP
st.set_page_config(
    page_title="CDS Journey Planner - Hybrid Dashboard",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🧠 COMPLETE SCHEDULE DATA SCHEMA MATRIX
schedule_raw = [
    {"date": "25 MAY", "tasks": ["President + VP + Governor", "January smiling buddha Revision", "Tense", "Idioms & phrases", "Watch root words class"]},
    {"date": "26 MAY", "tasks": ["Parliament", "January smiling buddha Revision", "Tense", "S1-S6 practice"]},
    {"date": "27 MAY", "tasks": ["Parliament + Parliamentary committees", "Jan.smiling buddha Revision", "Tense based error practice", "S1-S6 practice", "Watch Jan CA class"]},
    {"date": "28 MAY", "tasks": ["PM + CM + President", "Previous year error practice", "Parts of speech practice", "PQRS practice", "Idioms & phrases"]},
    {"date": "29 MAY", "tasks": ["Cell", "Feb smiling buddha Revision", "Noun", "S1-S2 practice", "Watch BAD class 2"]},
    {"date": "30 MAY", "tasks": ["Tissue", "Feb smiling buddha Revision", "Noun practice", "New pattern parts of speech"]},
    {"date": "31 MAY", "tasks": ["Polity Revision", "Backlogs", "Watch Jan CA class"]},
    {"date": "1 JUNE", "tasks": ["Life processes", "February smiling buddha Revision", "Watch Feb CA class"]},
    {"date": "2 JUNE", "tasks": ["Life processes", "March smiling buddha Revision", "Homonyms Revision", "S1-S6 practice"]},
    {"date": "3 JUNE", "tasks": ["Revise all polity topics covered so far", "March smiling buddha Revision", "Watch 11 most Asked Homonyms"]},
    {"date": "4 JUNE", "tasks": ["State legislature + panchayat + municipalities", "April smiling buddha Revision", "Pronoun", "Practice new pattern POS", "Fill ups practice", "PQRS practice", "Watch march CA class"]},
    {"date": "5 JUNE", "tasks": ["Constitutional & non-constitutional bodies", "April smiling buddha Revision", "Verb", "Pronoun practice", "Homonyms Revision", "Watch vocab class", "S1-S2 practice"]},
    {"date": "6 JUNE", "tasks": ["Revise cell and tissue", "Solve any previous year english paper", "April smiling buddha Revision"]},
    {"date": "7 JUNE", "tasks": ["Revise all Biology Topic covered", "Cloze test practice"]},
    {"date": "8 JUNE", "tasks": ["Disease", "January smiling buddha Revision", "Verb"]},
    {"date": "9 JUNE", "tasks": ["Plants & Human hormones", "Jan smiling buddha Revision", "Idioms & phrases"]},
    {"date": "10 JUNE", "tasks": ["Reproduction", "Jan smiling buddha Revision", "Verb practice", "Fill ups", "Homonyms Revision"]},
    {"date": "11 JUNE", "tasks": ["Revise polity topics covered so far", "Feb smiling buddha Revision"]},
    {"date": "12 JUNE", "focused_day": True, "tasks": ["Fundamental Rights", "Feb smiling buddha Revision", "Subject verb Agreement", "Idioms & phrases Revision"]},
    {"date": "13 JUNE", "tasks": ["DRSP + FDs", "Feb smiling buddha Revision", "Solve any previous year english question paper"]},
    {"date": "14 JUNE", "tasks": ["Revise Biology topics covered so far"]},
    {"date": "15 JUNE", "tasks": ["Diversity in living organisms", "Feb smiling buddha Revision", "Discourse marker", "Cloze test practice", "Watch BAD series class 3", "Error practice"]},
    {"date": "16 JUNE", "tasks": ["Control & coordination + formed elements + blood", "March smiling buddha Revision", "Question tag", "PQRS practice", "Idioms & phrases Revision"]},
    {"date": "17 JUNE", "tasks": ["Heredity & evolution", "March smiling buddha Revision", "Question tag practice", "Discourse marker", "Watch May CA class"]},
    {"date": "18 JUNE", "tasks": ["Making of the constitution", "March smiling buddha Revision", "New pattern POS practice", "S1-S6 practice"]},
    {"date": "19 JUNE", "tasks": ["Emergency provisions + Amendments & the constitution", "April smiling buddha revision", "Homonyms Revision", "S1-S2 practice"]},
    {"date": "20 JUNE", "tasks": ["Subordinates courts + HC + SC", "April smiling buddha revision", "S1-S6 + PQRS practice", "Fill ups practice", "Homonyms revision"]},
    {"date": "21 JUNE", "tasks": ["Complete pending tasks"]},
    {"date": "22 JUNE", "tasks": ["Revise polity topics covered so far"]},
    {"date": "23 JUNE", "tasks": ["Preamble", "April smiling buddha revision", "Grammar based error practice", "Solve previous year POS questions", "Idioms & phrases revision"]},
    {"date": "24 JUNE", "tasks": ["Complete Biology Revision", "April smiling buddha revision", "Solve any previous year english question paper", "S1-S6 practice", "Solve previous year S1-S2 question", "Watch vocab class", "Idioms & phrases revision"]},
    {"date": "25 JUNE", "tasks": ["Universe, Geology & Geological time scale", "Jan smiling buddha revision", "preposition", "cloze test"]},
    {"date": "26 JUNE", "tasks": ["latitude, longitude & interior of the earth", "Jan smiling buddha revision", "preposition", "phrasal verbs", "PQRS practice"]},
    {"date": "27 JUNE", "tasks": ["Earthquake and Volcanoes", "Jan smiling buddha revision", "fixed preposition", "preposition based fill ups", "SI-S6 practice"]},
    {"date": "28 JUNE", "tasks": ["complete polity Revision"]},
    {"date": "29 JUNE", "tasks": ["Geomorphic processes + rocks", "feb smiling buddha revision", "conjunction", "Idioms & phrases Revision", "cloze test", "watch vocab class"]},
    {"date": "30 JUNE", "tasks": ["Acids, Base & salts", "feb smiling buddha revision", "conjunction practice", "phrasal verbs", "SI-S6 practice"]},
    {"date": "1 JULY", "tasks": ["Metals & non-metals", "feb smiling buddha revision", "New pattern POS practice", "Homonyms Revision", "S1-S6 practice"]},
    {"date": "2 JULY", "tasks": ["Carbon & its compounds", "march smiling buddha revision", "Discourse marker", "S1-S2 practice", "Homonyms Revision"]},
    {"date": "3 JULY", "tasks": ["oceanic basin + ocean current", "march smiling buddha revision", "Grammar based error practice", "Idioms & phrases"]},
    {"date": "4 JULY", "tasks": ["coral reefs & tides", "march smiling buddha revision", "voice", "Narration", "S1-S2 practice"]},
    {"date": "5 JULY", "tasks": ["Revise physical Geography covered so far", "solve any previous year english paper"]},
    {"date": "6 JULY", "tasks": ["chemical Reaction & equation", "April smiling buddha revision", "voice practice", "Homonyms revision", "S1-S6 practice", "S1-S2 practice", "Idioms & Phrase Revision"]},
    {"date": "7 JULY", "tasks": ["Atoms & molecules + revision chemistry topics covered so far", "April smiling buddha revision", "Tense Revision + practice", "fill ups", "PQRS"]},
    {"date": "8 JULY", "tasks": ["Structure of Atoms", "April smiling buddha revision", "Discourse marker", "Idioms phrases Revision", "Homonyms Revision"]},
    {"date": "9 JULY", "tasks": ["state of matter", "may smiling buddha revision", "Narration practice"]},
    {"date": "10 JULY", "tasks": ["earth, Atmosphere, heat Budget, layers of earth's", "may smiling buddha revision", "Articles + Determiner", "S1-S6 practice", "Idioms & Phrases Revision"]},
    {"date": "11 JULY", "tasks": ["winds pressure belt + cyclones + Anticyclone", "may smiling buddha revision", "Articles + Determiner practice new pattern pos", "cloze test"]},
    {"date": "12 JULY", "tasks": ["inversion & temp + forms of condensation + clouds + precipitation", "english full mock test"]},
    {"date": "13 JULY", "tasks": ["fronts & landforms", "may smiling buddha revision", "Grammar based error practice", "S1-S6 practice", "Homonyms Revision"]}
]

daily_essentials = [
    "BOOK READING", "30 MIN CURRENT AFFAIRS REVISION", "KHELGHAR QUIZ", "NEWSPAPER", "DRR", "DIARY WRITING"
]

# 🗓️ CALENDAR ENGINE
def check_if_sunday(date_str):
    months_map = {"MAY": 5, "JUNE": 6, "JULY": 7}
    try:
        parts = date_str.strip().upper().split(" ")
        day_num = int(parts[0])
        month_num = months_map[parts[1]]
        dt = datetime(2026, month_num, day_num)
        return dt.weekday() == 6
    except:
        return False

for day in schedule_raw:
    day["is_sunday"] = check_if_sunday(day["date"])

# 💾 HYBRID ENGINE STATE CONFIGURATION SYSTEM
if "app_mode" not in st.session_state:
    st.session_state["app_mode"] = "cloud"
if "apps_script_url" not in st.session_state:
    st.session_state["apps_script_url"] = "https://script.google.com/macros/s/AKfycbzbNtODeoJpXQmV6zQ-JHFZg7u5EceONB9P76UaZBFXk5MbrYo6eG-aLwWVQ3msJOCw/exec"
if "workspace_sticky_notes" not in st.session_state:
    st.session_state["workspace_sticky_notes"] = ""
if "current_block_index" not in st.session_state:
    st.session_state["current_block_index"] = 0
if "cloud_data_loaded" not in st.session_state:
    st.session_state["cloud_data_loaded"] = False
if "cloud_error_flag" not in st.session_state:
    st.session_state["cloud_error_flag"] = False

# ☁️ CLOUD SYNC UTILITIES WITH SAFETY TIMEOUTS
def push_to_cloud(key, value):
    if st.session_state["app_mode"] == "cloud" and st.session_state["apps_script_url"]:
        try:
            payload = {"action": "update", "key": key, "value": str(value).upper()}
            requests.post(st.session_state["apps_script_url"], data=json.dumps(payload), headers={"Content-Type": "application/json"}, timeout=2)
        except Exception:
            pass

def pull_from_cloud():
    if st.session_state["app_mode"] == "cloud" and st.session_state["apps_script_url"]:
        try:
            response = requests.get(st.session_state["apps_script_url"], timeout=4)
            if response.status_code == 200:
                cloud_json = response.json()
                for key, val in cloud_json.items():
                    # Pure session state ko map karenge jo live sheet se aa rha h
                    if val in ["TRUE", "True", "true", True]:
                        st.session_state[key] = True
                    elif val in ["FALSE", "false", "False", False]:
                        st.session_state[key] = False
                    else:
                        st.session_state[key] = val
                st.session_state["cloud_data_loaded"] = True
                st.session_state["cloud_error_flag"] = False
            else:
                st.session_state["cloud_error_flag"] = True
        except Exception:
            st.session_state["cloud_error_flag"] = True

# 🛠️ INITIALIZE KEYS DYNAMICALLY WITH EXACT SHEET SCHEMAS
items_per_block = 8
total_blocks = (len(schedule_raw) + items_per_block - 1) // items_per_block

for idx, day in enumerate(schedule_raw):
    # Format directly mapping to sheet: task_6_JUNE_0 (No spaces, joined with underscore)
    date_clean = day["date"].strip().replace(" ", "_")
    for t_idx, _ in enumerate(day["tasks"]):
        key = f"task_{date_clean}_{t_idx}"
        if key not in st.session_state:
            st.session_state[key] = False

for b_id in range(total_blocks):
    for e_idx in range(len(daily_essentials)):
        for t_slot in range(items_per_block):
            abs_day = (b_id * items_per_block) + t_slot + 1
            key = f"daily_g{b_id+1}_e{e_idx}_d{abs_day}"
            if key not in st.session_state:
                st.session_state[key] = False

# Trigger Cloud Data Pull
if st.session_state["app_mode"] == "cloud" and st.session_state["apps_script_url"] and not st.session_state["cloud_data_loaded"]:
    pull_from_cloud()

# Parsing current time parameters
months_list = ["JAN", "FEB", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUG", "SEPT", "OCT", "NOV", "DEC"]
now = datetime.now()
current_date_str = f"{now.day} {months_list[now.month - 1]}"

today_index = -1
for idx, day in enumerate(schedule_raw):
    if day["date"].strip().upper() == current_date_str.strip().upper():
        today_index = idx
        break

# 🏛️ INTERFACE MANAGEMENT & CONNECTIONS
status_col, mode_btn_col = st.columns([3, 1])
with status_col:
    if st.session_state["cloud_error_flag"]:
        st.markdown("<p style='font-weight:600; margin-top:5px;'><span style='height:10px; width:10px; background-color:#dc2626; border-radius:50%; display:inline-block; margin-right:8px;'></span>⚠️ Cloud Response Timeout. Local Save Active.</p>", unsafe_allow_html=True)
    elif st.session_state["app_mode"] == "offline" or not st.session_state["apps_script_url"]:
        st.markdown("<p style='font-weight:600; margin-top:5px;'><span style='height:10px; width:10px; background-color:#f59e0b; border-radius:50%; display:inline-block; margin-right:8px;'></span>📱 Offline Mode Active</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='font-weight:600; margin-top:5px;'><span style='height:10px; width:10px; background-color:#10b981; border-radius:50%; display:inline-block; margin-right:8px;'></span>☁️ Cloud Sync Online & Active</p>", unsafe_allow_html=True)

with mode_btn_col:
    with st.expander("⚙️ Switch Mode Panel", expanded=False):
        chosen_mode = st.radio("Choose Mode:", ["📱 Offline Mode", "☁️ Cloud Sync Mode"], index=1 if st.session_state["app_mode"] == "cloud" else 0)
        if chosen_mode == "📱 Offline Mode":
            st.session_state["app_mode"] = "offline"
        else:
            st.session_state["app_mode"] = "cloud"
            script_input = st.text_input("Paste Apps Script URL:", value=st.session_state["apps_script_url"])
            if script_input and script_input != st.session_state["apps_script_url"]:
                st.session_state["apps_script_url"] = script_input
                st.session_state["cloud_data_loaded"] = False
                st.rerun()

# 👈 SIDEBAR PANEL DESIGN
with st.sidebar:
    st.markdown(
        f"<div style='text-align:center; background:linear-gradient(135deg, #1e3a8a, #3b82f6); padding:12px; border-radius:12px; color:white; margin-bottom:15px;'>"
        f"<h2 style='margin:0; font-size:1.4rem;'>CDS Focus Hub</h2>"
        f"</div>", 
        unsafe_allow_html=True
    )
    
    block_options = [f"Block Group {i} (Day {(i-1)*8+1} to {min(i*8, len(schedule_raw))})" for i in range(1, total_blocks + 1)]
    selected_block_str = st.selectbox("🎯 Select Study Block:", block_options, index=st.session_state["current_block_index"])
    st.session_state["current_block_index"] = block_options.index(selected_block_str)
    
    st.write("---")
    st.markdown("#### 📝 Quick Sticky Notes")
    def sync_sticky_notes():
        push_to_cloud("workspace_sticky_notes", st.session_state["sticky_notes_input"])
        st.session_state["workspace_sticky_notes"] = st.session_state["sticky_notes_input"]

    st.text_area(
        label="Quick Notes",
        value=st.session_state["workspace_sticky_notes"],
        placeholder="Yahan notes likhein...",
        height=140,
        label_visibility="collapsed",
        key="sticky_notes_input",
        on_change=sync_sticky_notes
    )

# 🏰 MAIN DASHBOARD RENDERING PLATFORM
start_idx = st.session_state["current_block_index"] * items_per_block
end_idx = min(start_idx + items_per_block, len(schedule_raw))
current_block_days = schedule_raw[start_idx:end_idx]

st.markdown("<h2 style='color:#1e3a8a;'>🎯 CDS Journey Planner - Hybrid Dashboard</h2>", unsafe_allow_html=True)

# TODAY'S SEPARATE DEDICATED SECTION
st.markdown(f"### ⚡ TODAY'S FOCUS TASKS ({current_date_str})")
if today_index != -1:
    today_data = schedule_raw[today_index]
    st.info(f"Today is {current_date_str}. Complete these specific targets:")
    
    for t_idx, task in enumerate(today_data["tasks"]):
        date_clean = today_data["date"].strip().replace(" ", "_")
        core_key = f"task_{date_clean}_{t_idx}"
        
        # UI Sync Handle
        if f"focus_{core_key}" not in st.session_state:
            st.session_state[f"focus_{core_key}"] = st.session_state.get(core_key, False)
            
        def update_from_focus(k=core_key):
            st.session_state[k] = st.session_state[f"focus_{k}"]
            push_to_cloud(k, st.session_state[k])

        st.checkbox(label=task, key=f"focus_{core_key}", value=st.session_state.get(core_key, False), on_change=update_from_focus)
else:
    st.success("🎉 No separate scheduled targets for today. Focus on pending revision blocks!")

st.write("---")

# ☑ CONTINUOUS DAILY ESSENTIAL TRICKER SYSTEM
st.markdown("<p style='color:#b45309; font-weight:700; font-size:1.1rem;'>☑ DAILY WORK (CONTINUOUS TRACKING COLUMNS)</p>", unsafe_allow_html=True)
st.markdown("<div style='background-color:#fffbeb; border:1px solid #fef3c7; border-radius:10px; padding:15px;'>", unsafe_allow_html=True)

for e_idx, essential in enumerate(daily_essentials):
    lbl_col, fields_col = st.columns([1, 3])
    with lbl_col:
        st.markdown(f"<div style='font-weight:600; font-size:0.85rem; color:#1f2937; margin-top:4px;'>⚡ {essential}</div>", unsafe_allow_html=True)
    
    with fields_col:
        cells = st.columns(items_per_block)
        for t_slot in range(items_per_block):
            absolute_day_number = start_idx + t_slot + 1
            if absolute_day_number <= len(schedule_raw):
                day_data = schedule_raw[absolute_day_number - 1]
                is_sun = day_data["is_sunday"]
                is_restricted = (essential in ["KHELGHAR QUIZ", "DRR"])
                
                with cells[t_slot]:
                    if is_sun and is_restricted:
                        st.markdown(f"<div style='text-align:center; color:#9ca3af; font-size:0.7rem;'>—<br><b>D{absolute_day_number}</b></div>", unsafe_allow_html=True)
                    else:
                        state_key = f"daily_g{st.session_state['current_block_index']+1}_e{e_idx}_d{absolute_day_number}"
                        
                        def sync_daily(sk=state_key):
                            push_to_cloud(sk, st.session_state[sk])
                            
                        st.checkbox(f"D{absolute_day_number}", key=state_key, on_change=sync_daily)
st.markdown("</div>", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# GRID ROWS DISPLAY FOR MAIN COURSE PLANNER SCHEDULE
st.markdown("##### 📋 STUDY SCHEDULE TARGET DAYS")
grid_row_1 = st.columns(4)
grid_row_2 = st.columns(4)
dashboard_grid_slots = grid_row_1 + grid_row_2

backlog_elements_html = []
total_pending_backlogs = 0

for global_idx, day_data in enumerate(schedule_raw):
    is_past_day = global_idx < today_index if today_index != -1 else global_idx < len(schedule_raw)
    date_clean = day_data["date"].strip().replace(" ", "_")
    for t_idx, task in enumerate(day_data["tasks"]):
        key = f"task_{date_clean}_{t_idx}"
        if is_past_day and not st.session_state.get(key, False):
            total_pending_backlogs += 1
            backlog_elements_html.append(f"<div style='color:#dc2626; font-size:0.8rem; margin-bottom:2px;'>⚠️ <b>{day_data['date']}:</b> {task}</div>")

for slot_idx, day_data in enumerate(current_block_days):
    absolute_day_count = start_idx + slot_idx + 1
    
    with dashboard_grid_slots[slot_idx]:
        if day_data["is_sunday"]:
            st.markdown(f"<div style='border:1px solid #fee2e2; padding:10px; border-radius:8px; background-color:#fef2f2;'>", unsafe_allow_html=True)
            st.markdown(f"🔴 <span style='color:#dc2626;'><b>[D{absolute_day_count}] {day_data['date']}</b></span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='border:1px solid #e5e7eb; padding:10px; border-radius:8px; background-color:#f9fafb;'>", unsafe_allow_html=True)
            st.markdown(f"📘 <b>[D{absolute_day_count}] {day_data['date']}</b>", unsafe_allow_html=True)
            
        st.markdown("<hr style='margin:6px 0; border:0; border-top:1px dashed #d1d5db;'>", unsafe_allow_html=True)
        
        date_clean = day_data["date"].strip().replace(" ", "_")
        for t_idx, task in enumerate(day_data["tasks"]):
            core_key = f"task_{date_clean}_{t_idx}"
            
            def sync_task(ck=core_key):
                push_to_cloud(ck, st.session_state[ck])
                
            st.checkbox(task, key=core_key, on_change=sync_task)
        st.markdown("</div>", unsafe_allow_html=True)

# 👈 AUTOMATED SIDEBAR BACKLOG ALERT PANEL
with st.sidebar:
    st.write("---")
    st.markdown("#### ⚠️ Auto-Backlog Corner")
    if total_pending_backlogs > 0:
        st.warning(f"Total {total_pending_backlogs} pending tasks detected!")
        for item in backlog_elements_html[:10]:
            st.markdown(item, unsafe_allow_html=True)
    else:
        st.success("🎉 Zero backlogs remaining!")