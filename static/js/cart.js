let updateBtns = document.querySelectorAll('.update-cart')

updateBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        let productId = btn.dataset.product
        let action = btn.dataset.action
        console.log(productId, action)

        console.log('User', user)
        if (user === 'AnonymousUser') {
            console.log('user is not logged in')
        } else {
            updateUserOrder(productId, action)

        }

    })

})

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...')

    const url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })

    }).then((response) => {
        return response.json
    }).then((data) => {
        console.log('data', data)
        location.reload()
    })
}