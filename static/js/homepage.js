document.addEventListener('DOMContentLoaded', function () {
    console.log("test1")
    let arrowLeft = document.querySelector(".arrow-left")
    let arrowRight = document.querySelector(".arrow-right")
    let allLeft = document.querySelectorAll(".left");
    let deleteTeam = document.getElementById("delete-team");

    let currenIndex = 0
    let currentLeft = allLeft[currenIndex]

    currentLeft.style.display = "block"

    resetStyle(allLeft, currenIndex)
    deleteTeam.setAttribute("data-team-id", allLeft[currenIndex].getAttribute("id"))


    arrowLeft.addEventListener("click", function () {
        currenIndex = printNext(allLeft, currenIndex, -1)
        deleteTeam.setAttribute("data-team-id", allLeft[currenIndex].getAttribute("id"))
    })
    arrowRight.addEventListener("click", function () {
        currenIndex = printNext(allLeft, currenIndex, 1)
        deleteTeam.setAttribute("data-team-id", allLeft[currenIndex].getAttribute("id"))
    })

    deleteTeam.addEventListener("click", function () {
        $.ajax({
            type: 'DELETE',
            url: `/delete_team/${deleteTeam.getAttribute("data-team-id")}`,
            success: function (data) {
                console.log(data)
                console.log("Success: ", data);
            },
            error: function (xhr, textStatus, errorThrown) {
                console.error("Error: ", textStatus, errorThrown);
                console.log("Response Text: ", xhr.responseText);
            }
        }).then(() => {
            location.reload();
        });
    })
})

//todo refacto
document.addEventListener('DOMContentLoaded', function () {
    console.log("test2")
    const openPopupBtnTeam = document.getElementById('openPopupBtnTeam');
    const popupTeam = document.getElementById('popupTeam');
    const closePopupBtnTeam = document.getElementById('closePopupBtnTeam');
    const popupFormTeam = document.getElementById('popupFormTeam');
    const deleteTeam = document.getElementById("delete-team");

    openPopupBtnTeam.addEventListener('click', function () {
        popupTeam.style.display = 'flex';
    });

    closePopupBtnTeam.addEventListener('click', function () {
        popupTeam.style.display = 'none';
    });


    popupFormTeam.addEventListener('submit', function (event) {
        event.preventDefault();
        const nameInput = document.getElementById('nameTeam').value;
        popupTeam.style.display = 'none';

        $.ajax({
            type: 'POST',
            url: popupFormTeam.action,
            data: {
                team_name: nameInput,
            },
            success: function (data) {
                console.log(data)
                console.log("Success: ", data);
            },
            error: function (xhr, textStatus, errorThrown) {
                console.error("Error: ", textStatus, errorThrown);
                console.log("Response Text: ", xhr.responseText);
            }
        }).then(() => {
            location.reload();
        });
    });
});


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

