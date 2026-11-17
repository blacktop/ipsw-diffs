## FamilyControlsAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.ManagedSettingsAgent"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cloudkit.partlycloudd"))

 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
```
