## wifid

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.triald.namespace-management"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))

 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.triald.namespace-management"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
```
