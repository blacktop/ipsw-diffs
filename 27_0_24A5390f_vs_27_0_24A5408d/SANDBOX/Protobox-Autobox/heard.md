## heard

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.assistant.dictation"))
+		(require-not (global-name "com.apple.sleepd.sleepserver"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist
```
