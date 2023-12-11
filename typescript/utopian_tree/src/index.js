'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
exports.utopianTree = void 0;
const fs_1 = require("fs");
process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString = '';
let inputLines = [];
let currentLine = 0;
process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});
process.stdin.on('end', function () {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});
function readLine() {
    return inputLines[currentLine++];
}
/*
 * Complete the 'utopianTree' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */
function utopianTree(n) {
    let h = 1;
    for (let i = 1; i <= n; i++) {
        h = (i % 2 === 0) ? h + 1 : h * 2;
    }
    return h;
}
exports.utopianTree = utopianTree;
function main() {
    const ws = (0, fs_1.createWriteStream)(process.env['OUTPUT_PATH'] || "");
    const t = parseInt(readLine().trim(), 10);
    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine().trim(), 10);
        const result = utopianTree(n);
        ws.write(result + '\n');
    }
    ws.end();
}
