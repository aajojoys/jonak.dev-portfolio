const CSS_SHOW = "show";
const CSS_HIDE = "hide";

export function get_client_element(attr, container=document) {
    return container.querySelector(attr);
}

export function get_client_all_elements(attr, container=document) {
    return container.querySelectorAll(attr);
}

export function get_client_element_value(attr, container=document) {
    const elem = container.querySelector(attr);
    if (elem) { return elem.value; }
    return null;
}

export function get_dataset_value_base(elem, attr_str) {
    /*
     * Get dataset value by given target element and attr_str (exclude prefix 'data-')
     * e.g. data-name="xxx" get_dataset_value_base(elem, attr_str="name")="xxx"
     *
     * @param { HTML element } elem: target underlying HTML element
     * @param { attr_str } str: dataset attr_str (exclude prefix 'data-') (if attr_str == "dataset", returns dataset object)
     *
     * returns { * }: Object if attr_str == "dataset"; if value exists, underlying value; otherwise null
     *
     */
    if (!elem) { return null; }
    const dataset_obj = { ...elem.dataset };
    if (attr_str == "dataset") { return dataset_obj; }
    return (Object.keys(dataset_obj).length) ? (dataset_obj[attr_str]) : (null);
}

export function get_all_dataset_base(elem) {
    /*
     * Get all dataset key values in Object
     *
     * @param { HTML element } elem: underlying HTML element
     *
     * returns { Object }: Object containing dataset key values
     *
     */
    if (!elem) { return null; }
    return { ...elem.dataset };
}

export function get_dataset_value_parent(parent_elem, attr_str) {
    const base_elem = get_select_option(parent_elem);
    return get_dataset_value_base(base_elem, attr_str);
}

export function add_dataset_elem(elem, attr_str, value) {
    elem.setAttribute(`data-${attr_str}`, value);
}

export function hide_elem(elem, cls_show=CSS_SHOW, cls_hide=CSS_HIDE) {
    if (cls_hide) { elem.classList.add(cls_hide); }
    elem.classList.remove(cls_show);
}

export function show_elem(elem, cls_show=CSS_SHOW, cls_hide=CSS_HIDE) {
    if (cls_show) { elem.classList.add(cls_show); }
    if (cls_hide) { elem.classList.remove(cls_hide); }
}

export function show_hide_elem(show_this_elem, hide_this_elem, cls_show=CSS_SHOW, cls_hide=CSS_HIDE) {
    if (show_this_elem) { show_elem(show_this_elem, cls_show, cls_hide); }
    if (hide_this_elem) { hide_elem(hide_this_elem, cls_show, cls_hide); }
}

export function toggle_show_hide_elem(elem, cls_show=CSS_SHOW, cls_hide=CSS_HIDE) {
    let to_show = false;
    // if cls_hide is empty string (skip cls_hide)
    if (!cls_hide) {
        to_show = elem.classList.contains(cls_show) ? false : true;
    } else {
        to_show = elem.classList.contains(cls_hide) ? true : false;
    }
    if (to_show) {
        show_elem(elem, cls_show, cls_hide);
    } else {
        hide_elem(elem, cls_show, cls_hide);
    }
}
