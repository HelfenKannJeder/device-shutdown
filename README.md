# Device Shutdown 

This is a simple container which maps a REST endpoint to the creation of a file.
The reason is to be able to shutdown the host system.
This repository is inspired by [the following stackoverflow](https://stackoverflow.com/questions/42660690/is-it-possible-to-shut-down-the-host-machine-by-executing-a-command-on-one-of-it) post and can be used together with `inotifywait`.
