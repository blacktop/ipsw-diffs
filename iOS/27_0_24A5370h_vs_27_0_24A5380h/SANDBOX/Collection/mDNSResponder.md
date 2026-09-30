## mDNSResponder

> Group: ⬆️ Updated

```diff

 
 (allow file-ungraft)
 
+(allow file-write*
+	(require-all
+		(subpath "/cores")
+		(require-not (file-mode #o0000))
+	)
+)
 (allow file-write*
 	(require-all
 		(subpath "/private/var/db/mds")

 		(literal "/private/var/tmp/mDNSResponder")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.mDNSResponder")
 		(subpath "/Library/Caches/com.apple.mDNSResponder")
-		(subpath "/cores")
 		(subpath "/private/var/folders/[^/]+/[^/]+/-Caches-/mds")
 		(subpath "/private/var/folders/[^/]+/[^/]+/C/mds")
 		(subpath "/private/var/log/mDNSResponder")

 	)
 )
 
+(allow file-write-data
+	(require-all
+		(subpath "/cores")
+		(require-not (file-mode #o0000))
+	)
+)
 (allow file-write-data
 	(require-all
 		(subpath "/private/var/db/mds")

 		(literal "/private/var/tmp/mDNSResponder")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.mDNSResponder")
 		(subpath "/Library/Caches/com.apple.mDNSResponder")
-		(subpath "/cores")
 		(subpath "/private/var/folders/[^/]+/[^/]+/-Caches-/mds")
 		(subpath "/private/var/folders/[^/]+/[^/]+/C/mds")
 		(subpath "/private/var/log/mDNSResponder")

 		(subpath "/private/var/OOPJit")
 	)
 )
+(allow file-write-unlink
+	(require-all
+		(subpath "/cores")
+		(require-not (file-mode #o0000))
+	)
+)
 (allow file-write-unlink
 	(require-all
 		(subpath "/private/var/db/mds")

 		(literal "/private/var/tmp/mDNSResponder")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.mDNSResponder")
 		(subpath "/Library/Caches/com.apple.mDNSResponder")
-		(subpath "/cores")
 		(subpath "/private/var/folders/[^/]+/[^/]+/-Caches-/mds")
 		(subpath "/private/var/folders/[^/]+/[^/]+/C/mds")
 		(subpath "/private/var/log/mDNSResponder")
```
