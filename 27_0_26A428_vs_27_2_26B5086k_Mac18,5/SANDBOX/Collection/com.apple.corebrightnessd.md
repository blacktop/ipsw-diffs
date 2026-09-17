## com.apple.corebrightnessd

> Group: ⬆️ Updated

```diff

 	(fsctl-command FSIOC_CAS_BSDFLAGS)
 )
 
+(allow system-info
+	(info-type "vfs.disk-space")
+)
+
 (allow user-preference-read
 	(require-any
 		(preference-domain "com.apple.corebrightness")
```
