"""
    Module defines the blueprint for creating an Entry object and
     a Diary object, which is a container for entry objects
"""


from datetime import datetime


class Diary:
    """
        Models a Diary as an object with

        Properties :
            entries -  a list of all the Entry objects made

        Methods :

            get_entries() - returns all entries in entries list,

            get_entry(entry_id) - returns entry with given entry_id

            add_entry(*args) - appends an entry  to entries list
              [*args = Entry object properties]

            edit_entry(entry_id, **kwargs) - modifies the values of the
                specified properties for the specified entry_id

            delete_entry(entry_id) - removes the specified entry from
                the list of entries
    """

    def __init__(self):
        """
            Initialize diary object
        """
        # For saving entries
        self.entries = []

        # Keep track of entries saved, use this to asign entry_id
        self.entry_count = 0

    def __repr__(self):
        """
            Define schematic for representing a diary.
            For experimentation in Terminal
        """
        return '< Entries : {}>'.format(self.entries)

    def get_entries(self):
        """
            Retrieve all entries in self.entries
        """
        return self.entries

    def get_entry(self, id):
        """
            Retrieve entry whose entry.entry_id == id from self.entries
        """
        # Retrieve list of all entries
        entries = self.get_entries()
        # Check if any of the entry_ids matches id, and return that entry
        # If no match, return None
        result = None
        for entry in entries:
            if entry.entry_id == id:
                result = entry
                break

        return result

    def add_entry(self, title, body, tags):
        """
            Checks whether similar entry already exists
            If no similar, creates entry
        """
        existing_titles = [entry.entry_title for entry in self.get_entries()]
        existing_bodies = [entry.entry_body for entry in self.get_entries()]

        if not title in existing_titles and not body in existing_bodies:
            entry = Entry(title, body, tags)
            # Append entry object to self.entries
            self.entries.append(entry)

            # Update entry_count
            self.entry_count += 1

            # Autogenerated entry_id - assigned by counting entries so far created
            entry.entry_id = self.entry_count
        else:
            entry = None

        return entry

    def edit_entry(self, entry, properties_to_edit):
        """
            Finds entry where entry.entry_id == id
            Updates values entry's properties as in **kwargs
        """
        # Locate entry, if entry exists
        for key, value in properties_to_edit.items():
            setattr(entry, key, value)
        
        return entry


class Entry:
    """
        Models an entry as an object with

        Properties :

            entry_id (autogenerated on instantiation),
            entry_title,
            entry_body,
            entry_tags, and
            entry_timestamp (autogenerated on instantiation)
    """

    def __init__(self, entry_title, entry_body, entry_tags, entry_id=0):
        """
            Initialize entry object
        """
        self.entry_title = entry_title
        self.entry_body = entry_body
        self.entry_tags = entry_tags
        self.entry_id = entry_id  # Assigned proper value while being saved

        # Store autogenerated timestamp as a formatted str
        self.entry_created_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        """
            Define schematic for representing an entry.
            For experimentation in Terminal
        """
        return '<{} - {} : {}>'.format(self.entry_id, self.entry_title, self.entry_body)
