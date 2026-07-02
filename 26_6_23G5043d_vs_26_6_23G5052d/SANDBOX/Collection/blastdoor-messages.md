## blastdoor-messages

> Group: ⬆️ Updated

```diff

 
 (allow file-read*
 	(require-all
-		(subpath "${HOME}/Library/SMS")
+		(require-any
+			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
+			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
+		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+		(subpath "${HOME}/Library/SMS")
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 		(extension "com.apple.app-sandbox.read")
 	)
 )
-(allow file-read*
-	(require-all
-		(subpath "/private/var/tmp/com.apple.imtransferagent")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
 (allow file-read*
 	(require-all
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.businessservicesd/temp")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory/LiveCallerID")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
-			(subpath "/private/var/tmp/com.apple.CallKit.CallDirectory/LiveCallerID")
+			(literal "${PROCESS_TEMP_DIR}/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
+			(subpath "${HOME}/Library/Caches/com.apple.businessservicesd/temp${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory/LiveCallerID")
 			(subpath "/private/var/tmp/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
 		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )
+(allow file-read*
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
+		(extension "com.apple.app-sandbox.read")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+		(extension "com.apple.app-sandbox.read")
+	)
+)
 (allow file-read*
 	(require-all
 		(require-any
-			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
-			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+			(subpath "/private/var/tmp/com.apple.imtransferagent")
 		)
 		(extension "com.apple.app-sandbox.read")
 	)
```
