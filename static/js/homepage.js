document.addEventListener('DOMContentLoaded', function () {
    const allLeft = document.querySelectorAll(".left");
    const deleteTeam = document.getElementById("delete-team");
    let currenIndex = 0
    const currentLeft = allLeft[currenIndex]
    currentLeft.style.display = "block"

    manage_arrow(allLeft, currenIndex, deleteTeam)
    resetStyle(allLeft, currenIndex)
    manage_delete_team(allLeft, currenIndex, deleteTeam)
    manage_add_team()
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
    const currentLeft = allLeft[currenIndex]
    currentLeft.style.display = "block"
    resetStyle(allLeft, currenIndex)
    return currenIndex
}

const request_api = (url, method, data) => {
    $.ajax({
        type: method,
        url: url,
        data: data,
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
}

const manage_arrow = (allLeft, currenIndex, deleteTeam) => {
    const arrowLeft = document.querySelector(".arrow-left")
    const arrowRight = document.querySelector(".arrow-right")
    const overlay = document.querySelector('.overlay');

    arrowLeft.addEventListener("click", function () {
        overlay.style.display = 'block';
        setTimeout(function () {
            overlay.style.display = 'none';
        }, 1000);
        setTimeout(function () {
            currenIndex = printNext(allLeft, currenIndex, -1)
            deleteTeam.setAttribute("data-team-id", allLeft[currenIndex].getAttribute("id"))
        }, 500);
    })

    arrowRight.addEventListener("click", function () {
        overlay.style.display = 'block';
        setTimeout(function () {
            overlay.style.display = 'none';
        }, 1000);
        setTimeout(function () {
            currenIndex = printNext(allLeft, currenIndex, 1)
            deleteTeam.setAttribute("data-team-id", allLeft[currenIndex].getAttribute("id"))
        }, 500);
    })
}


manage_delete_team = (allLeft, currenIndex, deleteTeam) => {
    deleteTeam.setAttribute("data-team-id", allLeft[currenIndex].getAttribute("id"))

    deleteTeam.addEventListener("click", function () {
        request_api(`/delete_team/${deleteTeam.getAttribute("data-team-id")}`, 'DELETE', {})
    })
}

manage_add_team = () => {
    const openPopupBtnTeam = document.getElementById('openPopupBtnTeam');
    const popupTeam = document.getElementById('popupTeam');
    const closePopupBtnTeam = document.getElementById('closePopupBtnTeam');
    const popupFormTeam = document.getElementById('popupFormTeam');

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
        request_api(popupFormTeam.action, 'POST', {team_name: nameInput});
    });
}