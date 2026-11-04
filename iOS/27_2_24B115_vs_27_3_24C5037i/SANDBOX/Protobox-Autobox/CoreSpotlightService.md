## CoreSpotlightService

> Group: ⬆️ Updated

```diff

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_PREALLOCATE

 
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
