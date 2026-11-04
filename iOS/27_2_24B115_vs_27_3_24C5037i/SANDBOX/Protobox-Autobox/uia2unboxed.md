## uia2unboxed

> Group: ⬆️ Updated

```diff

 				(require-not (require-any
 					(literal "/usr/local/bin/collectWiFiDebugInfo.sh")
 					(literal "/usr/local/bin/eventer")
-				))
-				(require-not (require-any
 					(literal "/usr/local/bin/gestalt_query")
 					(literal "/usr/local/bin/hkctl")
 				))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
