document.addEventListener("DOMContentLoaded", function() {
    var Description__in = document.querySelector("#Description__in");
    var User__info__group = document.querySelector(".User__info__group");
    var Izox__add = document.querySelector("#Izox__add");
    Izox__add.addEventListener("click", function() {
        var a = Description__in.value;
        console.log(a);
        if(a.length > 0) {
            var NEW__izox = document.createElement("div");
            NEW__izox.classList.add("izox__user__info");
            NEW__izox.classList.add("d-flex");
            NEW__izox.classList.add("flex-column");
            NEW__izox.innerHTML = `<p class="izox__userName">New User</p>
            <span class="izox__subtitle">${a}</span>
            <span class="izox__dataTime">05.11.2023 20:47</span>`
            User__info__group.appendChild(NEW__izox);
        } else {
            alert("Hech narsa kiritilmagan !!!");
        }
        Description__in.value = "";
    });
});