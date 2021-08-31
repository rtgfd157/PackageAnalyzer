const regFetch = require('npm-registry-fetch');

var keyword = process.argv[2];
var version = process.argv[3];

// console.log( typeof keyword  +  keyword + '\n');
// console.log( typeof  version +  version + '\n');

var req = {}
req[keyword] = version ;

var d = {};
var ver = {};
ver['version'] = version;

d[keyword] = ver ;

var auditData = {
    "name": "npm_audit_test",
    "version": "1.0.0",
    "requires": {
    },
    "dependencies": {
    }
};

auditData['requires'] = req;
auditData['dependencies'] = d;

//console.log( ' auditData :  \n   '+ auditData['dependencies'] + ' \n \n'  );

let opts = {
    "color":true,
    "json":true,
    "unicode":true,
    method: 'POST',
    gzip: true,
    body: auditData
};

return regFetch('/-/npm/v1/security/audits', opts)
    .then(res => {
        return res.json();
    })
    .then(res => {
        console.log(' \n');
        console.log(JSON.stringify(res, "", 3));
  }).catch(err => console.error(err));