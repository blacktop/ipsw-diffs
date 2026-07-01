# blastdoor-airlock

Group: Updated

```diff

 		(extension "com.apple.app-sandbox.read")
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
 (allow file-read*
 	(require-all
 		(subpath "${HOME}/Library/SMS")

 )
 (allow file-read*
 	(require-all
-		(require-any
-			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
-			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
-		)
+		(subpath "/private/var/tmp/com.apple.TelephonyUtilities/SharePlayActivityImages")
 		(extension "com.apple.app-sandbox.read")
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var/tmp/com.apple.imtransferagent")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
+		(extension "com.apple.app-sandbox.read")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.MobileSMS")
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var/tmp/com.apple.TelephonyUtilities/SharePlayActivityImages")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+			(subpath "/private/var/tmp/com.apple.imtransferagent")
+		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 		(extension "com.apple.app-sandbox.read")
 	)
 )
+(allow file-read*
+	(require-all
+		(require-any
+			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
+			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
+		)
+		(extension "com.apple.app-sandbox.read")
+	)
+)
 (allow file-read*
 	(require-all
 		(system-attribute internal-build)

 				(require-any
 					(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
 					(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
-					(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
 				)
 				(extension "com.apple.app-sandbox.read")
 			)

 				)
 				(extension "com.apple.app-sandbox.read")
 			)
+			(require-all
+				(require-any
+					(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+					(subpath "/private/var/tmp/com.apple.imtransferagent")
+				)
+				(extension "com.apple.app-sandbox.read")
+			)
 			(require-all
 				(require-not (literal "/private/var"))
 				(require-not (require-any

 				(extension "com.apple.app-sandbox.read")
 			)
 			(require-all
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+				(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
 				(extension "com.apple.app-sandbox.read")
 			)
 			(require-all

 				(subpath "/private/var/tmp/com.apple.TelephonyUtilities/SharePlayActivityImages")
 				(extension "com.apple.app-sandbox.read")
 			)
-			(require-all
-				(subpath "/private/var/tmp/com.apple.imtransferagent")
-				(extension "com.apple.app-sandbox.read")
-			)
 			(require-all
 				(subpath "/private/var/tmp/com.apple.messages")
 				(extension "com.apple.app-sandbox.read")
```
