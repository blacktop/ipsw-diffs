## eapolclient

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.springboard.blockableservices"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.network.EAPOLController"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.ctkd.token-client"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.inboxupdaterd"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.springboard.blockableservices"))
+		(require-not (global-name "com.apple.network.EAPOLController"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.inboxupdaterd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (xpc-service-name "com.apple.otadaemon"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
```
