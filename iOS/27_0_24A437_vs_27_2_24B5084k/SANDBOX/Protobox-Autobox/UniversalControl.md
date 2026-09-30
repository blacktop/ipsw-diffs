## UniversalControl

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.hangtracermonitor"))
 		(require-not (global-name "com.apple.gpumemd.source"))

 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.DragUI.druid.destination"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))

 		SYS_mkdir
 		SYS_rmdir
 		SYS_utimes
+		SYS_gethostuuid
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs
```
