//pg 38
//pushFront(arr, val) arr
function pushFront(arr, var){
    for(let i = arr.length-1; i>=0;i--){
        arr[i+1]=arr[i];
    }
    arr[0]=var;
    return arr;
}

//popFront(arr) val, if empty array, return empty array,  return value popped
function popFront(arr){
    if(arr.length>0){
        var temp=arr[0];
        for(let i=0; i<arr.length-1;i++){
            arr[i]=arr[i+1];
        }
        arr.length-=1
        return temp;
    }
    else{
        return arr;
    }
}
//insertAt(arr, idx, val) arr
function insertAt(arr,idx,val){
    if(idx>arr.length){
        console.log('invalid index');
        return arr;
    }
    for(let i=arr.length-1;i>=idx;i--){
        arr[i+1]=arr[i];
    }
    arr[idx]=val;
    return arr;
}
//removeAt(arr,idx) arr
function removeAt(arr, idx){
    var temp=arr[idx];
    for(let i = idx; i<arr.length-1;i++){
        arr[i]=arr[i+1];
    }
    arr.length-=1;
    return arr, temp;
}
//swapPair(arr) arr
function swapPairs(arr){
    if(arr.length%2!=0){
        var stop = arr.length-2;
    }
    else{
        var stop = arr.length-1
    }
    for (let i=0; i<=stop; i+=2){
        let temp = arr[i];
        arr[i]=arr[i+1];
        arr[i+1]=temp;
    }
    return arr;
}
//removeDuplicates(arr)
