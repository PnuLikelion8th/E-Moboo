

const score_up = document.querySelector('.score_up')
const score_down = document.querySelector('.score_down')
score_up.addEventListener('click', score, false);
score_down.addEventListener('click', score, false);

function score(e) {
   
    fetch('/score/' + e.target.className, {
        method: 'get',
        headers: {
            'Accept': 'application/json'
        }
    }).then((res) => {
        if (res.status === 200 || res.status === 201) {
            res.json().then((json) => {
                console.log("성공", json)
            },

            )
        } else {
        }
    }).catch(err => console.error(err));

    //document.querySelector('.score_reason').innerHTML=
    //"<input type=text placeholder='이유는요??' required><button>Go!</button>"
}

    