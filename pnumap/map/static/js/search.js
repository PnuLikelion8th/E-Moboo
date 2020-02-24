
const search_type_place = document.querySelector('.search_place_label')
const search_type_course = document.querySelector('.search_course_label')

search_type_place.addEventListener('click',function(){
    document.querySelector('.building_form').classList.add('show')
    document.querySelector('.course_form').classList.remove('show')

})
search_type_course.addEventListener('click', function () {
    document.querySelector('.course_form').classList.add('show')
    document.querySelector('.building_form').classList.remove('show')

})






const search_building_text = document.querySelector('#gnb_q_building')
const search_building_icon = document.querySelector('#gnb_q_building_icon')
search_building_text.addEventListener('search', search_building, false);
search_building_icon.addEventListener('click', search_building, false);


let pre_b = ""

function search_building() {
    console.log(this.value == undefined)
    if (this.value == undefined) {

        temp_b = document.querySelector('.pack' + this.previousSibling.previousSibling.value)
        temp_b.focus()
        temp_b.getElementsByTagName('span')[1].className = "blind_active"
        temp_b.getElementsByTagName('span')[1].innerHTML += "<a class='coursebtn' href='" + "/building/" + this.previousSibling.previousSibling.value + "'" + ">강의 둘러보기</a>"
        if (pre_b !== "" && pre_b !== temp_b) {
            pre_b.getElementsByTagName('span')[1].className = "blind"
            pre_b.getElementsByTagName('span')[1].querySelector('.coursebtn').remove()

        }
        if (pre_btn !== "" && pre_btn !== this) {
            pre_btn.getElementsByTagName('span')[1].className = "blind"
            pre_btn.getElementsByTagName('span')[1].querySelector('.coursebtn').remove()

        }
        sidetoggle()

        pre_b = temp_b
    } else {

        temp_b = document.querySelector('.pack' + this.value)
        temp_b.focus()
        temp_b.getElementsByTagName('span')[1].className = "blind_active"
        temp_b.getElementsByTagName('span')[1].innerHTML += "<a class='coursebtn' href='" + "/building/" + this.value + "'" + ">강의 둘러보기</a>"

        if (pre_b !== "" && pre_b !== temp_b) {
            pre_b.getElementsByTagName('span')[1].className = "blind"
            pre_b.getElementsByTagName('span')[1].querySelector('.coursebtn').remove()

        }
        if (pre_btn !== "" && pre_btn !== temp_b) {
            pre_btn.getElementsByTagName('span')[1].className = "blind"
            pre_btn.getElementsByTagName('span')[1].querySelector('.coursebtn').remove()

        }
        sidetoggle()
        pre_b = temp_b
    }
}

const search_course_text = document.querySelector('#gnb_q_course')
const search_course_icon = document.querySelector('#gnb_q_course_icon')
search_course_text.addEventListener('search', search_course, false);
search_course_icon.addEventListener('click', search_course, false);



function search_course() {
      
        // console.log(this.value)
      
        fetch('/search/', {
            method: 'get',
            headers: {
            // 'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
            }
            }).then((res) => {
                if (res.status === 200 || res.status === 201) {
                    res.json().then((json) => {
                console.log("성공",json)
        },

        )
    } else {
        // console.error("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
    }
    }).catch(err => console.error(err));


};

