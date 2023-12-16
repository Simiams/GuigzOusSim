document.addEventListener('DOMContentLoaded', function () {
    let arrowLeft = document.querySelector(".arrow-left")
    let arrowRight = document.querySelector(".arrow-right")
    let allLeft = document.querySelectorAll(".left");

    let currenIndex = 0
    let currentLeft = allLeft[currenIndex]

    currentLeft.style.display = "block"

    resetStyle(allLeft, currenIndex)

    arrowLeft.addEventListener("click", function (event) {
        currenIndex = printNext(allLeft, currenIndex, -1)
    })
    arrowRight.addEventListener("click", function (event) {
        currenIndex = printNext(allLeft, currenIndex, 1)
    })
})

const resetStyle = (allLeft, currentIndex) => {
    allLeft.forEach((item, index) => {
        if (index !== currentIndex) {
            item.style.display = "none"
        }
    })
}

const printNext = (allLeft, currenIndex, sens) => {
    if (allLeft.length === currenIndex + sens) {
        currenIndex = 0
    } else if (currenIndex + sens < 0) {
        currenIndex = allLeft.length - 1
    } else {
        currenIndex += sens
    }
    let currentLeft = allLeft[currenIndex]
    currentLeft.style.display = "block"
    resetStyle(allLeft, currenIndex)
    return currenIndex
}