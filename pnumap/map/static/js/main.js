const btn = document.getElementsByTagName('button');
let pre_btn =""
for(let i=0; i < btn.length; i++){
    btn[i].addEventListener('click', function(){
       
        // console.log("여기를 주목해보자", pre_num)
        let target_btn = this.getElementsByTagName('span')[1];

        if(target_btn.className=="blind"){
        
            target_btn.className = "blind_active"

            if (pre_btn !== "" && pre_btn !== this){
                pre_btn.getElementsByTagName('span')[1].className = "blind"
            }
        }       
        else{
            target_btn.className = "blind"
        }
     
        pre_btn = this
    })
  
}

