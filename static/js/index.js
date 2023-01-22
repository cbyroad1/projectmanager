



function collapse(){
    var contents = document.querySelectorAll(".task_container");

    for (let i = 0; i < contents.length; i++){
        contents[i].classList.toggle("disabled");
    }

}
