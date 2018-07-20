'use strict';

document.addEventListener('DOMContentLoaded', () => {
    addClickListeners();

    // Load proper nav-bar height
    assignProperNavHeight();

    // Add click listerners to entries and entry buttons
    // Event delegation, to account for newly added entries
    addClickListenersToEntries();
    addClickListenersToButtons();

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
        // Assign navbar height
        assignProperNavHeight();
    } 
    else if (tag.id === 'a-profile') {
        loadProfile();
    } 
    else if (tag.id === 'a-settings') {
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
    // Assign nav-bar height
    assignProperNavHeight();
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

function addClickListenersToButtons() {
    // Delete and Edit btns : action on click.
    // Use event delegation, because of newly added entries
    document.addEventListener('click', (event) => {
        if (event.target && (event.target.innerHTML === 'Delete'
         || event.target.innerHTML === 'Edit' || event.target.innerHTML === 'New')) {
            const clickedBtn = event.target;
            const parentEntry = clickedBtn.parentElement;
            if (clickedBtn.innerHTML === 'Delete') {
                parentEntry.remove();
            }
            else if(clickedBtn.innerHTML === 'New') {
                const title = prompt("Provide a title : ", "");
                const body = prompt("Type out your entry : ", "");
                const tags = prompt("Tags : ", "");
                if (title && body) {
                    addNewEntry(title, body, tags);
                }
            }
        }
    });
}

function addNewEntry(title, body, tags) {
    // Append newly created entry to list of entries
    const lastEntry = document.getElementById('entries-list').lastElementChild;
    const newEnty = lastEntry.cloneNode(true);
    newEnty.getElementsByTagName('h4')[0].innerText = `#${title}`;
    newEnty.getElementsByTagName('p')[1].innerText = `${body}`;
    newEnty.getElementsByTagName('p')[2].getElementsByTagName('span')[2].innerText = `${tags}`;

    document.getElementById('entries-list').prepend(newEnty);
    // Re-assign nav-bar height
    assignProperNavHeight();
}

function addClickListenersToEntries() {
    // Toggle entry contents on clicking show more. Use event delegation
    document.addEventListener('click', (event) => {
        if (event.target && event.target.innerHTML === 'Show more') {
            const clickedShowMore = event.target;
            clickedShowMore.nextElementSibling.classList.toggle('visible');
            clickedShowMore.innerHTML = 'Show less';
        }
        else if (event.target && event.target.innerHTML === 'Show less') {
            const clickedShowMore = event.target;
            clickedShowMore.nextElementSibling.classList.toggle('visible');
            clickedShowMore.innerHTML = 'Show more';
        }
    });
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

function assignProperNavHeight() {
    // Check height of container, assign to nav bar
    const heightParentContainer = document.getElementById('parent-container').offsetHeight;
    const heightHeader = document.getElementById('header').offsetHeight;
    const height = `${heightParentContainer - heightHeader}px`;
    document.getElementById('nav-bar').style.height = height;
};
