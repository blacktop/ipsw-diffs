## inboxupdaterd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (require-any
+			(global-name "com.apple.diagnostics.launcher-service")
+			(global-name "com.apple.diagnosticscheckupd")
+		))
 		(require-not (global-name "com.apple.private.corewifi-xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.bluetooth.xpc"))

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
-		(require-not (global-name "com.apple.diagnostics.launcher-service"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.MIBUFileServerHelper")
+			(xpc-service-name "com.apple.MIBULoopbackServerHelper")
+		))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.springboard.blockableservices"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (require-any
-			(xpc-service-name "com.apple.MIBUFileServerHelper")
-			(xpc-service-name "com.apple.MIBULoopbackServerHelper")
-		))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))

 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_SINGLE_WRITER
+		F_BARRIERFSYNC
 		F_OFD_SETLK
 		F_OFD_GETLK
 		F_OFD_SETLKWTIMEOUT
```
