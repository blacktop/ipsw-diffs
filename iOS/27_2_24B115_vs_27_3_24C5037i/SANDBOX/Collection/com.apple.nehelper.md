## com.apple.nehelper

> Group: ⬆️ Updated

```diff

 ;; (default) inherited from parent profile "baseline"
 (delegate default)
 
-(allow asr-parser-enter)
-
 (allow coalition-info)
 
 (allow consume-extension)

 		(literal "/private/var/preferences/com.apple.networkextension.plist")
 	)
 )
-(allow file-read*
-	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.networkd*")
-		(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-	)
-)
 (allow file-read*
 	(require-all
 		(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")

 		(system-attribute carrier-build)
 	)
 )
-(allow file-read*
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
-(allow file-read*
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkd*")
-		(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-	)
-)
 (allow file-read*
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension*")
+		(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
 (allow file-read*
 	(require-all
 		(extension "com.apple.assets.read")

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd*")
+		(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
 (allow file-read*
 	(require-all
 		(vnode-type DIRECTORY REGULAR-FILE)

 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension*")
-		(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
+		(literal "/private/var/Managed Preferences/mobile/com.apple.networkd*")
+		(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
 	)
 )
 (allow file-read*

 		(literal "/private/var/preferences/com.apple.networkextension.plist")
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(literal "/private/var/Managed Preferences/mobile/com.apple.networkd*")
-		(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")

 		(system-attribute carrier-build)
 	)
 )
-(allow file-read-metadata
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(literal "/private/var/preferences/com.apple.networkd*")
-		(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkextension*")
+		(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.assets.read")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "/private/var/preferences/com.apple.networkd*")
+		(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(vnode-type DIRECTORY REGULAR-FILE)

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkextension*")
-		(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
+		(literal "/private/var/Managed Preferences/mobile/com.apple.networkd*")
+		(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
 	)
 )
 (allow file-read-metadata

 (allow network*
 	(require-any
 		(literal "/private/var/run/racoon.sock")
-		(local udp "*:4500")
-		(local udp "*:500")
+		(local udp "*:*")
 	)
 )
 

 	(require-any
 		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
 		(literal "/private/var/run/racoon.sock")
-		(local udp "*:4500")
-		(local udp "*:500")
+		(local udp "*:*")
 	)
 )
 

 	(require-any
 		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
 		(literal "/private/var/run/racoon.sock")
-		(local udp "*:4500")
-		(local udp "*:500")
+		(local udp "*:*")
 	)
 )
 

 		(control-name "com.apple.network.statistics")
 		(literal "/private/var/run/mDNSResponder")
 		(literal "/private/var/run/racoon.sock")
-		(local udp "*:4500")
-		(local udp "*:500")
+		(local udp "*:*")
 		(remote tcp "*:*")
 		(remote udp "*:*")
 		(remote udp "*:443")
```
