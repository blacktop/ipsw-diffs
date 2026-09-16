## accessoryupdaterd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.accessories.transport-server"))
 		(require-not (global-name "com.apple.erm.logging"))

 		SYS_preadv_nocancel
 		SYS_pwritev_nocancel
 		SYS_ulock_wait2
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)
 )
 
```
