## proactiveeventtrackerd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.proactiveeventtrackerd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.feedbacklogger")
+			(subpath "${HOME}/Library/Caches/com.apple.proactiveeventtrackerd")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.proactiveeventtrackerd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.proactiveeventtrackerd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.feedbacklogger")
+			(subpath "${HOME}/Library/Caches/com.apple.proactiveeventtrackerd")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.proactiveeventtrackerd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.feedbacklogger")
+			(subpath "${HOME}/Library/Caches/com.apple.proactiveeventtrackerd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.feedbacklogger")
+			(subpath "${HOME}/Library/Caches/com.apple.proactiveeventtrackerd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.feedbacklogger")
+				(subpath "${HOME}/Library/Caches/com.apple.proactiveeventtrackerd")
+			)
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.proactiveeventtrackerd")
+		)
 	)
 )
 (allow file-issue-extension

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.feedbacklogger")
-				(subpath "${HOME}/Library/Caches/com.apple.proactiveeventtrackerd")
-			)
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.proactiveeventtrackerd")
-		)
-	)
-)
 (deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 			(require-all
 				(process-attribute is-apple-signed-executable)
 				(require-any
-					(literal "/private/var/preferences/com.apple.networkd.plist")
+					(literal "/private/var/Managed Preferences/mobile/com.apple.SystemConfiguration.plist")
 					(literal "/private/var/preferences/com.apple.networkextension.uuidcache.plist")
 				)
 			)

 )
 (allow sysctl-read
 	(require-all
-		(sysctl-name "net.statistics")
-		(system-attribute internal-build)
-	)
-)
-(allow sysctl-read
-	(require-all
-		(sysctl-name "kern.nisdomainname")
+		(require-any
+			(sysctl-name "kern.nisdomainname")
+			(sysctl-name "net.statistics")
+		)
 		(system-attribute internal-build)
 	)
 )
```
