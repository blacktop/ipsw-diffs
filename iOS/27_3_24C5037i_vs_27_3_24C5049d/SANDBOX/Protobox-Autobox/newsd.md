## newsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.lsd.icons"))
-		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
 		(require-not (global-name "com.apple.adid.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))

 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.adid"))

 		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
-		(require-not (global-name "com.apple.FSEvents"))
+		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.GSSCred"))
 		(require-not (global-name "com.apple.logd.events"))

 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.coremedia.figcpecryptor"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
+		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
+		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))

 		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
