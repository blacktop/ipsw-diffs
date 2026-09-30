## com.apple.sandboxd

> Group: ⬆️ Updated

```diff

 	(fsctl-command APFSIOC_SYNC_ROOT_SET_FLAG FSIOC_CAS_BSDFLAGS)
 )
 
+(allow system-info
+	(info-type "vfs.disk-space")
+)
+
 (allow system-kext-query)
 
 (deny system-mac-syscall)
```
