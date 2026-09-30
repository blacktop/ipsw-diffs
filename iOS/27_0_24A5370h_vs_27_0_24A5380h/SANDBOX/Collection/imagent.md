## imagent

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
-			(subpath "/private/var/tmp/com.apple.MobileSMS")
-		)
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
-			(subpath "/private/var/tmp/com.apple.MobileSMS")
-		)
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
-			(subpath "/private/var/tmp/com.apple.MobileSMS")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
-			(subpath "/private/var/tmp/com.apple.MobileSMS")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.identityservices.send")
-		(require-any
-			(subpath "${HOME}/Library/SMS")
-			(subpath "${PROCESS_TEMP_DIR}")
-			(subpath "/private/var/tmp")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
 				(require-any
 					(require-all
 						(subpath "/private/var")

 				)
 			)
 			(require-any
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
-				(subpath "/private/var/tmp/com.apple.MobileSMS")
+				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+				(subpath "/private/var/tmp/com.apple.messages")
 			)
 			(subpath "${HOME}/Library/Caches/com.apple.MobileSMS")
 			(subpath "${HOME}/Library/MessagesMetaData")
 			(subpath "${HOME}/Library/SMS")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileSMS")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS")
-			(subpath "/private/var/tmp/com.apple.messages")
+			(subpath "/private/var/tmp/com.apple.MobileSMS")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.identityservices.send")
+		(require-any
+			(subpath "${HOME}/Library/SMS")
+			(subpath "${PROCESS_TEMP_DIR}")
+			(subpath "/private/var/tmp")
 		)
 	)
 )

 	(require-all
 		(subpath "/private/var")
 		(require-any
-			(literal "/private/var/preferences/SystemConfiguration/com.apple.radios.plist")
 			(literal "/private/var/preferences/com.apple.networkd.plist")
 			(require-all
 				(require-any

 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS(/|$)")
 				)
 			)
+			(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDM.plist")
 		)
 	)
 )

 		(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
 		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PayloadDependency.plist")
+		(literal "/private/var/preferences/SystemConfiguration/com.apple.radios.plist")
 		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles")
 		(subpath "${FRONT_USER_HOME}/Library/Carrier Bundles/Overlay")
 		(subpath "${HOME}/Library/AddressBook")

 		(subpath "/System/Cryptexes")
 		(subpath "/private/preboot/Cryptexes")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS")
-		(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/MDM.plist")
 		(subpath "/private/var/tmp/com.apple.MobileSMS")
 		(subpath "/private/var/tmp/com.apple.messages")
 	)

 )
 (allow file-write*
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS(/|$)")
 	)
 )

 
 (allow file-write-create
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS(/|$)")
 	)
 )

 )
 (allow file-write-unlink
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS(/|$)")
 	)
 )
```
