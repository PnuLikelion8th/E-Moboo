//처음 보여지는 맵 화면이 가운데로 가도록
const focus_here = document.getElementById('focus');
focus_here.focus({preventScroll:false});
        
//건물 별 효과
const btn = document.getElementsByTagName('button');
let pre_btn =""
for(let i=0; i < btn.length; i++){
    btn[i].addEventListener('click', function(){
       
        // console.log("여기를 주목해보자", pre_num)
        let target_btn = this.getElementsByTagName('span')[1];
        console.log(target_btn)
        if(target_btn.className=="blind"){
            building_id = target_btn.parentElement.querySelector('.num').innerHTML;
            console.log(building_id)
            target_btn.className = "blind_active"
            target_btn.innerHTML += "<a class='coursebtn' href='"+"/building/"+building_id+"'"+">강의 둘러보기</a>";
            
            console.log(target_btn)

            if (pre_btn !== "" && pre_btn !== this){
                pre_btn.getElementsByTagName('span')[1].className = "blind"
                pre_btn.getElementsByTagName('span')[1].querySelector('.coursebtn').remove()
            }
            if (pre_b !== "" && pre_b !== this) {
                pre_b.getElementsByTagName('span')[1].className = "blind"
            }
        }       
        else{
            target_btn.className = "blind"
            target_btn.querySelector('.coursebtn').remove()
        }
     
        pre_btn = this
    })
  
}

