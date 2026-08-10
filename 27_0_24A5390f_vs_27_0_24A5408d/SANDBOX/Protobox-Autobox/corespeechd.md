## corespeechd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.siri.speakerprofile.embedding.service.xpc"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.coremedia.carplayavvc.xpc"))

 		MSC_task_self_trap
 		MSC_host_self_trap
 		MSC_semaphore_signal_trap
+		MSC_semaphore_signal_all_trap
 		MSC_semaphore_wait_trap
 		MSC_semaphore_timedwait_trap
 		MSC_semaphore_timedwait_signal_trap
```
