# carddav-merger
Simple Python Tool to Merge Several CardDav Address Books into One.

## Scope & Goal

* Merges several CardDav address books into one *without deleting* any existing contacts. Target is to gather all contacts from several address books into one without losing any data that may be deleted in the source address books.
* Tailored for and tested with [NextCloud](https://nextcloud.com) CardDav address books.
* Assumes that UIDs of contacts are unique across all address books.
* Does not consider changes made to contacts in the target address book. Those will be overwritten by the contacts from the source address books on the next sync.

## Usage

* Clone the repository
* Install dependencies via `pip install -group deploy`
* Create a file `config.toml` in the root directory with the following content:
  
  ```toml
  [target]
  username="username-target"
  password="password-target"
  address_book_url="https://target.server/path/to/addressbook/"
  
  [sources.source-1]
  username="username-source-1"
  password="password-source-1"
  address_book_url = "https://source1.server/path/to/addressbook/"
  
  [sources.source-2]
  username="username-source-2"
  password="password-source-2"
  address_book_url = "https://source2.server/path/to/addressbook/"
  ```
  
  You can add an abitrary number of source address books. The source IDs can be any string, but must be unique.

* Adapt the `main.py` file to your needs, e.g. to choose a different comparison method or to change the logging level.
* Run the script via `python main.py path/to/config.toml`.

## Status and Contributing

This is your usual "let me quickly set up an automation that works for me" project.
It works for me and I don't currently have any plans to extend it.
However, if it's useful for you and you want to contribute, feel free to open an issue or a pull request.
In particular, I'm open to adding
  * support for other CardDav servers than NextCloud.
  * support for different configuration formats that don't require storing credentials in plain text.
  * better documentation (docstrings in python code, sphinx docs, etc.)
  * proper Python packaging & PyPI publishing.