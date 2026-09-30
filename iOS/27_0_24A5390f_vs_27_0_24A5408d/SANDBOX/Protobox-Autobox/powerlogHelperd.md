## powerlogHelperd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.backlightd"))
 		(require-not (global-name "com.apple.powerd.extendedbattery"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.server.bluetooth.general.xpc"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.powerui.smartChargeManager"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))

 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.centaurid.xpc"))
 		(require-not (global-name "com.apple.trial.status"))
 		(require-not (global-name "com.apple.PowerManagement.control"))

 		(require-not (global-name "com.apple.backupd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.featureaccessd"))
+		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.wifip2pd"))

 		(require-not (xpc-service-name "com.apple.PPSFeatureFlagReader"))
 		(require-not (xpc-service-name "com.apple.PerfPowerServicesSignpostReader"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryReaderService"))
-		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.FSEvents"))
-		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.AttentionAwareness"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
