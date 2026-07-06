## BTServer

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.bluetoothd")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.bluetoothd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.bluetoothd")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.bluetoothd")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
+				(extension "com.apple.assets.read")
 				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
-				(subpath "${HOME}/Library/HTTPStorages/com.apple.bluetoothd")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.bluetoothd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.bluetoothd")
 		)
 	)
 )

 
 (allow file-read*
 	(require-all
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
-		(extension "com.apple.sandbox.pty")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
 	)
 )
 (allow file-read*
 	(require-all
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(literal "/dev/ttys*")
+		(extension "com.apple.sandbox.pty")
+		(regex #"^/dev/ttys([0-9])*")
 	)
 )
 (allow file-read*

 		(extension "com.apple.app-sandbox.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")

 	(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 )
 
-(allow file-read-data
-	(require-all
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-	)
-)
-(allow file-read-data
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
 (allow file-read-data
 	(require-all
 		(extension "com.apple.assets.read")

 		)
 	)
 )
+(allow file-read-data
+	(require-all
+		(literal "/dev/ttys*")
+		(extension "com.apple.sandbox.pty")
+		(regex #"^/dev/ttys([0-9])*")
+	)
+)
+(allow file-read-data
+	(require-all
+		(extension "com.apple.app-sandbox.read-write")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+		)
+	)
+)
 (allow file-read-data
 	(require-all
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")

 )
 (allow file-read-data
 	(require-all
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
-		(extension "com.apple.sandbox.pty")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
 	)
 )
 (allow file-read-data

 )
 (allow file-read-data
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-		)
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
 (allow file-read-data

 		(subpath "/Developer/Applications")
 		(subpath "/Library/Application Support/BTServer")
 		(subpath "/System")
-		(subpath "/System/Developer/Applications")
 		(subpath "/private/etc/bluetool")
 		(subpath "/private/preboot")
 		(subpath "/private/var/containers/Bundle")

 	(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 )
 
-(allow file-read-metadata
-	(require-all
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-	)
-)
-(allow file-read-metadata
-	(require-all
-		(extension "com.apple.sandbox.oopjit")
-		(subpath "/private/var/OOPJit")
-		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.assets.read")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(literal "/dev/ttys*")
+		(extension "com.apple.sandbox.pty")
+		(regex #"^/dev/ttys([0-9])*")
+	)
+)
+(allow file-read-metadata
+	(require-all
+		(extension "com.apple.app-sandbox.read-write")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
+		)
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(%entitlement-is-bool-true "com.apple.Contacts.database-allow")

 )
 (allow file-read-metadata
 	(require-all
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
-		(extension "com.apple.sandbox.pty")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")
-		)
+		(extension "com.apple.sandbox.oopjit")
+		(subpath "/private/var/OOPJit")
+		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
 (allow file-read-metadata

 
 (allow file-read-xattr
 	(require-all
-		(literal "/dev/ttys*")
-		(regex #"^/dev/ttys([0-9])*")
-		(extension "com.apple.sandbox.pty")
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
 	)
 )
 (allow file-read-xattr
 	(require-all
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
+		(literal "/dev/ttys*")
+		(extension "com.apple.sandbox.pty")
+		(regex #"^/dev/ttys([0-9])*")
 	)
 )
 (allow file-read-xattr

 		(extension "com.apple.app-sandbox.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
 			)
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+")

 		(global-name "com.apple.locationd.spi")
 		(global-name "com.apple.locationd.synchronous")
 		(global-name "com.apple.lsd.advertisingidentifiers")
-		(global-name "com.apple.lsd.modifydb")
 		(global-name "com.apple.lsd.openurl")
 		(global-name "com.apple.lsd.xpc")
 		(global-name "com.apple.marco")

 		(preference-domain "com.apple.PeoplePicker")
 		(preference-domain "com.apple.TelephonyUtilities")
 		(preference-domain "com.apple.ULLAConcierge")
+		(preference-domain "com.apple.assistant.public")
 		(preference-domain "com.apple.assistant.support")
 		(preference-domain "com.apple.avfoundation")
 		(preference-domain "com.apple.bluetooth")

 		(preference-domain "com.apple.PeoplePicker")
 		(preference-domain "com.apple.TelephonyUtilities")
 		(preference-domain "com.apple.ULLAConcierge")
+		(preference-domain "com.apple.assistant.public")
 		(preference-domain "com.apple.assistant.support")
 		(preference-domain "com.apple.avfoundation")
 		(preference-domain "com.apple.bluetooth")
```
