// let fs = require('fs'); 
// let parse = require('csv-parse');

// var csvData=[];
// fs.createReadStream('annual-enterprise-survey.csv')
//     .pipe(parse({delimiter: ':'}))
//     .on('data', function(csvrow) {
//         console.log(csvrow);
//         csvData.push(csvrow);        
//     })
//     .on('end',function() {
//       //do something with csvData
//       console.log(csvData);
//     });

var fs = require('fs');
var parse = require('csv-parse');

var inputFile='myfile.csv';

var parser = parse({delimiter: ','}, function (err, data) {
    console.log(data)
});
fs.createReadStream(inputFile).pipe(parser);