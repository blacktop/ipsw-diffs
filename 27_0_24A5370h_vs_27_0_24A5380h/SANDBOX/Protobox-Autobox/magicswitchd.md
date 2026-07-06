## magicswitchd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.server.bluetooth.le.pipe.xpc"))
-		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.wirelessproxd"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.pairedsyncd.syncstate"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.tailspind"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.pairedsyncd.syncstate"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.wirelessproxd"))
+		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.server.bluetooth.le.pipe.xpc"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FileCoordination"))
```
