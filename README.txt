Run Metsploitable virtual machine in background.
Find out the site's IP address.

Configure localhost port 8080 to be your proxy of choice (Using FoxyProxy on firefox is an easy way to do so)

Before you access the website, run proxy2.py using the command line, by typing "python proxy2.py" (obviously you need to have python 2.7 installed on your machine)

Now you can access the site by using previously-discovered Mutillidae IP address.

Go to pages Register/Login/Add to blog/Set color and try various SQLi/HTMLi/XSS attacks - Those pages should be protected when the proxy is up.

Apart from seeing the attacks being blocked, you can see the network traffic in the cmd window. In the cases we modify the requests, you will be able to see the changes. 

Now, give us a perfect score ;)
