document.addEventListener('DOMContentLoaded', function () {
    console.log("test")
    const _popup = document.querySelector('#popup');
    const _closeBtn = document.querySelector('.popup-close');
    const _hp = document.querySelector('#hp');
    const _attack = document.querySelector('#attack');
    const _defense = document.querySelector('#defense');
    const _speed = document.querySelector('#speed');
    const _image = document.querySelector('#image');
    const _name = document.querySelector('#name');
    const _abilities = document.querySelector('#abilities');
    const _card = document.querySelector('#card');
    const _container_team = document.querySelector('#container_team');

    const container_team = popup.querySelector('#container_team');

    _closeBtn.addEventListener('click', function () {
        popup.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });

    document.querySelectorAll('.pokemon_img').forEach(function (trigger) {
        trigger.addEventListener('click', function () {
            let team_buttons = [];
            let already_in_team = true
            let pokemon = JSON.parse(trigger.getAttribute('data-full-pokemon'));
            let t = trigger.getAttribute('data-current-team')
            if (t === null) {
                t = trigger.getAttribute('data-full-team')
                t = t.replace(/'/g, '')
                already_in_team = false
            }
            console.log(t)
            let team = JSON.parse(t);
            console.log("ou")
            console.log(pokemon.id_in_bdd);
            console.log(team);

            _popup.style.display = 'block';
            _image.setAttribute('src', pokemon.sprite_front);
            _hp.textContent = pokemon.stats.find(stat => stat.name === 'hp').base_stat;
            _attack.textContent = pokemon.stats.find(stat => stat.name === 'attack').base_stat;
            _defense.textContent = pokemon.stats.find(stat => stat.name === 'defense').base_stat;
            _speed.textContent = pokemon.stats.find(stat => stat.name === 'speed').base_stat;
            _name.textContent = pokemon.name;
            _abilities.innerHTML = pokemon.abilities.map(ability => `<p>${ability.name}</p>`);
            _card.style.background = "radial-gradient(circle at 50% 0%, rgb(1, 144, 255) 36%, rgb(255, 255, 255) 36%)";

            if (already_in_team) {
                team_buttons.push(`<button type="button" class="team-button btn btn-danger" data-management-type="delete" data-team-id="${team.id}">Virer de l'équipe</button>`);
            } else {
                for (t in team) {
                    team_buttons.push(`<button type="button" class="team-button btn btn-primary" data-management-type="create" data-team-id="${team[t].id}">${team[t].name}</button>`);
                }
            }
            console.log("team_buttons")
            _container_team.innerHTML = team_buttons;

            console.log(pokemon.id_in_bdd)

            document.querySelectorAll('.team-button').forEach(function (button) {
                button.addEventListener('click', function (event) {
                    event.preventDefault();
                    let teamId = button.getAttribute('data-team-id');
                    let managementType = button.getAttribute('data-management-type');
                    let id = pokemon.id_in_bdd === null ? pokemon.id : pokemon.id_in_bdd;

                    $.ajax({
                        type: 'POST',
                        url: container_team.action,
                        data: {
                            pokemon_id: id,
                            team_id: teamId,
                            management_type: managementType
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
                        if (already_in_team) {
                            location.reload();
                        }
                    });
                });
            });
        });
    });
});