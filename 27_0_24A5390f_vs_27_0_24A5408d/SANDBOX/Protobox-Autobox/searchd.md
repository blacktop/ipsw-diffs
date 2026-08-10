## searchd

> Group: ⬆️ Updated

```diff

 
 (deny ipc*)
 
+(deny ipc-posix-sem-open)
+(allow ipc-posix-sem-open
+	(ipc-posix-name "purplebuddy.sentinel")
+)
+
 (deny ipc-posix-shm-read-data)
 (allow ipc-posix-shm-read-data
 	(require-any

 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.spotlight.CSExattrCryptoService"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.OfficeImport.OfficeSpotlightImporter")
 			(xpc-service-name "com.apple.PassKit.PassKitSpotlightIndexExtension")

 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_openbyid_np
+		SYS_thread_selfusage
 		SYS_csrctl
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
```
