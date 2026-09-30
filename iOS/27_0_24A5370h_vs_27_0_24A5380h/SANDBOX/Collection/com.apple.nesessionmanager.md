## com.apple.nesessionmanager

> Group: ⬆️ Updated

```diff

 		(literal "/private/var/run/ppp[0-9]")
 		(literal "/private/var/run/racoon.pid")
 		(literal "/usr/local/bin/dnssdutil")
-		(literal "/usr/sbin")
 		(regex #"/private/var/preferences/com.apple.networkextension.([-a-z_A-Z0-9])+\.plist")
 		(regex #"/private/var/run/ppp([0-9])+\.pid")
 		(subpath "${FRONT_USER_HOME}/Containers/Bundle/Application")

 		(literal "/private/var/run/ppp[0-9]")
 		(literal "/private/var/run/racoon.pid")
 		(literal "/usr/local/bin/dnssdutil")
-		(literal "/usr/sbin")
 		(regex #"/private/var/preferences/com.apple.networkextension.([-a-z_A-Z0-9])+\.plist")
 		(regex #"/private/var/run/ppp([0-9])+\.pid")
 		(subpath "${FRONT_USER_HOME}/Containers/Bundle/Application")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.nesessionmanager")
 	)
 )
```
