let caravans = document.querySelectorAll('form.caravan-price');

for (let i = 0; i < caravans.length; i++) {
    caravans[i].addEventListener('click', function (event) {
        let caravan_price = caravans[i].parentNode.querySelector('span.p-price');
        let base_price = parseInt(caravan_price.innerText);
        let price_input = caravans[i].querySelector("input[name='price']");

        if (event.target.tagName.toLowerCase() === 'input') {

            if (event.target.type === 'checkbox') {
                if (event.target.checked === true) {
                    event.target.value = 'on';
                    base_price += parseInt(event.target.dataset.price);
                } else {
                    event.target.value = 'off';
                    base_price -= parseInt(event.target.dataset.price);
                }
                caravan_price.innerText = base_price;
            }

            if (event.target.type === 'radio') {
                event.target.addEventListener('change', function () {
                    if (event.target.checked === true) {

                        if (event.target.value === 'with-chassis') {
                            if (caravans[i].querySelector("input[name='parking_brake']").checked === true) {
                                base_price += parseInt(event.target.dataset.price) + parseInt(caravans[i].querySelector("input[name='parking_brake']").dataset.price);
                            } else {
                                base_price += parseInt(event.target.dataset.price);
                            }
                            caravans[i].querySelector("input[name='parking_brake']").removeAttribute('disabled');
                        }

                        if (event.target.value === 'no-chassis') {
                            if (caravans[i].querySelector("input[name='parking_brake']").checked === true) {
                                base_price = base_price - parseInt(caravans[i].querySelector("input[name='parking_brake']").dataset.price) - parseInt(caravans[i].querySelector("input[value='with-chassis']").dataset.price);
                            } else {
                                base_price -= parseInt(caravans[i].querySelector("input[value='with-chassis']").dataset.price);
                            }
                            caravans[i].querySelector("input[name='parking_brake']").setAttribute('disabled', 'true');
                        }

                    }
                    caravan_price.innerText = base_price;
                    price_input.value = base_price;
                });
            }

        }
        price_input.value = base_price;

        if (event.target.tagName.toLowerCase() === 'button') {

            let colors = document.querySelectorAll('.color-block');

            for (let i = 0; i < colors.length; i++) {
                colors[i].addEventListener('click', function (event) {
                    if (event.target.tagName.toLowerCase() === 'input') {
                        if (event.target.type === 'radio') {
                            event.target.addEventListener('change', function () {
                                for (let j = 0; j < colors.length; j++) {
                                    colors[j].querySelector('.color-img').classList.remove('selected');
                                }

                                if (event.target.checked === true) {
                                    event.target.parentNode.querySelector('.color-img').classList.add('selected');
                                    //get data name from modal
                                    let color_name = event.target.getAttribute('data-name');
                                    //confirm button
                                    let confirm = document.querySelector('#chooseColor .modal-footer button');
                                    let id_modal = confirm.getAttribute('data-id');

                                    let inputColor = caravans[id_modal].querySelector("input[name='color']");
                                    let buttonColor = caravans[id_modal].querySelector('button');

                                    confirm.addEventListener('click', function () {
                                        console.log(inputColor);
                                        inputColor.value = event.target.value;
                                        buttonColor.innerText = 'Color: ' + color_name;
                                    });
                                }

                            });
                        }
                    }
                });
            }

        }

    });
}
