window.onload = () => {

}

function sidetoggle(e) {
    let side_flag = document.querySelector('.small_menu_btn')

    if (side_flag.classList.contains('active')) {
        document.querySelector('.small_menu_btn_line_01_active').className = "small_menu_btn_line small_menu_btn_line_01"
        document.querySelector('.small_menu_btn_line_02_active').className = "small_menu_btn_line small_menu_btn_line_02"
        document.querySelector('.small_menu_btn_line_03_active').className = "small_menu_btn_line small_menu_btn_line_03"
        document.querySelector('.small_menu_section_active').className = "small_menu_section"
        side_flag.classList.remove('active')
    } else {
        document.querySelector('.small_menu_btn_line_01').className = "small_menu_btn_line small_menu_btn_line_01_active"
        document.querySelector('.small_menu_btn_line_02').className = "small_menu_btn_line small_menu_btn_line_02_active"
        document.querySelector('.small_menu_btn_line_03').className = "small_menu_btn_line small_menu_btn_line_03_active"
        document.querySelector('.small_menu_section').className = "small_menu_section small_menu_section_active"
        side_flag.classList.toggle('active')
    }
}