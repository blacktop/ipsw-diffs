## mobileassetd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mobileassetd")
-			(subpath "/private/var/tmp/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${HOME}/Library/Caches/mobileassetd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
 		)
 	)
 )

 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mobileassetd")
-			(subpath "/private/var/tmp/com.apple.mobileassetd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mobileassetd")
-			(subpath "/private/var/tmp/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${HOME}/Library/Caches/mobileassetd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
 		)
 	)
 )

 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mobileassetd")
-			(subpath "/private/var/tmp/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${HOME}/Library/Caches/mobileassetd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
+			(subpath "${HOME}/Library/Caches/com.apple.mobileassetd")
+			(subpath "${HOME}/Library/Caches/mobileassetd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-any
-				(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
+				(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
 				(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
 				(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
 				(subpath "${HOME}/Library/Caches/com.apple.mobileassetd")

 		(literal "/private/var/root/Library/Preferences/com.apple.WebFoundation.plist")
 		(literal "/private/var/run/com.apple.mobileassetd-MobileAssetBrain")
 		(subpath "${FRONT_USER_HOME}/Library/Assets")
-		(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
+		(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/VoiceServices/Assets")

 		(literal "/private/var/root/Library/Preferences/com.apple.MobileAsset.plist*")
 		(literal "/private/var/run/com.apple.mobileassetd-MobileAssetBrain")
 		(subpath "${FRONT_USER_HOME}/Library/Assets")
-		(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
+		(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/VoiceServices/Assets")

 		(literal "/private/var/root/Library/Preferences/com.apple.MobileAsset.plist*")
 		(literal "/private/var/run/com.apple.mobileassetd-MobileAssetBrain")
 		(subpath "${FRONT_USER_HOME}/Library/Assets")
-		(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
+		(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/VoiceServices/Assets")

 		(literal "/private/var/root/Library/Preferences/com.apple.MobileAsset.plist*")
 		(literal "/private/var/run/com.apple.mobileassetd-MobileAssetBrain")
 		(subpath "${FRONT_USER_HOME}/Library/Assets")
-		(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/HTTPStorages/com.apple.mobileassetd")
+		(subpath "${FRONT_USER_HOME}/Library/Caches/${HOME}/Library/Caches/com.apple.mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/Caches/mobileassetd")
 		(subpath "${FRONT_USER_HOME}/Library/VoiceServices/Assets")
```
