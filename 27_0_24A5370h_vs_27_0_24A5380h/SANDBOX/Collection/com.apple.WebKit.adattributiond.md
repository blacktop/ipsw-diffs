## com.apple.WebKit.adattributiond

> Group: ⬆️ Updated

```diff

 	(require-all
 		(subpath "/private/var")
 		(require-any
+			(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 			(literal "/private/var/preferences/com.apple.networkd.plist")
 			(require-all
 				(subpath "${HOME}")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Preferences/ByHost/\.GlobalPreferences\.")
 			)
-			(subpath "/private/var/preferences/Logging")
 		)
 	)
 )

 		(literal "/System/Library/DarwinDirectory/system/recordStore.data")
 		(literal "/dev/urandom")
 		(literal "/private/etc/master.passwd")
-		(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 		(literal "/private/var/db/nsurlstoraged/dafsaData.bin")
 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 		(subpath "/")

 		(subpath "/private/preboot/Cryptexes/OS")
 		(subpath "/private/var/db/mds")
 		(subpath "/private/var/mobile/Library/com.apple.webkit.adattributiond")
+		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")
 		(subpath "/usr/share")
 	)

 	(require-all
 		(subpath "/private/var")
 		(require-any
+			(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 			(literal "/private/var/preferences/com.apple.networkd.plist")
 			(require-all
 				(subpath "${HOME}")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Preferences/ByHost/\.GlobalPreferences\.")
 			)
-			(subpath "/private/var/preferences/Logging")
 		)
 	)
 )

 		(literal "/System/Library/DarwinDirectory/system/recordStore.data")
 		(literal "/dev/urandom")
 		(literal "/private/etc/master.passwd")
-		(literal "/private/var/db/DarwinDirectory/local/recordStore.data")
 		(literal "/private/var/db/nsurlstoraged/dafsaData.bin")
 		(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 		(literal "/usr/lib/log")

 		(subpath "/private/preboot/Cryptexes/OS")
 		(subpath "/private/var/db/mds")
 		(subpath "/private/var/mobile/Library/com.apple.webkit.adattributiond")
+		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")
 		(subpath "/usr/share")
 	)

 
 (allow mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.SystemConfiguration.PPPController"))
 		(require-not (global-name "com.apple.SystemConfiguration.SCNetworkReachability"))
-		(require-not (global-name "com.apple.networkd"))
 		(require-not (global-name "com.apple.nsurlstorage-cache"))
 		(require-not (global-name "com.apple.symptomsd"))
+		(require-not (global-name "com.apple.SystemConfiguration.PPPController"))
+		(require-not (global-name "com.apple.networkd"))
 		(require-any
 			(global-name "com.apple.CoreServices.coreservicesd")
 			(global-name "com.apple.SecurityServer")
 			(global-name "com.apple.analyticsd")
 			(global-name "com.apple.containermanagerd")
+			(global-name "com.apple.cookied")
+			(global-name "com.apple.distributed_notifications@Uv3")
 			(global-name "com.apple.lsd.mapdb")
 			(global-name "com.apple.lsd.modifydb")
 			(global-name "com.apple.ocspd")
-			(require-any
-				(global-name "com.apple.cookied")
-				(global-name "com.apple.distributed_notifications@Uv3")
-			)
 		)
 	)
 )
```
