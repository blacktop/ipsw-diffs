## CallAudioService

> Group: ⬆️ Updated

```diff

 (with-filter (mac-policy-name "AMFI")
 	(deny system-mac-syscall
 		(require-all
-			(require-not (mac-syscall-number 90))
 			(require-not (mac-syscall-number 96))
+			(require-not (mac-syscall-number 90))
 			(require-not (mac-syscall-number 102))
 		)
 	)
```
