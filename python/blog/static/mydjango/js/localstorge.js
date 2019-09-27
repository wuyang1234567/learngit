
 function storge(name){
    console.log("storge函数");
     obj={
        'na':username.value,
        'pwd':password.value
        };
     get=localStorage.getItem(name);
     if (name==="loginmsg"){
         arr=[];
     }else{
         if(get===null){
            arr=[];
         }
         else{
             arr=JSON.parse(get)
         }
     }

     arr.push(obj);  //对象push到数组中
     jsonarr=JSON.stringify(arr);//将数组转换为字符串
     localStorage.setItem(name,jsonarr);  //将字符串数组保存下来
     get=localStorage.getItem(name);
 }
