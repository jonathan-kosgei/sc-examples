### Running this app
```
git clone git@github.com:jonathan-kosgei/sc-examples.git
cp sc-examples/node .
cd node
git init
git remote add origin <git url in your dashboard entry for this app>
git add .
git commit -m 'Init'
git push origin master
```

You should get output similar to the following
```
jonathan@ubuntu:~/Projects/node$ git push origin master
Username for 'http://git.test-node.saharacluster.com': jkosgei
Password for 'http://jkosgei@git.test-node.saharacluster.com': 
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 582 bytes | 0 bytes/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: node6
remote: Already on 'master'
remote: package.json
remote: Installing dependencies..
remote: [-] Pruning
remote: npm WARN package.json app.js@1.0.0 No description
remote: npm WARN package.json app.js@1.0.0 No repository field.
remote: npm WARN package.json app.js@1.0.0 No README data
remote: [-] Installing
remote: app.js@1.0.0 /app
remote: +-- body-parser@1.15.2 
remote: | +-- bytes@2.4.0 
remote: | +-- content-type@1.0.2 
remote: | +-- debug@2.2.0 
remote: | | `-- ms@0.7.1 
remote: | +-- depd@1.1.0 
remote: | +-- http-errors@1.5.1 
remote: | | +-- inherits@2.0.3 
remote: | | +-- setprototypeof@1.0.2 
remote: | | `-- statuses@1.3.1 
remote: | +-- iconv-lite@0.4.13 
remote: | +-- on-finished@2.3.0 
remote: | | `-- ee-first@1.1.1 
remote: | +-- qs@6.2.0 
remote: | +-- raw-body@2.1.7 
remote: | | `-- unpipe@1.0.0 
remote: | `-- type-is@1.6.14 
remote: |   +-- media-typer@0.3.0 
remote: |   `-- mime-types@2.1.13 
remote: |     `-- mime-db@1.25.0 
remote: `-- express@4.14.0 
remote:   +-- accepts@1.3.3 
remote:   | `-- negotiator@0.6.1 
remote:   +-- array-flatten@1.1.1 
remote:   +-- content-disposition@0.5.1 
remote:   +-- cookie@0.3.1 
remote:   +-- cookie-signature@1.0.6 
remote:   +-- encodeurl@1.0.1 
remote:   +-- escape-html@1.0.3 
remote:   +-- etag@1.7.0 
remote:   +-- finalhandler@0.5.0 
remote:   +-- fresh@0.3.0 
remote:   +-- merge-descriptors@1.0.1 
remote:   +-- methods@1.1.2 
remote:   +-- parseurl@1.3.1 
remote:   +-- path-to-regexp@0.1.7 
remote:   +-- proxy-addr@1.1.2 
remote:   | +-- forwarded@0.1.0 
remote:   | `-- ipaddr.js@1.1.1 
remote:   +-- range-parser@1.2.0 
remote:   +-- send@0.14.1 
remote:   | +-- destroy@1.0.4 
remote:   | `-- mime@1.3.4 
remote:   +-- serve-static@1.11.1 
remote:   +-- utils-merge@1.0.0 
remote:   `-- vary@1.1.0 
remote: 
remote: npm WARN app.js@1.0.0 No description
remote: npm WARN app.js@1.0.0 No repository field.
remote: Done installing dependencies..
remote: Restarting app
remote: [PM2] Starting /app/app.js in fork_mode (1 instance)
remote: [PM2] Done.
remote: ┌──────────┬────┬──────┬─────┬────────┬─────────┬────────┬─────┬────────┬──────────┐
remote: │ App name │ id │ mode │ pid │ status │ restart │ uptime │ cpu │ mem    │ watching │
remote: ├──────────┼────┼──────┼─────┼────────┼─────────┼────────┼─────┼────────┼──────────┤
remote: │ app      │ 0  │ fork │ 182 │ online │ 0       │ 0s     │ 0%  │ 0 B    │ disabled │
remote: └──────────┴────┴──────┴─────┴────────┴─────────┴────────┴─────┴────────┴──────────┘
remote:  Use `pm2 show <id|name>` to get more details about an app
remote:    /===============================
remote:    | DEPLOYMENT COMPLETED
remote:    | Target branch: master
remote:    | Target folder: /ns/app
remote:    | Tag name     : release_20170107-1207
remote:    | View your app at http://test-node.saharacluster.com
remote:    | Saharacluster Ltd.,
remote:    \==============================
To http://git.test-node.saharacluster.com/jkosgei/test-node.git/
   1019180..4904ce3  master -> master
```
