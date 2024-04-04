import fs from 'node:fs';
import path from 'node:path';

function main() {
    console.log("\n\n-----------------------------------");
    console.log("\nJavaScript Single Threaded Script");
    console.log("\n-----------------------------------\n\n");

    const basePath = process.argv[2] || '../';
    const inputFile = process.argv[3] || 'data/biggerSample.txt';
    const inputFilePath = path.join(basePath, inputFile);
    const outputFilePath = path.join(basePath, 'data', 'outputCPP.txt');

    readWriteFile(inputFilePath, outputFilePath);
}

function readWriteFile(inputPath, outputPath) {
    // Start read timer
    const readStartTime = process.hrtime();

    const fileContent = [];
    const readStream = fs.createReadStream(inputPath, { encoding: 'utf8' });
    const writeStream = fs.createWriteStream(outputPath, { encoding: 'utf8' });

    readStream.on('data', (chunk) => {
        fileContent.push(chunk);
    });

    readStream.on('error', (err) => {
        console.error(`Error reading file: ${err}`);
    });

    readStream.on('end', () => {
        // End read timer and calculate reading time
        const readEndTime = process.hrtime(readStartTime);
        console.log(`Reading time: ${readEndTime[0]}s ${readEndTime[1] / 1000000}ms`);

        // Process the file content here
        console.log(`File size: ${fileContent.length} bytes`);

        // Start write timer
        const writeStartTime = process.hrtime();

        for (const chunk of fileContent) {
            writeStream.write(chunk);
        }

        writeStream.end();

        writeStream.on('finish', () => {
            // End write timer and calculate writing time
            const writeEndTime = process.hrtime(writeStartTime);
            console.log(`Writing time: ${writeEndTime[0]}s ${writeEndTime[1] / 1000000}ms`);
            console.log(`Output file: ${outputPath}`);
        });
    });
}

main();
