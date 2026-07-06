## com.apple.pdfextensionview

> Group: ⬆️ Updated

```diff

 
 (allow file-issue-extension
 	(require-all
-		(require-not (require-any
-			(literal "/System/Library/Caches/apticket.der")
-			(subpath "/System/Library/Caches/com.apple.factorydata")
-			(subpath "/System/Library/Caches/com.apple.kernelcaches")
-		))
 		(extension-class "com.apple.app-sandbox.read")
 		(require-any
 			(subpath "/System/Cryptexes")

 		)
 	)
 )
+(deny file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(require-any
+			(subpath "/System/Cryptexes")
+			(subpath "/private/preboot/Cryptexes")
+		)
+		(require-any
+			(literal "/System/Library/Caches/apticket.der")
+			(subpath "/System/Library/Caches/com.apple.factorydata")
+			(subpath "/System/Library/Caches/com.apple.kernelcaches")
+		)
+	)
+)
 
 (deny file-link)
 

 	(require-any
 		(subpath "/System/Cryptexes")
 		(subpath "/System/Library")
-		(subpath "/System/Library/Frameworks")
 		(subpath "/System/Library/PrivateFrameworks")
 		(subpath "/private/preboot/Cryptexes")
 		(subpath "/usr/lib")

 			(subpath "/System/Library/Caches/com.apple.kernelcaches")
 		))
 		(require-any
-			(literal "/dev/null")
 			(literal "/dev/random")
 			(literal "/dev/urandom")
-			(literal "/dev/zero")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
+					(require-any
+						(literal "/private/etc/group")
+						(literal "/private/etc/protocols")
+					)
 					(subpath "/System")
-					(subpath "/private/preboot/Cryptexes")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")
 					(subpath "/usr/share")

 					)
 				)
 			)
+			(require-any
+				(literal "/dev/null")
+				(literal "/dev/zero")
+			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 				(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 				(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 			)
+			(require-any
+				(subpath "/System/Cryptexes")
+				(subpath "/private/preboot/Cryptexes")
+			)
 			(subpath "/")
-			(subpath "/System/Cryptexes")
-			(subpath "/private/preboot/Cryptexes")
 		)
 	)
 )

 			(subpath "/System/Library/Caches/com.apple.kernelcaches")
 		))
 		(require-any
-			(literal "/dev/null")
 			(literal "/dev/random")
 			(literal "/dev/urandom")
-			(literal "/dev/zero")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
+					(require-any
+						(literal "/private/etc/group")
+						(literal "/private/etc/protocols")
+					)
 					(subpath "/System")
-					(subpath "/private/preboot/Cryptexes")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")
 					(subpath "/usr/share")

 					)
 				)
 			)
+			(require-any
+				(literal "/dev/null")
+				(literal "/dev/zero")
+			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 				(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 				(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 			)
+			(require-any
+				(subpath "/System/Cryptexes")
+				(subpath "/private/preboot/Cryptexes")
+			)
 			(subpath "/")
-			(subpath "/System/Cryptexes")
-			(subpath "/private/preboot/Cryptexes")
 		)
 	)
 )

 			(subpath "/System/Library/Caches/com.apple.kernelcaches")
 		))
 		(require-any
-			(literal "/dev/null")
 			(literal "/dev/random")
 			(literal "/dev/urandom")
-			(literal "/dev/zero")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
+					(require-any
+						(literal "/private/etc/group")
+						(literal "/private/etc/protocols")
+					)
 					(subpath "/System")
-					(subpath "/private/preboot/Cryptexes")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")
 					(subpath "/usr/share")

 					)
 				)
 			)
+			(require-any
+				(literal "/dev/null")
+				(literal "/dev/zero")
+			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 				(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
 				(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
 			)
+			(require-any
+				(subpath "/System/Cryptexes")
+				(subpath "/private/preboot/Cryptexes")
+			)
 			(subpath "/")
-			(subpath "/System/Cryptexes")
-			(subpath "/private/preboot/Cryptexes")
 		)
 	)
 )

 		(require-not (subpath "/AppleInternal"))
 		(require-any
 			(literal "/dev")
+			(literal "/private/etc/passwd")
 			(require-any
 				(literal "/etc/passwd")
 				(subpath "/private")

 	)
 )
 
+(allow file-write-data
+	(require-any
+		(literal "/dev/null")
+		(literal "/dev/zero")
+	)
+)
 (allow file-write-data
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
-(allow file-write-data
-	(require-any
-		(literal "/dev/null")
-		(literal "/dev/zero")
-	)
-)
 
 (allow fs-info)
 

 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-property "product-id")
+		(iokit-property "display-corner-radius")
+		(iokit-registry-entry-class "IOPlatformDevice")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(require-any
+			(iokit-property "large-format-phone")
+			(iokit-property "thin-bezel")
+		)
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )

 )
 (allow iokit-get-properties
 	(require-all
-		(require-any
-			(iokit-property "compatible-app-variant")
-			(iokit-property "external-hdr")
-		)
+		(iokit-property "device-colors")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
 (allow iokit-get-properties
 	(require-all
-		(iokit-property "device-colors")
+		(iokit-property "product-id")
+		(iokit-registry-entry-class "IOPlatformDevice")
+	)
+)
+(allow iokit-get-properties
+	(require-all
+		(require-any
+			(iokit-property "compatible-app-variant")
+			(iokit-property "external-hdr")
+		)
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )

 			(iokit-property "artwork-device-subtype")
 			(iokit-property "artwork-display-gamut")
 			(iokit-property "artwork-dynamic-displaymode")
+			(iokit-property "artwork-scale-factor")
 			(iokit-property "compatible-device-fallback")
 			(iokit-property "device-perf-memory-class")
 			(iokit-property "graphics-featureset-class")

 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
-	(require-all
-		(require-any
-			(iokit-property "large-format-phone")
-			(iokit-property "thin-bezel")
-		)
-		(iokit-registry-entry-class "IOPlatformDevice")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "artwork-scale-factor")
-		(iokit-registry-entry-class "IOPlatformDevice")
-	)
-)
-(allow iokit-get-properties
-	(require-all
-		(iokit-property "display-corner-radius")
-		(iokit-registry-entry-class "IOPlatformDevice")
-	)
-)
 
 (allow iokit-open-user-client
 	(require-all
```
