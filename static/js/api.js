document.addEventListener('DOMContentLoaded', function () {
    var popup = document.querySelector('#popup');
    var closeBtn = document.querySelector('.popup-close');
    var popupText = popup.querySelector('#popup-text');
    var container_team = popup.querySelector('#container_team');

    closeBtn.addEventListener('click', function () {
        popup.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });

    document.querySelectorAll('.pokemon_img').forEach(function (trigger) {
        trigger.addEventListener('click', function () {
            var url_img = trigger.getAttribute('src');
            var pokemon_name = trigger.getAttribute('data-pokemon-name');
            var pokemon_id = trigger.getAttribute('data-pokemon-id');
            var teams_id = trigger.getAttribute('data-team-ids');

            popup.style.display = 'block';
            popupText.textContent = pokemon_name;
            popup.querySelector('.popup-img').setAttribute('src', url_img);

            var button_teams = JSON.parse(teams_id).map(function (team_id) {
                return `
                    <button type="button" name="team_id" class="team-button" data-team-id="${team_id}">Add to Team ${team_id}</button>
                `;
            });
            container_team.innerHTML = button_teams;

            document.querySelectorAll('.team-button').forEach(function (button) {
                button.addEventListener('click', function (event) {
                    event.preventDefault();
                    var teamId = button.getAttribute('data-team-id');

                    container_team.setAttribute('data-custom', 'your_custom_value');

                    console.log("Submitting data: ", {
                        pokemon_id: trigger.getAttribute('data-pokemon-id'),
                        team_id: teamId,
                        pokemon_name: pokemon_name
                    });

                    $.ajax({
                        type: 'POST',
                        url: container_team.action,
                        data: {
                            pokemon_id: trigger.getAttribute('data-pokemon-id'),
                            team_id: teamId
                        },
                        success: function (data) {
                            console.log(data)
                            console.log("Success: ", data);
                        },
                        error: function (xhr, textStatus, errorThrown) {
                            console.error("Error: ", textStatus, errorThrown);
                            console.log("Response Text: ", xhr.responseText);
                        }
                    });
                });
            });
        });
    });
});


// // document.addEventListener('DOMContentLoaded', function () {
// //     var popup = document.querySelector('#popup');
// //     var closeBtn = document.querySelector('.popup-close');
// //     var popupText = popup.querySelector('#popup-text');
// //     var container_team = popup.querySelector('#container_team');
// //
// //     closeBtn.addEventListener('click', function () {
// //         popup.style.display = 'none';
// //     });
// //
// //     window.addEventListener('click', function (event) {
// //         if (event.target === popup) {
// //             popup.style.display = 'none';
// //         }
// //     });
// //
// //     document.querySelectorAll('.pokemon_img').forEach(function (trigger) {
// //         trigger.addEventListener('click', function () {
// //             var url_img = trigger.getAttribute('src');
// //             var pokemon_name = trigger.getAttribute('data-pokemon-name');
// //             var teams_id = trigger.getAttribute('data-team-ids');
// //
// //             popup.style.display = 'block';
// //             popupText.textContent = pokemon_name;
// //             popup.querySelector('.popup-img').setAttribute('src', url_img);
// //
// //             var button_teams = JSON.parse(teams_id).map(function (team_id) {
// //                 return `
// //                     <button type="submit" name="team_id" class="team-button" data-team-id="${team_id}">Add to Team ${team_id}</button>
// //                 `;
// //             });
// //             container_team.innerHTML = button_teams;
// //
// //             document.querySelectorAll('.team-button').forEach(function (button) {
// //                 button.addEventListener('click', function () {
// //                     var teamId = button.getAttribute('data-team-id');
// //                     console.log("Submitting data: ", {
// //                         pokemon_id: trigger.getAttribute('data-pokemon-id'),
// //                         team_id: teamId
// //                     });
// //
// //                     $.ajax({
// //                         type: 'POST',
// //                         url: container_team.action,
// //                         data: $(container_team).serialize(),
// //                         success: function (data) {
// //                             console.log("Success: ", data);
// //                         },
// //                         error: function (xhr, textStatus, errorThrown) {
// //                             console.error("Error: ", textStatus, errorThrown);
// //                             console.log("Response Text: ", xhr.responseText);
// //                         }
// //                     });
// //                 });
// //             });
// //         });
// //     });
// // });
//
//
// document.addEventListener('DOMContentLoaded', function () {
//     var pokemon_img = document.querySelectorAll('.pokemon_img');
//     var popup = document.querySelector('#popup');
//     var closeBtn = document.querySelector('.popup-close');
//     var popupText = popup.querySelector('#popup-text');
//     var container_team = popup.querySelector('#container_team');
//
//     pokemon_img.forEach(function (trigger) {
//         trigger.addEventListener('click', function () {
//             url_img = trigger.getAttribute('src');
//             pokemon_name = trigger.getAttribute('data-pokemon-name');
//             teams_id = trigger.getAttribute('data-team-ids');
//
//             popup.style.display = 'block';
//             popupText.textContent = pokemon_name;
//             popup.querySelector('.popup-img').setAttribute('src', url_img);
//
//             container_team.innerHTML =  `
//                     <input type="hidden" id="pokemon_id" name="pokemon_id" value="123">
//              `
//
//             button_teams = JSON.parse(teams_id).map(function (team_id) {
//                 return `
//                         <button type="submit" name="team_id" class="team-button" data-team-id="${team_id}">Add to Team ${team_id}</button>
//                        `;
//             });
//             container_team.innerHTML += button_teams;
//
//
//             // pokemonIdInput = document.getElementById('pokemon_id');
//             // document.querySelectorAll('.team-button').forEach(function (button) {
//             //     button.addEventListener('click', function () {
//             //         var teamId = button.getAttribute('data-team-id');
//             //         console.log("Submitting data: ", {pokemon_id: pokemonIdInput.value, team_id: teamId});
//             //     });
//             // });
//         });
//     });
//
//     closeBtn.addEventListener('click', function () {
//         popup.style.display = 'none';
//     });
//
//     window.addEventListener('click', function (event) {
//         if (event.target === popup) {
//             popup.style.display = 'none';
//         }
//     });
//
//     $(document).ready(function () {
//         $('#container_team').submit(function (event) {
//             event.preventDefault();
//             console.log(this)
//             console.log($(this).attr('action'))
//             console.log($(this).serialize())
//             $.ajax({
//                 type: 'POST',
//                 url: $(this).attr('action'),
//                 data: $(this).serialize(),
//                 success: function (data) {
//                     console.log(data);
//                 },
//                 error: function (error) {
//                     console.error(error);
//                 }
//             });
//         });
//     });
// });
//
//
// // document.addEventListener('DOMContentLoaded', function () {
// //     var pokemon_img = document.querySelectorAll('.pokemon_img');
// //     var popup = document.querySelector('#popup');
// //     var closeBtn = document.querySelector('.popup-close');
// //     var popupText = popup.querySelector('#popup-text');
// //     var container_team = popup.querySelector('#container_team');
// //
// //     pokemon_img.forEach(function (trigger) {
// //         trigger.addEventListener('click', function () {
// //             url_img = trigger.getAttribute('src');
// //             pokemon_name = trigger.getAttribute('data-pokemon-name');
// //             pokemon_id = trigger.getAttribute('data-pokemon-id');
// //             teams_id = trigger.getAttribute('data-team-ids');
// //
// //             popup.style.display = 'block';
// //             popupText.textContent = pokemon_name;
// //             popup.querySelector('.popup-img').setAttribute('src', url_img);
// //             button_teams = JSON.parse(teams_id).map(function (team_id) {
// //                 return `<button type="button" class="team-button" data-team-id="${team_id}">Add to Team ${team_id}</button>`;
// //             });
// //             container_team.innerHTML = button_teams;
// //
// //             // Add event listener to each team button
// //             var teamButtons = document.querySelectorAll('.team-button');
// //             teamButtons.forEach(function (button) {
// //                 button.addEventListener('click', function () {
// //                     var teamId = button.getAttribute('data-team-id');
// //
// //                     // Create a form dynamically
// //                     var form = document.createElement('form');
// //                     form.setAttribute('method', 'post');
// //                     form.setAttribute('action', '{% url "add_pokemon_to_team" %}');
// //
// //                     // Add CSRF token
// //                     var csrfInput = document.createElement('input');
// //                     csrfInput.setAttribute('type', 'hidden');
// //                     csrfInput.setAttribute('name', 'csrfmiddlewaretoken');
// //                     csrfInput.setAttribute('value', '{{ csrf_token }}');
// //                     form.appendChild(csrfInput);
// //
// //                     // Add Pokemon ID input
// //                     var pokemonIdInput = document.createElement('input');
// //                     pokemonIdInput.setAttribute('type', 'hidden');
// //                     pokemonIdInput.setAttribute('name', 'pokemon_id');
// //                     pokemonIdInput.setAttribute('value', pokemon_id);
// //                     form.appendChild(pokemonIdInput);
// //
// //                     // Add Team ID input
// //                     var teamIdInput = document.createElement('input');
// //                     teamIdInput.setAttribute('type', 'hidden');
// //                     teamIdInput.setAttribute('name', 'team_id');
// //                     teamIdInput.setAttribute('value', teamId);
// //                     form.appendChild(teamIdInput);
// //
// //                     // Append the form to the body and submit it
// //                     document.body.appendChild(form);
// //                     form.submit();
// //                 });
// //             });
// //         });
// //     });
// //
// //     closeBtn.addEventListener('click', function () {
// //         popup.style.display = 'none';
// //     });
// //
// //     window.addEventListener('click', function (event) {
// //         if (event.target === popup) {
// //             popup.style.display = 'none';
// //         }
// //     });
// // });
