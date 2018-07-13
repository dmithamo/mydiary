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

function loadContents(tag) {
    if (tag.id === 'a-entries') {
        loadEntries();
    } else if (tag.id === 'a-profile') {
        loadProfile();
    } else if (tag.id === 'a-settings') {
        loadSettings();
    }
    
}

function loadEntries() {
    alert("Entries!!");
}

function loadProfile() {
    alert("Profile!!!");
}

function loadSettings() {
    alert("Settings!!!");
}

function unselectAllAnchorTags() {
    // Unmark other Tags
    for (const anchorTag of anchorTags) {
        anchorTag.classList.remove('active-link');
    }
}