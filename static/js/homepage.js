document.addEventListener('DOMContentLoaded', function () {
    let arrowLeft = document.querySelector(".arrow-left")
    let arrowRight = document.querySelector(".arrow-right")
    arrowLeft.addEventListener("click", function (event) {
        console.log("left")
    })
    arrowRight.addEventListener("click", function (event) {
        console.log("right")
    })
})