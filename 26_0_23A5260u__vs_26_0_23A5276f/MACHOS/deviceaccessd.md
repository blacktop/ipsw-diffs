## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-320.33.1.4.0
-  __TEXT.__text: 0x31d84
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_stubs: 0x4880
-  __TEXT.__objc_methlist: 0x1978
+320.36.0.0.0
+  __TEXT.__text: 0x32194
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_stubs: 0x4980
+  __TEXT.__objc_methlist: 0x19d8
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0x1da4
-  __TEXT.__objc_methname: 0x6335
+  __TEXT.__gcc_except_tab: 0x1db0
+  __TEXT.__objc_methname: 0x657f
   __TEXT.__objc_classname: 0x1ff
-  __TEXT.__objc_methtype: 0x147f
-  __TEXT.__cstring: 0xb538
-  __TEXT.__unwind_info: 0xa88
-  __DATA_CONST.__auth_got: 0x718
+  __TEXT.__objc_methtype: 0x14bc
+  __TEXT.__cstring: 0xb775
+  __TEXT.__unwind_info: 0xa58
+  __DATA_CONST.__auth_got: 0x710
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0xed0
+  __DATA_CONST.__const: 0xe58
   __DATA_CONST.__cfstring: 0x1000
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA.__objc_const: 0x22d0
-  __DATA.__objc_selrefs: 0x17c8
+  __DATA.__objc_selrefs: 0x1830
   __DATA.__objc_ivar: 0x22c
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x6e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB085A16-A03A-30CC-BDEB-2C4C9928C8F1
-  Functions: 915
-  Symbols:   342
-  CStrings:  2427
+  UUID: 6A61BAA1-5EDA-36CF-A716-7B885236FF33
+  Functions: 922
+  Symbols:   341
+  CStrings:  2452
 
Symbols:
- _dispatch_group_wait
CStrings:
+ "-[DADaemonServer _authorizeWiFiAwareDeviceFor:pairingKeyStoreID:device:error:]"
+ "-[DADaemonServer _deauthorizeWiFiAwareDeviceFor:withAppPairingID:]"
+ "-[DADaemonServer _persistWiFiAwareDevice:device:pairingID:bundleID:]_block_invoke_2"
+ "-[DADaemonServer _persistWiFiAwareDevice:device:pairingID:bundleID:]_block_invoke_4"
+ "-[DADaemonServer _reauthorizeWiFiAwareDeviceFor:withAppPairingID:]"
+ "-[DADaemonServer _uninstallWiFiAwareDeviceFor:appPairingID:]"
+ "-[DADaemonServer _updateWiFiAwareDeviceNameFor:appPairingID:newName:]"
+ "-[DAWiFiScanner authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:error:]"
+ "-[DAWiFiScanner authorizePairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:completionHandler:]"
+ "-[DAWiFiScanner deauthorizePairedDeviceFor:withAppPairingID:]"
+ "-[DAWiFiScanner reauthorizePairedDeviceFor:withAppPairingID:]"
+ "-[DAWiFiScanner reauthorizePairedDeviceFor:withAppPairingID:completionHandler:]"
+ "-[DAWiFiScanner uninstallPairedDeviceFor:withAppPairingID:]"
+ "-[DAWiFiScanner updatePairedDeviceNameFor:withAppPairingID:toNewName:]"
+ "@32@0:8@16Q24"
+ "@40@0:8@16Q24@32"
+ "Failed to authorize wi-fi aware device %@ for app %@, Error=%@"
+ "Failed to de-authorize Wi-Fi Aware device %@, deviceID =%@ for app %@, Error=%@"
+ "Failed to re-authorize wi-fi aware device %@ for app %@, Error=%@"
+ "Found existing device record, but it's not authorized to be upgraded. %@"
+ "No keyStoreID"
+ "Q48@0:8@16@24@32^@40"
+ "Q64@0:8@16@24q32d40q48^@56"
+ "[WiFi] Session keyStoreID is INVALID"
+ "[WiFi] _deauthorizeWiFiAwareDeviceFor bundleID='%@' with ID='%llu'"
+ "[WiFi] authorizing WiFi aware device with  devicePairingID='%@' and bundleID = '%@'"
+ "[WiFi] device signature match"
+ "[WiFi] device superID match"
+ "_authorizeWiFiAwareDeviceFor:pairingKeyStoreID:device:error:"
+ "_deauthorizeWiFiAwareDeviceFor:withAppPairingID:"
+ "_reauthorizeWiFiAwareDeviceFor:withAppPairingID:"
+ "_uninstallWiFiAwareDeviceFor:appPairingID:"
+ "_updateWiFiAwareDeviceNameFor:appPairingID:newName:"
+ "authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:error:"
+ "deauthorizePairedDeviceFor:withAppPairingID:"
+ "reauthorizePairedDeviceFor:withAppPairingID:"
+ "reauthorizePairedDeviceFor:withAppPairingID:completionHandler:"
+ "reauthorizePairedDeviceFor:withDeviceID:"
+ "removePairedDeviceFor:withDeviceID:"
+ "stillTrackableWhenUnpaired"
+ "uninstallPairedDeviceFor:withAppPairingID:"
+ "uninstallPairedDeviceFor:withDeviceID:"
+ "updatePairedDeviceNameFor:withAppPairingID:toNewName:"
+ "updatePairedDeviceNameFor:withDeviceID:toNewName:"
- "-[DADaemonServer _addWiFiAwareDeviceFor:withDevicePairingID:completionHandler:]"
- "-[DADaemonServer _persistWiFiAwareDevice:device:pairingID:bundleID:]_block_invoke_3"
- "-[DAWiFiScanner addPairedDeviceFor:withDevicePairingID:completionHandler:]"
- "-[DAWiFiScanner reauthorizePairedDeviceFor:withDeviceID:completionHandler:]"
- "Failed to authorize wi-fi aware device %@ for app %@, TimedOut=%s, Error=%@"
- "Failed to de-authorize Wi-Fi Aware device %@, deviceID =%@ for app %@, TimedOut=%s, Error=%@"
- "Failed to re-authorize wi-fi aware device %@ for app %@, TimedOut=%s, Error=%@"
- "No Device ID"
- "[WiFi] Added device for bundleID=%@ devicePairingID='%@'"
- "[WiFi] Failed to add Wi-Fi Aware device '%@'. TimedOut=%s, Error=%@, devicePairingID=%@, for bundleID=%@"
- "[WiFi] Session device ID is INVALID"
- "[WiFi] _saveDeviceAppAccessInfo: ADD wi-fi aware device for bundleID='%@', deviceName='%@'"
- "[WiFi] addWiFiAwareDevice wifiScanner='%@' for bundleID=%@, deviceUUID='%@'"
- "[WiFi] forgetWiFiAwareDevice wifiScanner='%@' with ID='%llu'"
- "_addWiFiAwareDeviceFor:withDevicePairingID:completionHandler:"
- "addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:"
- "addPairedDeviceFor:withDevicePairingID:completionHandler:"
- "v24@?0Q8@\"NSError\"16"
- "v40@0:8@16@24@?32"

```
