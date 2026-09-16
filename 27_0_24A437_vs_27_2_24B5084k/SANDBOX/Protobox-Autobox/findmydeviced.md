## findmydeviced

> Group: ⬆️ Updated

```diff

 (deny iokit-open-service)
 (allow iokit-open-service
 	(require-any
+		(iokit-registry-entry-class "AppleCredentialManager")
 		(iokit-registry-entry-class "IOHIDUserDevice")
 		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKit")
 	)

 			(global-name "com.apple.findmy.findmylocate.friendshipservice")
 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.icloud.searchpartyd.beaconmanager.simplebeacon"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
```
