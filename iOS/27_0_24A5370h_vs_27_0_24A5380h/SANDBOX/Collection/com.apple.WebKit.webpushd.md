## com.apple.WebKit.webpushd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(subpath "/private/var")
 		(require-any
+			(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 			(require-all
 				(subpath "${HOME}")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Preferences/ByHost/\.GlobalPreferences\.")
 			)
-			(subpath "/private/var/preferences/Logging")
 		)
 	)
 )

 		(literal "/private/etc/master.passwd")
 		(literal "/private/etc/passwd")
 		(literal "/private/etc/services")
-		(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 		(literal "/private/var/db/os_eligibility/eligibility.plist")
 		(subpath "${HOME}/Library/WebClips")
 		(subpath "${HOME}/Library/WebKit/WebPush")

 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
 		(subpath "/private/var/db/mds")
+		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")
 		(subpath "/usr/share")
 	)

 	(require-all
 		(subpath "/private/var")
 		(require-any
+			(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 			(require-all
 				(subpath "${HOME}")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Preferences/ByHost/\.GlobalPreferences\.")
 			)
-			(subpath "/private/var/preferences/Logging")
 		)
 	)
 )

 		(literal "/private/etc/master.passwd")
 		(literal "/private/etc/passwd")
 		(literal "/private/etc/services")
-		(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 		(literal "/private/var/db/os_eligibility/eligibility.plist")
 		(literal "/usr/lib/log")
 		(literal "/usr/local/lib/log")

 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
 		(subpath "/private/var/db/mds")
+		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")
 		(subpath "/usr/share")
 	)
```
