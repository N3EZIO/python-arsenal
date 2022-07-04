var key = "IAK";

var message = "ANDY REID";

var duplicate = message.replace(" ", "");

console.log(duplicate);

if (duplicate.length / 2 != 0) {
	duplicate += "X";
}

console.log(duplicate);
var alphabet = [
	"A",
	"B",
	"C",
	"D",
	"E",
	"F",
	"G",
	"H",
	"I",
	"K",
	"L",
	"M",
	"N",
	"O",
	"P",
	"Q",
	"R",
	"S",
	"T",
	"U",
	"V",
	"W",
	"X",
	"Y",
	"Z",
];

var key_list = [
	[2, 4, 6, 8, 4],
	[1, 3, 5, 7, 3],
	[8, 6, 4, 2, 2],
	[7, 5, 3, 1, 4],
	[7, 5, 3, 1, 7],
];

console.log(key_list[3][4]);

for (let i = 0; i < 5; i++) {
	for (let j = 0; j < 5; j++) {
		key_list[i][j] = "0";
	}
}

function make_key() {

    console.log("js is pretty good");
    }

make_key();
