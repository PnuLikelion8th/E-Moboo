//처음 보여지는 맵 화면이 가운데로 가도록
const focus_here = document.getElementById('focus');
focus_here.focus({preventScroll:false});
        
//건물 별 효과
const btn = document.getElementsByTagName('button');

for(let i=0; i < btn.length; i++){
    btn[i].addEventListener('click', function(){
        let target_btn = this.getElementsByTagName('span')[1];
        console.log(target_btn);
        if(target_btn.className=="blind"){
        target_btn.className = "blind_active"
    
        }
        else{
            target_btn.className = "blind"
        }
    })
}

