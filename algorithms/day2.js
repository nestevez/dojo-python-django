function remove_blanks(anything){
  if (typeof anything != 'string'){
    if (typeof anything == 'object'){
      anything = anything.join("");
      return anything;
    } else {
      anything = anything.toString();
    }
  }
  var a = anything.split(" ");
  anything = a.join("");
  return anything;
}

var a = ['play', 'that', 'funky', 'music'];
console.log(remove_blanks(a));
