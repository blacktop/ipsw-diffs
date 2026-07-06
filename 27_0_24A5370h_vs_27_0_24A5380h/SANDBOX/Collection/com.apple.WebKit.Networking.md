## com.apple.WebKit.Networking

> Group: ⬆️ Updated

```diff

 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/preboot/Cryptexes/OS/System/Library")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_WebContentRestrictions")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")

 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/preboot/Cryptexes/OS/System/Library")
 		(subpath "/private/var/MobileAsset/AssetsV2/com_apple_MobileAsset_WebContentRestrictions")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")

 )
 (allow mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.networkscored"))
-		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
+		(require-not (global-name "com.apple.hangtracerd"))
+		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (xpc-service-name "*"))

 			(require-all
 				(state-flag "BlockNetworkAccess")
 				(local tcp "*:*")
-				(require-not (remote tcp "*:*"))
 				(require-not (remote udp "*:*"))
+				(require-not (remote tcp "*:*"))
 				(require-not (literal "/private/var/run/mDNSResponder"))
 			)
 		)

 (allow socket-option-set
 	(require-all
 		(socket-option-level IPPROTO_IPV6)
-		(socket-option-name 35 36 61 62)
+		(socket-option-name 27 35 36 61 62)
 	)
 )
 (allow socket-option-set

 	)
 )
 (allow socket-option-set
-	(socket-option-name 20 27 7)
+	(socket-option-name 7 20 27)
 )
 
 (deny syscall-unix)
```
