var is_select_nid = document.getElementById("is_nid");
is_select_nid.addEventListener('click', show_hide_input);


function show_hide_input(){
    var value_is_nid = is_select_nid.value;
    if (value_is_nid === 'no'){
        document.getElementById("nid").removeAttribute("required");
        document.getElementById("nid__input").style.display = 'none';
    }else {
        document.getElementById("nid__input").style.display = 'block';
        document.getElementById("nid").required = true;
    }
}
