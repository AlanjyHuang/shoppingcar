function loadMsg(db) {
    console.log(db)
    console.log('in js')
    let action = 'get'
    let mydat = new FormData()
    mydat.append('control', action)
    mydat.append('db', db)
    url = 'http://192.168.56.1/shoppingcar/controllers/control.py'
    fetch(url, {
        method: 'POST',
        body: mydat,
    })
        .then(function (res) {
            //console.log(res)
            //return res.text()
            return res.json()
        })
        .then(function (data) {
            //example of returning results as text
            /**/
            //  console.log(data[1])
            //  JSON.parse(json.stringfy(data))
            console.log(data)
            /*let div=document.getElementById('guestbook');
        		div.innerHTML=data;
        */

            //example of returning results as a json object
            //    dat = data.dat //the dot format
            //     list = data['list'] //the [] indexed format
            //  console.log(dat, list)
            console.log('then ok')
            let p = '<tr><th>商品名稱</th><th>價格</th><th>數量</th></tr>'
            for (item of data) {
                console.log('then ok')
                if (parseInt(item.Number) > 0) {
                    p += '<tr style="height:50px">'
                    p += '<td>'
                    p += item.Name
                    p += '</td>'
                    p += '<td>'
                    console.log(item.Price)
                    if (parseInt(item.Price) > 1000) {
                        console.log(item.Price)
                        p += "<p style = 'color:Tomato;'>"
                    } else p += '<p>'
                    p += item.Price
                    p += '</p>'
                    console.log(p)
                    p += '</td>'
                    p += '<td>'
                    p += item.Number
                    p += '</td>'
                    p += '</tr>'
                }
            }
            let div = document.getElementById('guestbook')
            div.innerHTML = p
        })
}
function loadMsg_manager(db) {
    console.log(db)
    console.log('in js')
    let action = 'get'
    let mydat = new FormData()
    mydat.append('control', action)
    mydat.append('db', db)
    url = 'http://192.168.56.1/shoppingcar/controllers/control.py'
    fetch(url, {
        method: 'POST',
        body: mydat,
    })
        .then(function (res) {
            //console.log(res)
            //return res.text()
            return res.json()
        })
        .then(function (data) {
            //example of returning results as text
            /**/
            //  console.log(data[1])
            //  JSON.parse(json.stringfy(data))
            console.log(data)
            /*let div=document.getElementById('guestbook');
        		div.innerHTML=data;
        */

            //example of returning results as a json object
            //    dat = data.dat //the dot format
            //     list = data['list'] //the [] indexed format
            //  console.log(dat, list)
            console.log('then ok')
            let p = '<tr><th>商品ID</th><th>商品名稱</th><th>價格</th><th>數量</th></tr>'
            for (item of data) {
                console.log(item.Name, item.Number)
                if (parseInt(item.Number) > 0) {
                    p += '<tr style="height:50px">'
                    p += '<td>'
                    p += item.ID
                    p += '</td>'
                    p += '<td>'
                    p += item.Name
                    p += '</td>'
                    p += '<td>'
                    p += item.Price
                    p += '</td>'
                    p += '<td>'
                    p += item.Number
                    p += '</td>'
                    p += '</tr>'
                }
            }
            let div = document.getElementById('guestbook')
            div.innerHTML = p
        })
}
function add_to_car(name, num) {
    console.log(name, num)
    let action = 'add'
    let mydat = new FormData()
    let buy_name = document.getElementById(name).value
    let buy_num = document.getElementById(num).value
    console.log(buy_name, buy_num)
    mydat.append('control', action)
    mydat.append('Name', buy_name)
    mydat.append('Num', buy_num)
    console.log(mydat)
    url = 'http://192.168.56.1/shoppingcar/controllers/control.py'
    fetch(url, {
        method: 'POST',
        body: mydat,
    }).then(function (res) {
        console.log(res.text())
        //return res.text()
        //return res.json()
    })
}
function add_to_storage(ID, name, price, num) {
    console.log(ID, name, price, num)
    let action = 'add_stor'
    let mydat = new FormData()
    let buy_ID = document.getElementById(ID).value
    let buy_name = document.getElementById(name).value
    let buy_price = document.getElementById(price).value
    let buy_num = document.getElementById(num).value
    mydat.append('control', action)
    mydat.append('Name', buy_name)
    mydat.append('Price', buy_price)
    mydat.append('Num', buy_num)
    mydat.append('ID', buy_ID)
    console.log(mydat)
    url = 'http://192.168.56.1/shoppingcar/controllers/control.py'
    fetch(url, {
        method: 'POST',
        body: mydat,
    }).then(function (res) {
        console.log(res.text())
        //return res.text()
        //return res.json()
    })
}
function edit_storage(ID, name, price, num) {
    console.log(ID, name, price, num)
    let action = 'edit'
    let mydat = new FormData()
    let buy_ID = document.getElementById(ID).value
    let buy_name = document.getElementById(name).value
    let buy_price = document.getElementById(price).value
    let buy_num = document.getElementById(num).value
    mydat.append('control', action)
    mydat.append('Name', buy_name)
    mydat.append('Price', buy_price)
    mydat.append('Num', buy_num)
    mydat.append('ID', buy_ID)
    mydat.append('DB', 'storage')
    console.log(mydat)
    url = 'http://192.168.56.1/shoppingcar/controllers/control.py'
    fetch(url, {
        method: 'POST',
        body: mydat,
    }).then(function (res) {
        console.log(res.text())
        //return res.text()
        //return res.json()
    })
}
function eddit_car(name, num) {
    let action = 'edit'
    let mydat = new FormData()
    // let buy_ID = document.getElementById(ID).value
    let buy_name = document.getElementById(name).value
    // let buy_price = document.getElementById(price).value
    let buy_num = document.getElementById(num).value
    mydat.append('control', action)
    mydat.append('Name', buy_name)
    //   mydat.append('Price', buy_price)
    mydat.append('Num', buy_num)
    mydat.append('DB', 'shopping')
    //  mydat.append('ID', buy_ID)
    console.log(mydat)
    url = 'http://192.168.56.1/shoppingcar/controllers/control.py'
    fetch(url, {
        method: 'POST',
        body: mydat,
    }).then(function (res) {
        console.log(res.text())
        //return res.text()
        //return res.json()
    })
}
function out() {
    let action = 'cashout'
    let mydat = new FormData()
    // console.log('cashouting')
    mydat.append('control', action)
    url = 'http://192.168.56.1/shoppingcar/controllers/control.py'
    fetch(url, {
        method: 'POST',
        body: mydat,
    })
        .then(function (res) {
            console.log('back')
            return res.text()
            //return res.json()
        })
        .then(function (data) {
            console.log(data)
            let p = '<h1>總共' + data + '元</h1>'
            let div = document.getElementById('total')
            div.innerHTML = p
        })
}
