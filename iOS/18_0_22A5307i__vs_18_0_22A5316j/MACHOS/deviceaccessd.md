## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-304.23.1.0.0
-  __TEXT.__text: 0x2272c
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_stubs: 0x33e0
-  __TEXT.__objc_methlist: 0xce8
+304.24.2.1.0
+  __TEXT.__text: 0x23318
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_stubs: 0x35c0
+  __TEXT.__objc_methlist: 0xd10
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x18a4
-  __TEXT.__cstring: 0x74ae
-  __TEXT.__objc_classname: 0x15c
-  __TEXT.__objc_methname: 0x39cd
-  __TEXT.__objc_methtype: 0x9bc
+  __TEXT.__gcc_except_tab: 0x1944
+  __TEXT.__cstring: 0x7855
+  __TEXT.__objc_classname: 0x15d
+  __TEXT.__objc_methname: 0x3bcb
+  __TEXT.__objc_methtype: 0x9d6
   __TEXT.__info_plist: 0x549
-  __TEXT.__unwind_info: 0x618
-  __DATA_CONST.__auth_got: 0x658
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0xbb0
-  __DATA_CONST.__cfstring: 0xd20
+  __TEXT.__unwind_info: 0x630
+  __DATA_CONST.__auth_got: 0x660
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0xc00
+  __DATA_CONST.__cfstring: 0xdc0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x1f80
-  __DATA.__objc_selrefs: 0xe68
-  __DATA.__objc_ivar: 0x164
+  __DATA.__objc_const: 0x2000
+  __DATA.__objc_selrefs: 0xee0
+  __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x5a8
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 392
-  Symbols:   289
-  CStrings:  1606
+  Functions: 399
+  Symbols:   294
+  CStrings:  1649
 
Symbols:
+ _CFURLSetResourcePropertyForKey
+ _OBJC_CLASS_$_DAUserAlert
+ _OBJC_CLASS_$_NSRunLoop
+ __kCFURLIsExcludedFromUnencryptedBackupKey
+ _kCFBooleanTrue
+ _strncmp
- _dispatch_main
CStrings:
+ "\x01\x12\x11"
+ "### RemoveDeviceConfirmation %!@(MISSING) success for %!@(MISSING)"
+ "### RemoveDeviceConfirmation create reply failed"
+ "### RemoveDeviceConfirmation[%!@(MISSING)] alert failed: %!@(MISSING)"
+ "### RemoveDeviceConfirmation[%!@(MISSING)] failed: %!@(MISSING)"
+ "### _reportDiscoveredBTDevice app %!@(MISSING) appID: %!@(MISSING) rssi: %!@(MISSING) advData: %!@(MISSING) inDaemonDiscovery %!@(MISSING) inDiscoveryObject %!@(MISSING) config %!@(MISSING)"
+ "### _reportDiscoveredBTDevice rssi: %!@(MISSING) lower than threshold %!d(MISSING), ignoring"
+ "### _runNextTask %!@(MISSING) already paired"
+ "-[DABluetoothPairingManager _addNewTask:completion:bluetoothOp:pairCTKD:showSyncAlert:displayName:]"
+ "-[DABluetoothPairingManager persistBluetoothDevice:pairingRequired:pairWithCTKD:showPrivacySyncAlert:displayName:completion:]"
+ "-[DADaemonXPCConnection _xpcRemoveDeviceAppAccessInfo:]_block_invoke_4"
+ "-[DADaemonXPCConnection _xpcRemoveDeviceConfirmation:accessInfo:userConfirmed:request:]"
+ "-[DADaemonXPCConnection _xpcRemoveDeviceConfirmation:accessInfo:userConfirmed:request:]_block_invoke"
+ "ASK_DISPLAY_NAME"
+ "Accessory"
+ "AlwaysRequireAccessoryRemovalUserConfirmation: %!s(MISSING) -> %!s(MISSING)"
+ "App"
+ "BluetoothDiscoveryRSSIThreshold: %!d(MISSING) -> %!l(MISSING)ld"
+ "Permission denied for current operation"
+ "SSID %!@(MISSING) did not match discovery config's prefix %!@(MISSING) for %!@(MISSING)"
+ "SSID did not match discovery configuration's SSID prefix."
+ "SaveDeviceAppAccessInfo: iTunes backup resource %!@(MISSING), error %!{(MISSING)public}@"
+ "T@\"NSString\",&,N,V_displayName"
+ "TB,R,N"
+ "User canceled device removal"
+ "Waiting for user input for device removal"
+ "_addNewTask:completion:bluetoothOp:pairCTKD:showSyncAlert:displayName:"
+ "_displayName"
+ "_prefAlwaysRequireAccessoryRemovalUserConfirmation"
+ "_prefsBTRSSIThreshold"
+ "_saveAccessoryDevice: iTunes backup resource %!@(MISSING), error %!{(MISSING)public}@"
+ "_xpcRemoveDeviceConfirmation:accessInfo:userConfirmed:request:"
+ "accessoryRemovalAlert:appName:"
+ "activateWithCompletionHandler:"
+ "alwaysConfirmBeforeAccessoryRemoval"
+ "alwaysRequireRemovalConfirm"
+ "appDiscoveryConfiguration"
+ "bluetoothClassicAddress"
+ "bluetoothRSSIThreshold"
+ "bluetoothRange"
+ "bridgingIdentifier"
+ "displayName %!@(MISSING)"
+ "localizedName"
+ "mainRunLoop"
+ "persistBluetoothDevice:pairingRequired:pairWithCTKD:showPrivacySyncAlert:displayName:completion:"
+ "run"
+ "setActionHandler:"
+ "setBluetoothClassicAddress:"
+ "setCustomProperty:value:"
+ "setDisplayName:"
+ "v16@?0@\"NSError\"8"
+ "v16@?0Q8"
+ "v44@0:8@16@24B32@36"
+ "v52@0:8@16B24B28B32@36@?44"
+ "v56@0:8@16@?24q32B40B44@48"
- "\x01\x12"
- "### _reportDiscoveredBTDevice app %!@(MISSING) appID: %!@(MISSING) advData: %!@(MISSING) inDaemonDiscovery %!@(MISSING) inDiscoveryObject %!@(MISSING) config %!@(MISSING)"
- "### _runNextTask persisting  %!@(MISSING)"
- "-[DABluetoothPairingManager _addNewTask:completion:bluetoothOp:pairCTKD:showSyncAlert:]"
- "-[DABluetoothPairingManager persistBluetoothDevice:pairingRequired:pairWithCTKD:showPrivacySyncAlert:completion:]"
- "SSID Prefix did not match discovery configuration's SSID prefix for %!@(MISSING)"
- "SSID Prefix did not match discovery configuration's SSID prefix."
- "SaveDeviceSettings: Updating device state activating -> authorized for %!@(MISSING)"
- "_addNewTask:completion:bluetoothOp:pairCTKD:showSyncAlert:"
- "persistBluetoothDevice:pairingRequired:pairWithCTKD:showPrivacySyncAlert:completion:"
- "v44@0:8@16B24B28B32@?36"
- "v48@0:8@16@?24q32B40B44"

```
