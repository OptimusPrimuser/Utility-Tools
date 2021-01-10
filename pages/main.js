eel.expose(completed);
function addEffects()
{
    var i;
    var text='';
    for (i = 1; i < 9; i++) {
        if (document.getElementById(i.toString()).checked==true)
            text += '1';
        else
            text += '0';
    }
    text=text+'-'+document.getElementById('quality').value.toString()
    document.getElementById('applied').innerHTML=document.getElementById('applied').innerHTML+"\n"+text
}

function clearEffects()
{
    var i;
    for (i = 1; i < 9; i++) {
    document.getElementById(i.toString()).checked=false;
    } 
    var others=['noSpace','move','fSuffix']
    for (i = 0; i < 3; i++) {
        document.getElementById(others[i]).checked=false;
    }
}

function showImgB()
{
    document.getElementById('imgMenu').style.animationName='appear';
    document.getElementById('imgMenu').style.animationPlayState='running';
    console.log( document.getElementById('imgMenu').style);
}

function hideImgB()
{
    document.getElementById('imgMenu').style.animationName='disappear';
    document.getElementById('imgMenu').style.animationPlayState='running';
    console.log( document.getElementById('imgMenu').style);
}

function showRenamerB()
{
    document.getElementById('renamerMenu').style.animationName='appear';
    document.getElementById('renamerMenu').style.animationPlayState='running';
    console.log( document.getElementById('renamerMenu').style);
}

function hideRenamerB()
{
    document.getElementById('renamerMenu').style.animationName='disappear';
    document.getElementById('renamerMenu').style.animationPlayState='running';
    console.log( document.getElementById('renamerMenu').style);
}

function showDirectoryB()
{
    document.getElementById('directoryMenu').style.animationName='appear';
    document.getElementById('directoryMenu').style.animationPlayState='running';
    console.log( document.getElementById('directoryMenu').style);
}

function hideDirectoryB()
{
    document.getElementById('directoryMenu').style.animationName='disappear';
    document.getElementById('directoryMenu').style.animationPlayState='running';
    console.log( document.getElementById('directoryMenu').style);
}

function applyEffects()
{
    var inputFolder = document.getElementById("inputFolder").value
    var outputFolder = document.getElementById("outputFolder").value
    var applied = document.getElementById("applied").value.trim().split('\n')
    eel.applyEffects(inputFolder,outputFolder,applied)
}

function renaming()
{
    var folder = document.getElementById("folder").value
    var prefix = document.getElementById("prefix").value
    var suffix = document.getElementById("suffix").value
    var noSpace= document.getElementById("noSpace").checked
    eel.renaming(folder,noSpace,prefix,suffix)
}

function singler()
{
    var inputDirectory = document.getElementById("inputDirectory").value
    var outputDirectory = document.getElementById("outputDirectory").value
    var move = document.getElementById("move").checked
    var fSuffix= document.getElementById("fSuffix").checked
    eel.singler(inputDirectory,outputDirectory,move,fSuffix)
}

function completed()
{
    alert("Operation Completed 🤩🤩🤩🤩")
}