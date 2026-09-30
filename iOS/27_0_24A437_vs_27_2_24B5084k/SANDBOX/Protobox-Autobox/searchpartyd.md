## searchpartyd

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.findmy.findmylocate.friendshipservice")
 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.bluetooth.xpc"))
```
