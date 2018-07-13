'use strict';
const entriesLink = document.getElementById('entries');
const profileLink = document.getElementById('profile');
const settingsLink = document.getElementById('settings');

const allLinks = [entriesLink, profileLink, settingsLink];

document.addEventListener('DOMContentLoaded', function(){
    allLinks.forEach((link) => link.addEventListener('click', function(){
        // Unselect any other clicked link
        unselectLinks();

        // Mark clicked link as selected
        this.classList.add('active-link'); 
    }));

    entriesLink.addEventListener('click', function(){
        loadEntries();
    });
});

function loadEntries() {
}

function unselectLinks() {
    // Unselect other links
    for (const link of allLinks) {
        link.classList.remove('active-link');
    }
}