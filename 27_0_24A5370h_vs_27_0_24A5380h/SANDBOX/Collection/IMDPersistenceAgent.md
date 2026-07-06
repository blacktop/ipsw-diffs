## IMDPersistenceAgent

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/tmp/com.apple.messages")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+			(subpath "/private/var/tmp/com.apple.messages")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/tmp/com.apple.messages")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/tmp/com.apple.messages")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+			(subpath "/private/var/tmp/com.apple.messages")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "/private/var/tmp/com.apple.messages")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+			(subpath "/private/var/tmp/com.apple.messages")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+			(subpath "/private/var/tmp/com.apple.messages")
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
+			(require-any
+				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+				(subpath "/private/var/tmp/com.apple.messages")
+			)
 			(subpath "${HOME}/Library/Caches/PassKit")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
-			(subpath "/private/var/tmp/com.apple.messages")
 		)
 	)
 )

 		SYS_flistxattr
 		SYS_fsctl
 		SYS_shm_open
+		SYS_sysctlbyname
 		SYS_stat_extended
 		SYS_lstat_extended
 		SYS_fstat_extended
```
