## apsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.momentsd"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.facetimemessagestored.service"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.safetyalerts"))
+		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.jetpackassetd.xpc"))
+		(require-not (global-name "com.apple.diagd"))
 		(require-not (require-any
 			(global-name "${ANY_UUID}")
 			(global-name "DeviceSpecificTopic1")

 			(global-name "com.apple.carrierutilitiesd")
 			(global-name "com.apple.carrierutilitiesd.aps")
 			(global-name "com.apple.cloudpaird.aps")
+			(global-name "com.apple.communicationtrustd.aps")
 			(global-name "com.apple.companiond")
 			(global-name "com.apple.contacts.postersyncd.aps")
 			(global-name "com.apple.coredata.test")

 			(global-name "com.apple.wte.aesd")
 			(global-name "dummy.delegate.port")
 		))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.facetimemessagestored.service"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.safetyalerts"))
-		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
-		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.jetpackassetd.xpc"))
-		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
```
