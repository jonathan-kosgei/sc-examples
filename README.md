# Saharacluster code samples
Example code for the Saharacluster platform

**_Creating an app_**
 - To start navigate to http://saharacluster.com and register. Confirm your email to be able to proceed.
 - Click the + on the navbar and enter a name for your app. Your app will then be accessible at http://<app_name>.saharacluster.com.
 - Next, select an app type from the list, choosing either one of Python, PHP or Node. This will init your app with the basic tools for that language.
 
 **_Using this repository_**
```
  Clone this repo; via ssh
  # git clone git@github.com:jonathan-kosgei/sc-examples.git
  or http
  # git clone https://github.com/jonathan-kosgei/sc-examples.git
  
  We'll setup a PHP app for this example
  
  cd into the PHP directory
  # cd php
  
  Init a git repository
  # git init
  
  Navigate to your dashboard http://saharacluster.com/app/list.
  
  You should see the app you created listed there, copy the url under `Git` and paste it into the following command
  # git remote add origin <paste_the_git_url_here>
  
  Then run:
  # git add .
  # git commit -m 'Initial Commit'
  and finally;
  # git push origin master
  
  Enter the username you registered with and the password from your dashboard listed next to your app to authenticate.
  
```

**_After successully pushing your repo to your sc app you should see output similar to the following._**

```
jonathan@ubuntu:~/Projects/Saharacluster/Examples/saharacluster$ git push beta master
Username for 'http://git.test.saharacluster.com': jonathan-kosgei
Password for 'http://jonathan-kosgei@git.test.saharacluster.com': 
Counting objects: 141, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (133/133), done.
Writing objects: 100% (141/141), 1.14 MiB | 269.00 KiB/s, done.
Total 141 (delta 24), reused 0 (delta 0)
remote: python
remote: Already on 'master'
remote: requirements.txt
remote: Installing dependencies..
remote: Done installing dependencies..
remote: Stopping app
remote: Starting app
remote:    /===============================
remote:    | DEPLOYMENT COMPLETED
remote:    | Target branch: master
remote:    | Target folder: /app
remote:    | Tag name     : release_20160908-2035
remote:    | Saharacluster Ltd.,
remote:    \==============================
To http://git.test.saharacluster.com/jonathan-kosgei/test.git/
 * [new branch]      master -> master
```


**_Saharacluster will;_** 
 - Autoinstall all your app's dependencies listed in either one of a `requirements.txt` , `package.json` or `composer.json`. The file that SC looks for depends on the app type you selected when creating your app.
 - Create a private git repository for your app, limited to 200Mb of code. Use s3 or some other service to host your access/static files and use this repo for your code.
 
 
**_View your app!_**

From the dashboard click the link next to your app's name.
