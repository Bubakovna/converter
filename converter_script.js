function plnToChfConverter(pln){
    var result = pln * 0.23;
    var message =  pln.toString() + " PLN are " + result.toString() + " CHF.";
    return message
}

console.log(plnToChfConverter(1));
console.log(plnToChfConverter(10));
console.log(plnToChfConverter(100));