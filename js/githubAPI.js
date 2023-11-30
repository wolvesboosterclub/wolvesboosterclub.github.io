const githubAPI = "https://api.github.com/repos/wolvesboosterclub/wolvesboosterclub.github.io/contents/";

function getGitHubListing(filematch, directory = "") {
        
    if (document.cookie.includes("wbc_githubAPI_" + directory + "=")) {
        return new Promise((resolve, reject) => {
            const cookies = decodeURIComponent(document.cookie).split(';');
            for(var cookie of cookies) {
                if (cookie.includes("wbc_githubAPI_" + directory + "=")) {
                    const entries = JSON.parse(atob(cookie.split('=', 2)[1]));
                    var files = [];
    
                    for(var entry of entries) {
                        if (!entry.name.match(filematch))
                            continue;
    
                        files.push(entry);
                    }
                    resolve(files);
                }
            }
            reject("Cookie seemed to contain previous information for directory " + 
                directory + " but was unable to parse the entries");
        });
    }
    
    return fetch(githubAPI + directory, {
        method: "GET"
    }).then((resp) => {
        if (resp.ok) {
            return resp.json();
        }
        throw new Error("Unable to find directory listings at " + githubAPI + directory);
    }).then((contents) => {

        var listings = [];
        var files = [];
        for(let i = 0, len = contents.length; i < len; i++) {
            var entry = contents[i];

            listings.push({
                name: entry.name,
                download_url: entry.download_url
            })

            if (!entry.name.match(filematch)) 
                continue;
                
            files.push(entry);
        }

        const d = new Date();
        d.setTime(d.getTime() + (10*60*1000));
        document.cookie = "wbc_githubAPI_" + directory + "=" + btoa(JSON.stringify(listings)) + ";expires=" + d.toUTCString() + ";path=/;";

        return files;
    });
}