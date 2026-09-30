## accessoryd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.accessoryd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/Caches/com.apple.iapd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
 		(subpath "${HOME}/Library/Caches/com.apple.iapd")
 	)
 )

 					(extension "com.apple.security.exception.files.absolute-path.read-write")
 					(extension "com.apple.security.exception.files.home-relative-path.read-only")
 					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-					(subpath "${HOME}/Library/Caches/com.apple.iapd")
 				)
 			)
 			(subpath "${HOME}/Library/Caches/com.apple.accessoryd")

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")
+		(subpath "${HOME}/Library/Caches/com.apple.iapd")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(require-all
+				(subpath "${HOME}/Library/Assets")
+				(extension-class "com.apple.aned.read-only")
+			)
+			(require-all
+				(subpath "/private/var/MobileAsset")
+				(extension-class "com.apple.aned.read-only")
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(subpath "${HOME}/Library/Caches/com.apple.iapd")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "${HOME}/Library/Caches/com.apple.iapd")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.accessoryd")
-				(extension-class "com.apple.aned.read-only")
+				(extension-class "com.apple.mediaserverd.read")
 			)
 			(subpath "${HOME}/Library/Caches/com.apple.iapd")
 		)

 )
 (allow file-read*
 	(require-all
-		(subpath "/System/Library/Carrier Bundles")
+		(subpath "/private/var")
+		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
 		)
 	)
 )

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 			)
 		)
 	)

 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
+		(subpath "/System/Library/Carrier Bundles")
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 		)
 	)
 )

 )
 (allow file-read-data
 	(require-all
-		(subpath "/System/Library/Carrier Bundles")
+		(subpath "/private/var")
+		(subpath "${FRONT_USER_HOME}")
 		(require-any
-			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
+			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
 		)
 	)
 )

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 			)
 		)
 	)

 )
 (allow file-read-data
 	(require-all
-		(subpath "/private/var")
-		(subpath "${FRONT_USER_HOME}")
+		(subpath "/System/Library/Carrier Bundles")
 		(require-any
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-			(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/GeoServices($|/)")
+			(regex #"^/System/Library/Carrier Bundles/.*/carrier\.plist$")
+			(regex #"^/System/Library/Carrier Bundles/.*\.png$")
 		)
 	)
 )

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
-			)
-			(require-all
-				(subpath "${HOME}")
 				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 					)
 				)
 			)
-		)
-	)
-)
-(allow file-write*
-	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")
+			(require-all
+				(subpath "${HOME}")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+			)
 		)
 	)
 )

 		)
 	)
 )
+(allow file-write*
+	(require-all
+		(vnode-type REGULAR-FILE)
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")
+			)
+		)
+	)
+)
 (allow file-write*
 	(require-any
 		(literal "${HOME}/Library/Logs/CrashReporter/accessoryd*")

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 			)
 		)
 	)

 )
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")
+			)
 		)
 	)
 )

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+				(require-any
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+					(require-all
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+					)
+				)
 			)
 			(require-all
 				(subpath "${HOME}")
-				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
-					)
-				)
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 			)
 		)
 	)

 )
 (allow file-write-data
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")

 )
 (allow file-write-data
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")
+			)
 		)
 	)
 )

 		(require-any
 			(require-all
 				(subpath "${FRONT_USER_HOME}")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
-			)
-			(require-all
-				(subpath "${HOME}")
 				(require-any
-					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
 					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/ExternalAccessory/ea[.0-9]+$")
+						(subpath "${HOME}")
+						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
 					)
 				)
 			)
-		)
-	)
-)
-(allow file-write-unlink
-	(require-all
-		(vnode-type REGULAR-FILE)
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
-			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")
+			(require-all
+				(subpath "${HOME}")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Media/([^/]+/)?iTunes_Control(/|$)")
+			)
 		)
 	)
 )

 		)
 	)
 )
+(allow file-write-unlink
+	(require-all
+		(vnode-type REGULAR-FILE)
+		(require-any
+			(require-all
+				(vnode-type REGULAR-FILE)
+				(subpath "${HOME}/Library/AddressBook")
+				(%entitlement-is-bool-true "com.apple.Contacts.database-allow")
+				(extension "com.apple.tcc.kTCCServiceAddressBook")
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.accessoryd")
+				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.iapd")
+			)
+		)
+	)
+)
 (allow file-write-unlink
 	(require-any
 		(literal "${HOME}/Library/Logs/CrashReporter/accessoryd*")
```
