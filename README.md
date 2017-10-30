# practice-garage
Practice for google app engine python with jinja2 jquery and webpack

download the project

## Setup _google app engine_

- install 
[google app engine](https://cloud.google.com/appengine/docs/standard/python/download)
-- _The app-engine-python package is required_<br>

see [GAE local run](https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server)




## Setup _npm and webpack_

- install [nodejs](https://nodejs.org/en/) -- _install recommended version_

use the commandline and go to the project. Now type `npm install`<br>
this will install all java script dependencies for the project.

now webpack needs to watch the javascript files and place the generated files in the static/dist folder.<br>
type `npm run dev`
<br>since watcher is defined in dev modus the script will keep running and detect changes.


----- to fix error there are to many files.<br>
go to :<br>
`/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/mtime_file_watcher.py`
    
below the
```
for dirpath, dirnames, filenames in os.walk(self._directory, followlinks=True):```

place at line ~167: _ofcourse this line number can be different_
```
if '/node_modules/' in dirpath:
    continue```