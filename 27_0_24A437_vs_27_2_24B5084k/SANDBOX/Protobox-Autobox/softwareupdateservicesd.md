## softwareupdateservicesd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.powerd.coresmartpowernap"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))

 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.remoted"))
+		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (require-any
```
