const speaker_toggle_btn = document.querySelector('.tri')
const speaker_section = document.querySelector('.speaker_hidden_section')

speaker_toggle_btn.addEventListener('click',function(){
    console.log(speaker_toggle_btn)
    console.log(speaker_section)
    if(speaker_section.classList.contains("speaker_section_active")){
        speaker_section.classList.remove('speaker_section_active')
    }
    else{
        speaker_section.classList.toggle("speaker_section_active")

    }
    

})