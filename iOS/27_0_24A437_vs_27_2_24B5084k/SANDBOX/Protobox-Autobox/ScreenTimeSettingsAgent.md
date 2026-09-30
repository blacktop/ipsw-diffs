## ScreenTimeSettingsAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.cksharingmanagementd"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
```
