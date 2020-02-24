

let search_box = document.querySelector('.search')

search_box.addEventListener('submit', search, false);




    function search() {
        let pk = this.getAttribute('name')

        let data = new FormData();
        data.append('pk', pk);

        fetch('/search/', {
            body: data,
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

