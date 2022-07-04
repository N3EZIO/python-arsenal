var string = 'decode caesar';

var shift = 5;

caesar = '';

for (let index = 0; index < string.length; index++) {
	if (string[index] == ' ') {
		caesar += ' ';
	} else {
		var asci = string[index].charCodeAt() + shift;
		if (asci > 122 || (asci > 90 && asci - shift < 90)) {
			asci = asci - 26;
			caesar += String.fromCharCode(asci);
		} else {
			caesar += String.fromCharCode(asci);
		}
	}
}

console.log(caesar);
