## TVRemoteUI

> `/System/Library/PrivateFrameworks/TVRemoteUI.framework/TVRemoteUI`

```diff

-548.50.7.0.0
-  __TEXT.__text: 0xda2ec
+548.50.8.0.0
+  __TEXT.__text: 0xda320
   __TEXT.__auth_stubs: 0x1b00
   __TEXT.__objc_methlist: 0xb3f8
-  __TEXT.__const: 0x2664
+  __TEXT.__const: 0x2654
   __TEXT.__gcc_except_tab: 0x1da0
   __TEXT.__cstring: 0x4bd5
-  __TEXT.__oslogstring: 0x5a22
+  __TEXT.__oslogstring: 0x5922
   __TEXT.__ustring: 0x4a
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__constg_swiftt: 0x2dcc

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4E3F2722-B8B6-39BA-835C-AB60F9FCEF92
-  Functions: 4708
-  Symbols:   17707
-  CStrings:  7162
+  UUID: F66F72F2-C7E2-3F8D-A620-ABBDA2F31812
+  Functions: 4709
+  Symbols:   17711
+  CStrings:  7164
 
Functions:
+ _OUTLINED_FUNCTION_2
~ -[TVRUIRemoteViewController _presentKeyboardWithAttributes:initialText:] : 996 -> 992
~ ___47-[TVRUIUpNextViewController markItemAsWatched:]_block_invoke.cold.1 : 68 -> 80
~ ___50-[TVRUIUpNextViewController removeItemFromUpNext:]_block_invoke.cold.1 : 68 -> 80
~ ___47-[TVRUIUpNextViewController playItem:animated:]_block_invoke_2.cold.1 : 68 -> 80
CStrings:
+ "%s %@"
+ "Active device did connect name: %{public}@ identifier: %@"
+ "Active device: %@"
+ "Adding connected device: %@"
+ "Adding new uidevice: %@ for core device: %@"
+ "Adding suggested device: %@"
+ "Auto selecting %@"
+ "Cannot find coredevice for device:%@"
+ "Configured RemoteViewController with device-id %@ identifier type %{public}@ device-type %ld launch-context %{public}@"
+ "Configured RemoteViewController with device-id %@ of type %{public}@"
+ "Device list updated: %@"
+ "Error marking %{public}@ as watched: %{public}@"
+ "Error removing %{public}@ from watch list: %{public}@"
+ "Found coreUIDevice:%@ for device:%@"
+ "Found preferred device to connect %@"
+ "Keyboard presentation allowed activeDevice: %@, siriSessionActive: %{bool}d, text: %@, presentedViewController: %@, keyboardController: %@"
+ "Keyboard presentation suppressed activeDevice: %@, siriSessionActive: %{bool}d"
+ "New device list: %@"
+ "No device found for preferred device %@ - deviceList: %@ "
+ "Old device list: %@"
+ "RemoteViewCtrl received callback to end text editing for device %@ text length: %lu"
+ "Requesting connect to device=%@ with connectionContext:%@"
+ "Requesting tvremoted to %@ lock screen assertion for device: %@"
+ "Selecting device: %@ with connectionContext: %{public}@"
+ "Skipping auto select because a device is already active %@"
+ "Sorted device list: %@"
+ "Suggested devices %@"
+ "Toggling control panel controls. active device %@. isConnected %d"
+ "UI Device callback - did connect %@. Now messaging child view controllers"
+ "UI device callback - began connecting %@"
+ "UI requested to disconnect with device: %@ with type %ld"
+ "Updated active device to: %@"
+ "Updating active device to: %@ from: %@"
+ "User picked device: %@"
+ "User tapped on already connected device: %@"
+ "[Autoconnect] Updated active device to: %@"
+ "device - %@ supportsFindMy: %s"
+ "deviceBeganConnecting %@"
+ "deviceConnected %@"
+ "devices: %@"
+ "ui device cancelling auth challenge %@ for device %@"
- "%s %{public}@"
- "Active device did connect name: %{public}@ identifier: %{public}@"
- "Active device: %{public}@"
- "Adding connected device: %{public}@"
- "Adding new uidevice: %{public}@ for core device: %{public}@"
- "Adding suggested device: %{public}@"
- "Auto selecting %{public}@"
- "Cannot find coredevice for device:%{public}@"
- "Configured RemoteViewController with device-id %{public}@ identifier type %{public}@ device-type %ld launch-context %{public}@"
- "Configured RemoteViewController with device-id %{public}@ of type %{public}@"
- "Device list updated: %{public}@"
- "Found coreUIDevice:%{public}@ for device:%{public}@"
- "Found preferred device to connect %{public}@"
- "Keyboard presentation allowed activeDevice: %{public}@, siriSessionActive: %{bool}d, text: %{public}@, presentedViewController: %@, keyboardController: %@"
- "Keyboard presentation suppressed activeDevice: %{public}@, siriSessionActive: %{bool}d"
- "New device list: %{public}@"
- "No device found for preferred device %{public}@ - deviceList: %{public}@ "
- "Old device list: %{public}@"
- "RemoteViewCtrl received callback to end text editing for device %{public}@ text length: %lu"
- "Requesting connect to device=%{public}@ with connectionContext:%@"
- "Requesting tvremoted to %@ lock screen assertion for device: %{public}@"
- "Selecting device: %{public}@ with connectionContext: %{public}@"
- "Skipping auto select because a device is already active %{public}@"
- "Sorted device list: %{public}@"
- "Suggested devices %{public}@"
- "Toggling control panel controls. active device %{public}@. isConnected %d"
- "UI Device callback - did connect %{public}@. Now messaging child view controllers"
- "UI device callback - began connecting %{public}@"
- "UI requested to disconnect with device: %{public}@ with type %ld"
- "Updated active device to: %{public}@"
- "Updating active device to: %{public}@ from: %{public}@"
- "User picked device: %{public}@"
- "User tapped on already connected device: %{public}@"
- "[Autoconnect] Updated active device to: %{public}@"
- "device - %{public}@ supportsFindMy: %s"
- "deviceBeganConnecting %{public}@"
- "deviceConnected %{public}@"
- "devices: %{public}@"
- "ui device cancelling auth challenge %@ for device %{public}@"

```
