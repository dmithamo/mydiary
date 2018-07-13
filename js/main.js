'use strict';

document.addEventListener('DOMContentLoaded', () => {
    addClickListeners();
});

// Select anchor tags and put them in array
const entriesTag = document.getElementById('a-entries');
const profileTag = document.getElementById('a-profile');
const settingsTag = document.getElementById('a-settings');

// Array of anchor tags
const anchorTags = [entriesTag, profileTag, settingsTag];


// Add click listener to all anchorTags, do common function
function addClickListeners() {
    for (const anchorTag of anchorTags) {

        anchorTag.addEventListener('click', () => {
            // unmark any other marked anchorTags
            unselectAllAnchorTags();

            // Mark clicked anchorTag
            anchorTag.classList.add('active-link');

            // Load appropriate contents depending on clicked anchorTag
            loadContents(anchorTag);
        });
    }
}


// Select divs linked to anchorTags above and put them in array
const entriesDiv = document.getElementById('entries');
const profileDiv = document.getElementById('profile');
const settingsDiv = document.getElementById('settings');

// Array of content divs
const contentDivs = [entriesDiv, profileDiv, settingsDiv];

// Select ols within the divs above above and put them in array
const entriesList = document.getElementById('entries-list');
const profileList = document.getElementById('profile-list');
const settingsList = document.getElementById('settings-list');

// Array of ols in content divs
const contentLists = [entriesList, profileList, settingsList];

function loadContents(tag) {
    // Remove everything from contents div
    removeAllContent();

    if (tag.id === 'a-entries') {
        loadEntries();
    } else if (tag.id === 'a-profile') {
        loadProfile();
    } else if (tag.id === 'a-settings') {
        loadSettings();
    }
    
}

function removeAllContent() {
    for (const contentDiv of contentDivs) {
        contentDiv.style.display = 'none';
    }

    for (const contentList of contentLists) {
        contentList.style.display = 'none';
    }
}

function loadEntries() {
    entriesDiv.style.display = 'block';
    entriesList.style.display = 'block';
}

function loadProfile() {
    // Display profileDiv and contents
    profileDiv.style.display = 'block';
    profileList.style.display = 'block';
    
}

function loadSettings() {
    settingsDiv.style.display = 'block';
    settingsList.style.display = 'block';
}

function unselectAllAnchorTags() {
    // Unmark other Tags
    for (const anchorTag of anchorTags) {
        anchorTag.classList.remove('active-link');
    }
}

// Select all buttons
const buttons = document.querySelectorAll('button');
// add click listeners to btns
addClickListenersToButtons();

function addClickListenersToButtons() {
    for (const btn of buttons) {
        btn.addEventListener('click', (event) => {
            const elem = event.target;
            const parentElem = event.target.parentElement;
            
            if (elem.innerHTML === 'Delete') {
                parentElem.remove();

            } else if(elem.innerHTML === 'Delete') {

            }
        });
    }
}