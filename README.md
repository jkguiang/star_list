Hosted here: http://uaf-8.t2.ucsd.edu/~jguiang/dump/list_example/#

#### Files:
1. `database.json`
    - JSON that maps star data/metadata to corresponding files
2. `favicon.ico`
    - tab image, found [here](https://icons8.com/icon/43473/shooting-stars-filled)
3. `galaxy.jpg`
    - background image, found [here](https://en.wikipedia.org/wiki/Galaxy#/media/File:M82_HST_ACS_2006-14-a-large_web.jpg)
4. `index.html`
    - static aspects of the page (i.e. main title, links to CSS and other JS dependencies, etc.)
    - uses: [Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/), [jQuery](https://jquery.com/)
5. `index.js`
    - dynamic aspects of the page (i.e. generates list from JSON, handles "search" functionality)
6. `mk_json.py`
    - generates a randomly-seeded JSON with pseudo data to simulate actual database
