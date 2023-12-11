'use strict';

import { WriteStream, createWriteStream } from "fs";
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';

    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

/*
 * Complete the 'utopianTree' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */

export function utopianTree(n: number): number {
    let h = 1;
    for (let i = 1; i <= n; i++) {
        h = (i % 2 === 0) ? h + 1 : h * 2;
    }
    return h;
}

function main() {
    const ws: WriteStream = createWriteStream(process.env['OUTPUT_PATH'] || "");

    const t: number = parseInt(readLine().trim(), 10);

    for (let tItr: number = 0; tItr < t; tItr++) {
        const n: number = parseInt(readLine().trim(), 10);

        const result: number = utopianTree(n);

        ws.write(result + '\n');
    }

    ws.end();
}
