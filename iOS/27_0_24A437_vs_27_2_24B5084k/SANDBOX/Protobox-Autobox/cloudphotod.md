## cloudphotod

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		SYS___channel_sync
 		SYS_ulock_wait
 		SYS_ulock_wake
+		SYS_fclonefileat
 		SYS_terminate_with_payload
 		SYS_abort_with_payload
 		SYS_os_fault_with_payload
```
