## secure-capture-extension

> Group: ⬆️ Updated

```diff

 			(extension "com.apple.security.exception.files.absolute-path.read-write")
 			(extension "com.apple.security.exception.files.home-relative-path.read-only")
 			(extension "com.apple.security.exception.files.home-relative-path.read-write")
-			(require-all
-				(extension "com.apple.assets.read")
-				(require-any
-					(subpath "${HOME}/Library/Assets")
-					(subpath "/private/var/MobileAsset")
-				)
-			)
 		)
 	)
 )

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension "com.apple.assets.read")
+		(require-any
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(require-any
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
+			(require-all
+				(extension-class "com.apple.mediaserverd.read")
+				(subpath "/private/var/MobileAsset")
+			)
+		)
+	)
+)
 
 (allow file-link)
 (deny file-link

 		)
 	)
 )
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "IOSurfaceAcceleratorCapabilitiesDict")
-		(iokit-registry-entry-class "IOService")
-	)
-)
 (allow iokit-get-properties
 	(require-all
 		(iokit-registry-entry-class "AppleJPEGDriver")

 		)
 	)
 )
+(allow iokit-get-properties
+	(require-all
+		(iokit-property "IOSurfaceAcceleratorCapabilitiesDict")
+		(iokit-registry-entry-class "IOService")
+	)
+)
 (allow iokit-get-properties
 	(require-all
 		(iokit-registry-entry-class "IOAcceleratorES")

 		(preference-domain "com.apple.MobileAsset")
 		(preference-domain "com.apple.NanoRegistry")
 		(preference-domain "com.apple.UIKit")
+		(preference-domain "com.apple.assistant.public")
 		(preference-domain "com.apple.assistant.support")
 		(preference-domain "com.apple.avfoundation")
 		(preference-domain "com.apple.carrier")

 		(preference-domain "com.apple.MobileAsset")
 		(preference-domain "com.apple.NanoRegistry")
 		(preference-domain "com.apple.UIKit")
+		(preference-domain "com.apple.assistant.public")
 		(preference-domain "com.apple.assistant.support")
 		(preference-domain "com.apple.avfoundation")
 		(preference-domain "com.apple.carrier")
```
