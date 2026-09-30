## wifianalyticsd

> Group: ⬆️ Updated

```diff

 
 (allow file-ungraft)
 
+(allow file-write*
+	(require-any
+		(subpath "${HOME}/Library/Application Support/com.apple.wifianalyticsd")
+		(subpath "${HOME}/Library/com.apple.wifi.analytics")
+		(subpath "${HOME}/Library/com.apple.wifianalyticsd")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.wifianalyticsd")
+		(subpath "/private/var/tmp/com.apple.wifianalyticsd")
+	)
+)
 (allow file-write*
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
-(allow file-write*
+(deny file-write*
+	(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
+)
+
+(allow file-write-create
 	(require-any
 		(subpath "${HOME}/Library/Application Support/com.apple.wifianalyticsd")
 		(subpath "${HOME}/Library/com.apple.wifi.analytics")

 		(subpath "/private/var/tmp/com.apple.wifianalyticsd")
 	)
 )
-(deny file-write*
-	(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
-)
-
 (allow file-write-create
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
-(allow file-write-create
-	(require-any
-		(subpath "${HOME}/Library/Application Support/com.apple.wifianalyticsd")
-		(subpath "${HOME}/Library/com.apple.wifi.analytics")
-		(subpath "${HOME}/Library/com.apple.wifianalyticsd")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.wifianalyticsd")
-		(subpath "/private/var/tmp/com.apple.wifianalyticsd")
-	)
-)
 (deny file-write-create
 	(with no-report)
 	(literal "${HOME}/Library/Logs/CrashReporter/CFNetwork_*")

 		(subpath "/private/var/OOPJit")
 	)
 )
+(allow file-write-unlink
+	(require-any
+		(subpath "${HOME}/Library/Application Support/com.apple.wifianalyticsd")
+		(subpath "${HOME}/Library/com.apple.wifi.analytics")
+		(subpath "${HOME}/Library/com.apple.wifianalyticsd")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.wifianalyticsd")
+		(subpath "/private/var/tmp/com.apple.wifianalyticsd")
+	)
+)
 (allow file-write-unlink
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
-(allow file-write-unlink
-	(require-any
-		(subpath "${HOME}/Library/Application Support/com.apple.wifianalyticsd")
-		(subpath "${HOME}/Library/com.apple.wifi.analytics")
-		(subpath "${HOME}/Library/com.apple.wifianalyticsd")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.wifianalyticsd")
-		(subpath "/private/var/tmp/com.apple.wifianalyticsd")
-	)
-)
 (deny file-write-unlink
 	(literal "${ANY_USER_HOME}/Library/Caches/GeoServices/tguid.bin")
 )
```
