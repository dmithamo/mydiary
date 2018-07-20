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
    // Clear page; prepare to load seetings or entries or profile
    for (const contentDiv of contentDivs) {
        contentDiv.style.display = 'none';
    }

    for (const contentList of contentLists) {
        contentList.style.display = 'none';
    }
};

function loadEntries() {
    // Load entries on clicking 'entries' a-tag
    entriesDiv.style.display = 'block';
    entriesList.style.display = 'block';
};

function loadProfile() {
    // Display profileDiv and contents
    profileDiv.style.display = 'block';
    profileList.style.display = 'block';
};

function loadSettings() {
    // Load settings on clicking 'settings' a-tag
    settingsDiv.style.display = 'block';
    settingsList.style.display = 'block';
};

function unselectAllAnchorTags() {
    // Unmark other Tags
    for (const anchorTag of anchorTags) {
        anchorTag.classList.remove('active-link');
    }
};

// Select all buttons
const buttons = document.querySelectorAll('button');
// add click listeners to btns
addClickListenersToButtons();

function addClickListenersToButtons() {
    // Delete and Edit btns : action on click
    for (const btn of buttons) {
        btn.addEventListener('click', (event) => {
            const clickedBtn = event.target;
            const parentEntry = clickedBtn.parentElement;

            if (clickedBtn.innerHTML === 'Delete') {
                parentEntry.remove();

            } else if(clickedBtn.innerHTML === 'New') {
                clickedBtn.setAttribute('style', 'background-color : black; color : blue')
                // Thinking about this ...
            }
        
        });
    }
}

// Select all entries' 'Show More' links
const showMoreLinks = document.querySelectorAll('.show-more');
// Add click listeners
addClickListenersToEntries();

function addClickListenersToEntries() {
    // Toggle entry contents on clicking show more
    for (const showMore of showMoreLinks) {
        showMore.addEventListener('click', (event) => {
            const clickedShowMore = event.target;
            clickedShowMore.nextElementSibling.classList.toggle('visible');

            if (clickedShowMore.innerHTML === 'Show more') {
                clickedShowMore.innerHTML = 'Show less';
            } else {
                clickedShowMore.innerHTML = 'Show more';
            }
        });
    }
}

// Select all entry titles and entry bodies 
const entryTitles = document.querySelectorAll('.entry-title');
const entryBodies = document.querySelectorAll('.entry-body');
// Combine into one array for common action
const titlesAndBodies = [...entryTitles, ...entryBodies];

// Add dblclick listeners
onClickTitlesAndBodies();

function onClickTitlesAndBodies() {
    // On dblclick, provide prompt for editing
    for (const entryParam of titlesAndBodies) {
        // Add tool-tip
        entryParam.setAttribute('title', 'Double click the title or body to edit it');
        // Add dblclick listener, provide propmt on dblclick
        entryParam.addEventListener('dblclick', (event) => {
            const clickedParam = event.target;
            const newText = prompt('Edit this to?', clickedParam.innerHTML)
            if (newText) {
                clickedParam.innerHTML = newText;
            };
        });
    }
}