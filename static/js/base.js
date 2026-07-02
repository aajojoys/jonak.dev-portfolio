import { add_dataset_elem, get_client_all_elements, get_client_element, get_dataset_value_base, hide_elem, show_elem, show_hide_elem, toggle_show_hide_elem } from "./utility.js"

const SESSION_THEME_KEY = "theme";
const TAG_BODY = "body";
const CLS_THEMETOGGLE = ".themetoggle-icon";
const CSS_THEMETOGGLE_DARK = "dark";
const CSS_THEMETOGGLE_LIGHT = "light";
const CLS_NAVTOGGLE = ".nav-toggle";
const CLS_NAVCENTER = ".nav-center";
const CLS_NAVRIGHT = ".nav-right";
const CSS_SHOWMENU = "show-menu";
const CLS_SHOWOPTION = ".show-option";
const CLS_SHOWOPTION_TS = ".show-option-ts";
const CLS_TS_ITEMS = ".ts-items";
const CLS_SHOWOPTION_BTN = ".show-option-btn";
const CLS_GALLERY_SLIDER_PREV = ".gallery-slider-prev";
const CLS_GALLERY_SLIDER_NEXT = ".gallery-slider-next";
const CLS_GALLERY_SLIDE = ".gallery-slide";
const ID_FORM_RESUME = "resume-form";
const CLS_RESUME_LINK = ".resume-link";
const ID_TURNSTILE = "cf-turnstile";
const TURNSTILE_RESPONSE = "cf-turnstile-response";
const CLS_CONTAINER = ".container";
const CLS_MODALOVERLAY_CONTAINER = ".modal-overlay";
let resume_widget_id = null;

function set_session_theme(theme_val) {
    sessionStorage.setItem(SESSION_THEME_KEY, theme_val);
}

function set_theme_by_session() {
    const cached_theme = sessionStorage.getItem(SESSION_THEME_KEY);
    const body_elem = get_client_element(TAG_BODY);
    if (cached_theme) {
        show_elem(body_elem, cached_theme, (cached_theme == CSS_THEMETOGGLE_LIGHT) ? CSS_THEMETOGGLE_DARK : CSS_THEMETOGGLE_LIGHT);
    } else {
        // default to CSS_THEMETOGGLE_DARK
        show_elem(body_elem, CSS_THEMETOGGLE_DARK, CSS_THEMETOGGLE_LIGHT);
        set_session_theme(CSS_THEMETOGGLE_DARK);
    }
}

function onclick_theme() {
    const elem = get_client_element(CLS_THEMETOGGLE);
    const body_elem = get_client_element(TAG_BODY);
    // elem.addEventListener('click', toggle_show_hide_elem.bind(null, body_elem, CSS_THEMETOGGLE_DARK, CSS_THEMETOGGLE_LIGHT));
    if (elem) { elem.addEventListener('click', () => {
        toggle_show_hide_elem(body_elem, CSS_THEMETOGGLE_DARK, CSS_THEMETOGGLE_LIGHT);
        set_session_theme(body_elem.classList.contains(CSS_THEMETOGGLE_DARK) ? CSS_THEMETOGGLE_DARK : CSS_THEMETOGGLE_LIGHT);
    })}
}

function onclick_nav_menu_helper(toggle_elem) {
    const center_elem = get_client_element(CLS_NAVCENTER);
    const right_elem = get_client_element(CLS_NAVRIGHT);
    [toggle_elem, center_elem, right_elem].forEach(elem => toggle_show_hide_elem(elem, CSS_SHOWMENU, ""));
}

function onclick_nav_menu() {
    const toggle_elem = get_client_element(CLS_NAVTOGGLE);
    if (toggle_elem) { toggle_elem.addEventListener("click", () => onclick_nav_menu_helper(toggle_elem)); }
}

function show_loader(to_show) {
    const container_elem = get_client_element(CLS_CONTAINER);
    const modal_elem = get_client_element(CLS_MODALOVERLAY_CONTAINER);
    to_show ? show_hide_elem(modal_elem, container_elem) : show_hide_elem(container_elem, modal_elem);
}

async function turnstile_on_success(token) {
    const controller = new AbortController();
    const timeout_id = setTimeout(() => controller.abort(), 10000);
    try {
        const resume_form_elem = document.getElementById(ID_FORM_RESUME);
        const form_data = new FormData(resume_form_elem);
        form_data.set(TURNSTILE_RESPONSE, token);
        const res = await fetch(resume_form_elem.action, {
            method: "POST",
            body: form_data,
            signal: controller.signal,
        })
        if (!res.ok) {
            alert("Try again later!");
        }
        const data = await res.json();
        if (data) { window.location = data.download_url };
    } catch(err) {
        if (err.name === "AbortError") {
            alert("Try again later!");
        }  
    } finally {
        clearTimeout(timeout_id);
        show_loader(false);
        turnstile.reset(resume_widget_id);
    }
}

function init_turnstile() {
    const turnstile_elem = document.getElementById(ID_TURNSTILE);

    if (!turnstile_elem) { return; };

    resume_widget_id = turnstile.render(turnstile_elem, {
        sitekey: get_dataset_value_base(turnstile_elem, 'sitekey'),
        execution: "execute",
        appearance: "interaction-only",
        callback: turnstile_on_success,
        "error-callback": () => {
            show_loader(false);
            alert("Verification failed. Try again later!");
        },

        "expired-callback": () => {
            show_loader(false);
            alert("Token expired. Try again later!")
        },
        "timeout-callback": () => {
            show_loader(false);
            alert("Verification timed out. Try again later!")
        },
    });
}

function onclick_resume_link() {
    init_turnstile();
    let download_inprogress = false;
    const resume_link_elem = get_client_element(CLS_RESUME_LINK);
    const resume_form_elem = document.getElementById(ID_FORM_RESUME);
    if (!resume_form_elem || !resume_link_elem) { return; }

    resume_link_elem.addEventListener('click', async (e) => {
        if (download_inprogress) { return; }
        download_inprogress = true;
        show_loader(true);
        e.preventDefault();
        turnstile.execute(resume_widget_id);
        download_inprogress = false;
    });
}

function onlick_show_option_helper(showoption_elem) {
    for (const child of showoption_elem.children) {
        toggle_show_hide_elem(child);
    }
}

function onclick_show_option() {
    const showoption_elems = get_client_all_elements(CLS_SHOWOPTION);
    for (const elem of showoption_elems) {
        elem.addEventListener("click", () => onlick_show_option_helper(elem));
    }
}

function onclick_show_option_ts_helper(showoption_ts_elem) {
    const tsitems_elem = get_client_element(CLS_TS_ITEMS);
    const btn_elems = get_client_all_elements(CLS_SHOWOPTION_BTN, showoption_ts_elem);
    for (const elem of [tsitems_elem, ...btn_elems]) { toggle_show_hide_elem(elem); }
}

function onclick_show_option_ts() {
    const ts_elem = get_client_element(CLS_SHOWOPTION_TS);
    if (ts_elem) { ts_elem.addEventListener("click", () => onclick_show_option_ts_helper(ts_elem)); }
}

function onclick_gallery_slider_btn_helper(btn_elem) {
    const curr_counter_key = "ccounter";
    const total_counter_key = "total";
    const slider_elem = btn_elem.parentElement;
    const prev_elem = get_client_element(CLS_GALLERY_SLIDER_PREV, slider_elem);
    const next_elem = get_client_element(CLS_GALLERY_SLIDER_NEXT, slider_elem);
    const bcounter = parseInt(get_dataset_value_base(prev_elem, curr_counter_key));
    // before
    const last_counter = parseInt(get_dataset_value_base(prev_elem, total_counter_key)) - 1; // counter starts from index 0
    if (bcounter == 0) { show_elem(prev_elem); }
    if (bcounter == last_counter) { show_elem(next_elem); }
    let ccounter = bcounter;
    if (btn_elem == next_elem) {
        ccounter += 1;
    } else {
        ccounter -= 1;
    }
    // after
    if (ccounter == 0) { hide_elem(prev_elem); }
    if (ccounter == last_counter) { hide_elem(next_elem); }
    const slide_elems = get_client_all_elements(CLS_GALLERY_SLIDE, slider_elem);
    add_dataset_elem(prev_elem, curr_counter_key, ccounter);
    add_dataset_elem(next_elem, curr_counter_key, ccounter);
    show_elem(slide_elems[ccounter]);
    hide_elem(slide_elems[bcounter]);
}

function onclick_gallery_slider_btn() {
    const next_elems = get_client_all_elements(CLS_GALLERY_SLIDER_NEXT);
    const prev_elems = get_client_all_elements(CLS_GALLERY_SLIDER_PREV);
    for (const elem of [...next_elems, ...prev_elems]) {
        elem.addEventListener("click", () => onclick_gallery_slider_btn_helper(elem));
    }
}

export function base_events() {
    set_theme_by_session();
    onclick_theme();
    onclick_nav_menu();
    onclick_resume_link();
    onclick_show_option();
    onclick_show_option_ts();
    onclick_gallery_slider_btn();
}

