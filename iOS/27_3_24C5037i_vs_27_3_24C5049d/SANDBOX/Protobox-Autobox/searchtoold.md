## searchtoold

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.assistant.settings"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))

 		SYS_seteuid
 		SYS_sigreturn
 		SYS_pathconf
+		SYS_fpathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap
```
