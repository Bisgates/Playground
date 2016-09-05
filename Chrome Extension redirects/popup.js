
var tablink = ""


chrome.tabs.getSelected(null,function(tab) {
    tablink = tab.url.replace(".android.com",".android.youdaxue.com").replace("www.","").replace("https","http");
});




function clickHandler(e) {

    chrome.tabs.update({url:tablink});
    window.close(); 
}

document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener("click",clickHandler);
});