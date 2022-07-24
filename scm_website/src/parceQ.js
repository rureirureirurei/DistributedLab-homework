const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const { URLSearchParams } = require('url');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/auth', (req, res) => {
    c = req.originalUrl
    flag = 0
    a=""
    k=0
    for (let i = 13; ;i++) {
        if (c[i] == '&')
            break;
        a += c[i]
        k=i
    }
    a+=" "
    kk=0
    for (let i = k+7; ;i++) {
        if (c[i] == '&')
            break;
        a += c[i]
        kk=i
    }
    a+=" "
    for (let i = kk+6; i<c.length;i++) {
        if (c[i] == '&')
            break;
        a += c[i]
    }

    fs.writeFileSync('userData.txt', a+"<br>", {flag:"a+"})   
    res.append('Access-Control-Allow-Origin', ['*']);
    res.sendStatus(200);
    //res.writeHead(200, { 'Content-Type': contentType, 'Access-Control-Allow-Origin': '*' });
});
var path = require('path');

app.get('/userInfo', (req, res) => {
    const data = fs.readFileSync('userData.txt', {encoding:'utf8', flag:'r'})
    var options = {
        root: path.join(__dirname, '..')
    };
    console.log(__dirname)
    res.sendFile("/userData.txt", options)
    res.append('Access-Control-Allow-Origin', ['*']);
    //res.sendStatus(200);
    //res.writeHead(200, { 'Content-Type': contentType, 'Access-Control-Allow-Origin': '*' });
});


app.listen(80, () => console.log(`Started server at http://localhost:80!`));