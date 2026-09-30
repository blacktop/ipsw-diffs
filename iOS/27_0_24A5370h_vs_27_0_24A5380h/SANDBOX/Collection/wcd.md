## wcd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox/com.apple.watchconnectivity")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/com.apple.watchconnectivity")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents/Inbox/com.apple.watchconnectivity")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Application Support/com.apple.watchconnectivity")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches")
+		(extension-class "com.apple.identityservices.send")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-				)
-			)
-			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(require-any
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents/Inbox/com\.apple\.watchconnectivity/")
 					(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/com\.apple\.watchconnectivity/")

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Caches")
-		(extension-class "com.apple.identityservices.send")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(subpath "${PROCESS_TEMP_DIR}")
 		(extension-class "com.apple.identityservices.send")
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(subpath "/private/var/tmp")
-		(extension-class "com.apple.identityservices.send")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension "com.apple.wcd.readonly")
 		(require-any
-			(require-all
-				(require-any
-					(subpath "/AppleInternal/Applications")
-					(subpath "/System/Developer/Applications")
-				)
-				(extension-class "com.apple.identityservices.send")
-			)
 			(require-all
 				(require-any
 					(subpath "/private/var/factory_mount/[^/]+/Applications")

 				(subpath "${FRONT_USER_HOME}/Containers/Bundle")
 				(extension-class "com.apple.identityservices.send")
 			)
+			(require-all
+				(subpath "/AppleInternal/Applications")
+				(extension-class "com.apple.identityservices.send")
+			)
 			(require-all
 				(subpath "/Applications")
 				(extension-class "com.apple.identityservices.send")

 				(subpath "/Developer/Applications")
 				(extension-class "com.apple.identityservices.send")
 			)
+			(require-all
+				(subpath "/System/Developer/Applications")
+				(extension-class "com.apple.identityservices.send")
+			)
 			(require-all
 				(subpath "/private/var")
 				(require-any

 )
 (allow file-issue-extension
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(require-any
 			(require-all
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/Library/Application Support/com\.apple\.watchconnectivity(/|$)")

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(subpath "/private/var/tmp")
+		(extension-class "com.apple.identityservices.send")
+	)
+)
 (deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))

 					)
 				)
 			)
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp")

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.ClockKit\.activeComplications|com\.apple\.sockpuppet\.activeComplications)$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 						)
 					)
 				)

 					)
 				)
 			)
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 				(subpath "/private/var/personalized_factory/[^/]+/Applications")
 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Documents")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library")
 			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp")

 						(require-any
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*/carrier\.plist$")
 							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/Carrier Bundles/.*\.png$")
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/(com\.apple\.ClockKit\.activeComplications|com\.apple\.sockpuppet\.activeComplications)$")
+							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/NanoPreferencesSync/NanoDomains/com.apple.nanoprefsyncd$")
 						)
 					)
 				)
```
