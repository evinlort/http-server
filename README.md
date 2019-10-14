# http-server
Custom HTTP server with routing

Use web.py to define route (by name) to specific controller. Syntax is `Router("COMMAND", "PATH", "CONTROLLER:METHOD")`

Put the controller with defined name into controllers directory
Controller is a python file with methods which may return a response (strings for now)
