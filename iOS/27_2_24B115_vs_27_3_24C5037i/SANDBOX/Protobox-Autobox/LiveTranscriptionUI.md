## LiveTranscriptionUI

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.usymptomsd"))

 		SYS_munlock
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_fsetattrlist

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_guarded_open_dprotected_np
 		SYS_persona
 		SYS_work_interval_ctl
 		SYS_getentropy

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
