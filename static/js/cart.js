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

    const url = '/update_items/'

    fetch(url, {
        method = 'POST',
        headers = {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
}