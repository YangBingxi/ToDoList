// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
        var div = this.parentElement;
        // div.style.display = "none";
        window.alert("亲，完成了没就想删除？"+"右击试试吧。")
    }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');

document.getElementById("myUL").oncontextmenu = function(e){
    e.preventDefault();
};
document.getElementById("myUL").onmouseup = function(oEvent){
    var list_id = oEvent.target.id;
    var div = oEvent.target;
    if(!oEvent) oEvent = window.event;
    if(oEvent.button==2){
        console.log("right"+list_id);
        var deleteResult = window.confirm("确定要删除这条记录吗？");
        if (deleteResult==true){
            console.log("true");
            $.ajax({
                type: 'POST',
                url: '/changestatus/',
                data: {status: 0, list_id: list_id},
                dataType: 'json'
            }).done();
        div.style.display = "none";

        }else {
            console.log("False");
        }
    }
}
document.getElementById("myUL").addEventListener("click", function (e) {
    //console.log(e.target.id);
    var list_id = e.target.id;
    console.log(list_id);
    if (e.target.tagName === 'LI') {
        e.target.classList.toggle('checked');
        $.ajax({
            type: 'POST',
            url: '/changestatus/',
            data: {status: 5, list_id: list_id},
            dataType: 'json'
        }).done();
    }
}, false);


// Create a new list item when clicking on the "Add" button
function newElement() {
    var li = document.createElement("li");
    var inputValue = document.getElementById("myInput").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
        alert("You must write something!");
    } else {
        $.ajax({
            type: 'POST',
            url: '/addlist/',
            data: {content: inputValue},
            dataType: 'json'
        }).done();
        document.getElementById("myUL").appendChild(li);
    }
    document.getElementById("myInput").value = "";

    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function () {
            var div = this.parentElement;
            div.style.display = "none";
        }
    }
}
