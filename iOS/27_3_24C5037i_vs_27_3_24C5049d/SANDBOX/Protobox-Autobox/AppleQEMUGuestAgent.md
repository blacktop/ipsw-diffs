## AppleQEMUGuestAgent

> Group: ⬆️ Updated

```diff

 	)
 )
 
-(deny process-exec*
-	(process-attribute is-autoboxed)
+(allow process-exec*
+	(with no-sandbox)
+	(require-not (process-attribute is-autoboxed))
 )
 
 (deny socket-ioctl)
```
