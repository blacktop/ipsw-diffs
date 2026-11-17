## InteractiveLegacyProfilesSubscriber

> Group: ⬆️ Updated

```diff

 	(deny system-mac-syscall
 		(require-all
 			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
 		)
```
