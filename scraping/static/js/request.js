const f = document.getElementById('form');
const q = document.getElementById('query');
const namesUrl = 'https://deck-scraper.herokuapp.com/names/';
const scrapeUrl = 'https://deck-scraper.herokuapp.com/scrape/';
var tree = document.createDocumentFragment();

async function submitted(event)
{
    const myNode = document.getElementById("main");

    while (myNode.firstChild)
    {
    myNode.removeChild(myNode.lastChild);
    }


    event.preventDefault();

    const response2 = await fetch(scrapeUrl + q.value);
    const responsedata2 = await response2.json();

    const cleaneddata2 = responsedata2.data;

    console.log(cleaneddata2);

    for(x in cleaneddata2)
    {
        try
        {
        console.log(cleaneddata2[x].image_uris.png);
        }

        catch(err)
        {
        for(y in cleaneddata2[x]){
        console.log(y.card_faces);
        }

        }

    }



    const response = await fetch(namesUrl + q.value);

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
