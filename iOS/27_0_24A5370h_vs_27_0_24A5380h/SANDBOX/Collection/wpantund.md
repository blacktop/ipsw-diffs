## wpantund

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/CoreThread")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.threadradiod")
+			(subpath "/private/var/tmp/com.apple.threadradiod")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/CoreThread")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/CoreThread")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.threadradiod")
+			(subpath "/private/var/tmp/com.apple.threadradiod")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter/CoreThread")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.threadradiod")
+			(subpath "/private/var/tmp/com.apple.threadradiod")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.threadradiod")
+			(subpath "/private/var/tmp/com.apple.threadradiod")
+		)
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-any
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.threadradiod")
```
