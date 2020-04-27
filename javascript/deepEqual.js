function deepEqual(param, param1) {
    if (typeof param === "object" && typeof param1 === "object" && param !== null && param1 !== null) {
        const keys = Object.keys(param);
        const keys1 = Object.keys(param1);
        if (keys.length === keys1.length) {
            let count = 0;
            for (let i = 0; i < keys.length; i++) {
                if (typeof param[keys[i]] === "object" && typeof param1[keys1[i]] === "object") {
                    return deepEqual(param[keys[i]], param1[keys1[i]])
                }
                else if (param[keys[i]] === param1[keys1[i]]) {
                    count++;
                } else {
                    return false;
                }
            }
            if (count === keys.length) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else if (param === param1) {
        return true;
    } else {
        return false;
    }
}
