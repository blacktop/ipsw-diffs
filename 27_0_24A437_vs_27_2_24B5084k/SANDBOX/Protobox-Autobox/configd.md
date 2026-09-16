## configd

> Group: ⬆️ Updated

```diff

 
 (allow default)
 
+(deny asr-parser-enter
+	(require-any
+		(require-not (asr-parser-domain ASR_DOMAIN_IMAGES))
+		(require-not (asr-parser-name "com.apple.imageio.png"))
+	)
+)
+
 (deny file-ioctl)
 (allow file-ioctl
 	(ioctl-command
```
