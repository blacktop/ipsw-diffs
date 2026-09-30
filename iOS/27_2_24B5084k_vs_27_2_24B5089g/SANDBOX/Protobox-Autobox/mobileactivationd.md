## mobileactivationd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.absd"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.mobilestoredemodhelper"))

 		(require-not (global-name "com.apple.eligibilityd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.CellularPlanDaemon.xpc"))
+		(require-not (global-name "com.apple.absinthed"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.runningboard"))
```
