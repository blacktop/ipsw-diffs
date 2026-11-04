## networkdiagnosticsd

> Group: ⬆️ Updated

```diff

 				(require-not (literal "/usr/bin/log"))
 				(require-not (literal "/usr/bin/awk"))
 				(require-not (literal "/bin/sh"))
-				(require-not (literal "/System/Library/PrivateFrameworks/SystemConfiguration.framework/get-network-info"))
-				(require-not (literal "/usr/bin/defaults"))
+				(require-not (require-any
+					(literal "/System/Library/PrivateFrameworks/SystemConfiguration.framework/get-network-info")
+					(literal "/usr/bin/defaults")
+				))
 			)
 		)
 	)

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
