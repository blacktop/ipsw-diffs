## deviceconfigurationd

> Group: ⬆️ Updated

```diff

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "AMFI")
+(with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
-			(require-not (mac-syscall-number 90))
-			(require-not (mac-syscall-number 96))
-			(require-not (mac-syscall-number 102))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
 		)
 	)
 )
 (deny system-mac-syscall
 	(require-any
-		(require-not (mac-policy-name "Sandbox"))
-		(require-not (mac-syscall-number 2))
+		(require-not (mac-policy-name "AMFI"))
+		(require-not (mac-syscall-number 90))
 	)
 )
 
```
