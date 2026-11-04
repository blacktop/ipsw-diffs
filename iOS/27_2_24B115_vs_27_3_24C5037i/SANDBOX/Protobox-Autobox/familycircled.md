## familycircled

> Group: ⬆️ Updated

```diff

 
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
 	)
 )
 (deny system-mac-syscall
```
