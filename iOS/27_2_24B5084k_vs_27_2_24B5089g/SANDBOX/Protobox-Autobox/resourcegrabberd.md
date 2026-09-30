## resourcegrabberd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
```
