function countB(param) {
    let count = 0;
    for (let i = 0; i < param.length; i++) {
        if (param[i] === "B") {
            count++;
        }
    }
    return count;
}

console.log(countB("BiggBossbbB"))

function countChar(param, param1) {
    let count = 0
    for (let i = 0; i < param.length; i++) {
        if (param[i] === param1) {
            count++;
        }
    }
    return count;
}

console.log(countChar("srikar", "r"))