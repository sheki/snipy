#What
Snipy is a [pastebin](http://en.wikipedia.org/wiki/Pastebin) to store and read code snippets which runs on [Google App Engine (GAE)](http://code.google.com/appengine/).

#Why 
Lot of times you need to share code within the organization, for discussing issues, debugging, blaming. Sharing code on email is archaic and ugly.
Snipy will host a pastebin internally and allow you internal codesharing (provided your org. is on App Engine).

#How to use.
As of now, this code is not hosted on any app engine. (Plans for it in near future).
But you can download the code and deploy it using the App Engine Launcher.

#Code
Snipy is built using :

* [Flask](http://flask.pocoo.org/) - Basic and awesome web framework.
* [WTForms](http://wtforms.simplecodes.com/) - For form validation and generation.
* [Pygments](http://pygments.org/)  Python Syntax Highlighter , lexing is directly dependent on capabilities of Pygments:w

Snipy is more or less gluing together of a lot of available components on GAE.


#TODO's
* Supported Languages should be configurable. (Right now Java, Python, C/C++ are supported).

* Support description of snippet's

* Better CSS for the site.

* Better color combination for the highlighted code (aka Github).

* Support File Upload.

* User Authentication on GAE. ( Who snipped what).

* Comments on snippets  (ala Github GISTS).

* API to upload snippets.


# LICENSE :
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2011 Abhishek Kona <abhishek.kona@gmail.com>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this codebase, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
