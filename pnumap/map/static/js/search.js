

const search_box = document.querySelector('#gnb_q')
const search_icon = document.querySelector('.search_icon')
search_box.addEventListener('search', search, false);
search_icon.addEventListener('click', search, false);

    function search() {

     
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

