const f = document.getElementById('form');
const q = document.getElementById('query');
const url = 'https://deck-scraper.herokuapp.com/names/';
var tree = document.createDocumentFragment();
var averagecmc = 0;

async function submitted(event)
{
    const myNode = document.getElementById("main");

    while (myNode.firstChild) 
    {
    myNode.removeChild(myNode.lastChild);
    }
    
    event.preventDefault()
    const response = await fetch(url + q.value);

    const responsedata = await response.json();
    const cleaneddata = responsedata.values;
    console.log(cleaneddata);


    for(x in cleaneddata)
    {

        var div = document.createElement("div");
        div.setAttribute("id", cleaneddata[x].name);
        div.appendChild(document.createTextNode(cleaneddata[x].num + "x "));
        div.appendChild(document.createTextNode(cleaneddata[x].name));
        tree.append(div);
    }

    document.getElementById("main").appendChild(tree);

    const newdata = JSON.stringify(cleaneddata);
}
f.addEventListener('submit', submitted);
