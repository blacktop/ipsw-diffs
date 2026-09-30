## com.apple.nehelper

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/Caches/nehelper")
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/Caches/nehelper")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/Caches/nehelper")
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/Caches/nehelper")
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(extension "com.apple.assets.read")
+				(require-any
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
 			(subpath "${HOME}/Library/Caches/nehelper")
 			(subpath "${HOME}/Library/Cookies")
 		)

 	)
 )
 
-(allow file-read*
-	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-	)
-)
-(allow file-read*
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
-		)
-	)
-)
 (allow file-read*
 	(require-all
 		(%entitlement-is-present "com.apple.private.networkextension.configuration")

 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var")
+		(literal "/private/var/Managed Preferences/mobile/com.apple.networkd*")
+		(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
+(allow file-read*
+	(require-all
+		(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
+		(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/System/Library/Carrier Bundles")
 		(require-any
-			(require-all
-				(literal "/private/var/Managed Preferences/mobile/com.apple.networkd*")
-				(require-any
-					(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-					(require-all
-						(literal "/private/var/preferences/com.apple.networkextension*")
-						(require-any
-							(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-							(require-all
-								(literal "/private/var/preferences/com.apple.networkd*")
-								(require-any
-									(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-											(require-all
-												(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-												(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-				(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-			)
-			(require-all
-				(literal "/private/var/preferences/com.apple.networkd*")
-				(require-any
-					(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-							(require-all
-								(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-								(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(literal "/private/var/preferences/com.apple.networkextension*")
-				(require-any
-					(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-					(require-all
-						(literal "/private/var/preferences/com.apple.networkd*")
-						(require-any
-							(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-									(require-all
-										(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-										(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-					(require-all
-						(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-						(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-					)
-				)
-			)
+			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
 (allow file-read*
 	(require-all
 		(extension "com.apple.sandbox.oopjit")

 )
 (allow file-read*
 	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/VPN-*")
-		(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
+		(literal "/private/var/preferences/com.apple.networkd*")
+		(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(literal "/private/var/preferences/SystemConfiguration/VPN-*")
+				(require-any
+					(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+				)
+			)
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
+		)
 	)
 )
 (allow file-read*

 )
 (allow file-read*
 	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
+		(literal "/private/var/preferences/com.apple.networkextension*")
+		(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
 	)
 )
 (allow file-read*

 	)
 )
 
-(allow file-read-metadata
-	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(subpath "/System/Library/Carrier Bundles")
-		(regex #"^/System/Library/Carrier Bundles/.*\.png$")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(extension "com.apple.assets.read")
-		(require-any
-			(subpath "${HOME}/Library/Assets")
-			(subpath "/private/var/MobileAsset")
-		)
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-present "com.apple.private.networkextension.configuration")

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/private/var")
+		(literal "/private/var/Managed Preferences/mobile/com.apple.networkd*")
+		(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
+		(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/System/Library/Carrier Bundles")
 		(require-any
-			(require-all
-				(literal "/private/var/Managed Preferences/mobile/com.apple.networkd*")
-				(require-any
-					(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-					(require-all
-						(literal "/private/var/preferences/com.apple.networkextension*")
-						(require-any
-							(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-							(require-all
-								(literal "/private/var/preferences/com.apple.networkd*")
-								(require-any
-									(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-									(require-all
-										(subpath "${FRONT_USER_HOME}")
-										(require-any
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-											(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-											(require-all
-												(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-												(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-				(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-			)
-			(require-all
-				(literal "/private/var/preferences/com.apple.networkd*")
-				(require-any
-					(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-							(require-all
-								(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-								(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(literal "/private/var/preferences/com.apple.networkextension*")
-				(require-any
-					(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-					(require-all
-						(literal "/private/var/preferences/com.apple.networkd*")
-						(require-any
-							(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
-							(require-all
-								(subpath "${FRONT_USER_HOME}")
-								(require-any
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-									(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-									(require-all
-										(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-										(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(require-all
-				(subpath "${FRONT_USER_HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-					(require-all
-						(literal "/private/var/Managed Preferences/mobile/com.apple.networkextension*")
-						(regex #"^/private/var/Managed Preferences/mobile/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
-					)
-				)
-			)
+			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(subpath "/usr/local/lib")
+		(system-attribute carrier-build)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.sandbox.oopjit")

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/VPN-*")
-		(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
+		(literal "/private/var/preferences/com.apple.networkd*")
+		(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(subpath "/private/var")
+		(require-any
+			(require-all
+				(literal "/private/var/preferences/SystemConfiguration/VPN-*")
+				(require-any
+					(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
+					(require-all
+						(subpath "${FRONT_USER_HOME}")
+						(require-any
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+						)
+					)
+				)
+			)
+			(require-all
+				(subpath "${FRONT_USER_HOME}")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+				)
+			)
+		)
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
+		)
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(subpath "/usr/local/lib")
-		(system-attribute carrier-build)
+		(literal "/private/var/preferences/com.apple.networkextension*")
+		(regex #"^/private/var/preferences/com\.apple\.networkextension(\.[-0-9A-Z_a-z]+)?\.plist")
 	)
 )
 (allow file-read-metadata

 
 (allow file-ungraft)
 
+(allow file-write*
+	(require-all
+		(literal "/private/var/preferences/SystemConfiguration/VPN-*")
+		(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
+	)
+)
 (allow file-write*
 	(require-all
 		(literal "/private/var/preferences/com.apple.networkd*")

 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/nehelper")
 	)
 )
-(allow file-write*
-	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/VPN-*")
-		(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
-	)
-)
 (allow file-write*
 	(require-all
 		(literal "/private/var/preferences/com.apple.networkextension*")

 
 (allow file-write-create
 	(require-all
-		(literal "/private/var/preferences/com.apple.networkd*")
-		(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
+		(literal "/private/var/preferences/SystemConfiguration/VPN-*")
+		(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
 	)
 )
 (allow file-write-create
 	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/VPN-*")
-		(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
+		(literal "/private/var/preferences/com.apple.networkd*")
+		(regex #"^/private/var/preferences/com\.apple\.networkd(\.[-0-9A-Z_a-z]+)?\.plist")
 	)
 )
 (allow file-write-create

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/nehelper")
 	)
 )

 		(subpath "/private/var/OOPJit")
 	)
 )
+(allow file-write-unlink
+	(require-all
+		(literal "/private/var/preferences/SystemConfiguration/VPN-*")
+		(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
+	)
+)
 (allow file-write-unlink
 	(require-all
 		(literal "/private/var/preferences/com.apple.networkd*")

 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/nehelper")
 	)
 )
-(allow file-write-unlink
-	(require-all
-		(literal "/private/var/preferences/SystemConfiguration/VPN-*")
-		(regex #"^/private/var/preferences/SystemConfiguration/VPN-[^/]+\.plist")
-	)
-)
 (allow file-write-unlink
 	(require-all
 		(literal "/private/var/preferences/com.apple.networkextension*")
```
