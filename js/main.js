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

// Select divs linked to anchorTags above and put them in array
const entriesDiv = document.getElementById('entries');
const profileDiv = document.getElementById('profile');
const settingsDiv = document.getElementById('settings');

// Array of content divs
const contentDivs = [entriesDiv, profileDiv, settingsDiv];

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
}

function loadEntries() {
    alert(entriesDiv.style.display)
    entriesDiv.style.display = 'block';
    alert(entriesDiv.style.display)
}

function loadProfile() {
    profileDiv.style.display = 'block';
}

function loadSettings() {
    settingsDiv.style.display = 'block';
}

function unselectAllAnchorTags() {
    // Unmark other Tags
    for (const anchorTag of anchorTags) {
        anchorTag.classList.remove('active-link');
    }
}