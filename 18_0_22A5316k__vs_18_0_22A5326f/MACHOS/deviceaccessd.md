## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-304.24.2.1.0
-  __TEXT.__text: 0x23318
+304.26.2.0.0
+  __TEXT.__text: 0x249d0
   __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_stubs: 0x35c0
-  __TEXT.__objc_methlist: 0xd10
+  __TEXT.__objc_stubs: 0x36e0
+  __TEXT.__objc_methlist: 0xd50
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x1944
-  __TEXT.__cstring: 0x7855
+  __TEXT.__gcc_except_tab: 0x196c
+  __TEXT.__cstring: 0x802a
   __TEXT.__objc_classname: 0x15d
-  __TEXT.__objc_methname: 0x3bcb
-  __TEXT.__objc_methtype: 0x9d6
+  __TEXT.__objc_methname: 0x3d22
+  __TEXT.__objc_methtype: 0xa07
   __TEXT.__info_plist: 0x549
-  __TEXT.__unwind_info: 0x630
+  __TEXT.__unwind_info: 0x650
   __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0xc00
-  __DATA_CONST.__cfstring: 0xdc0
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0xc98
+  __DATA_CONST.__cfstring: 0xe20
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x2000
-  __DATA.__objc_selrefs: 0xee0
-  __DATA.__objc_ivar: 0x170
+  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA.__objc_const: 0x2090
+  __DATA.__objc_selrefs: 0xf20
+  __DATA.__objc_ivar: 0x180
   __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x5a8
-  __DATA.__bss: 0x18
+  __DATA.__data: 0x5b0
+  __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 399
-  Symbols:   294
-  CStrings:  1649
+  Functions: 412
+  Symbols:   295
+  CStrings:  1706
 
Symbols:
+ _kTCCResetSyncAuth
+ _os_transaction_create
- _objc_release_x2
CStrings:
+ "\x01\x11\x13"
+ "\x02\x11\x12\x13\xfa\x13"
+ "### Buddy - %!s(MISSING)"
+ "### Cannot validate cache yet, device in buddy"
+ "### Connected to %!@(MISSING) letting app take it from here"
+ "### Invalidate devices waiting for app approval when UI is dismissed %!@(MISSING), %!@(MISSING), %!@(MISSING)"
+ "### ModifyAccessoryDevice, Using containerized path %!s(MISSING)"
+ "### Remove all devices and AppAccess"
+ "### Remove all devices and AppAccess directory, using containerized path %!s(MISSING)"
+ "### Removed-AllDevicesAndAppAccess %!@(MISSING), %!@(MISSING)"
+ "### Removing all access for device: %!@(MISSING)"
+ "### SaveAccessoryDevice, Using containerized path %!s(MISSING)"
+ "### SaveDeviceAppAccessInfo, using containerized path %!s(MISSING)"
+ "### _persistBluetoothDevice BT pairing manager event %!@(MISSING) %!@(MISSING) %!@(MISSING) %!@(MISSING)"
+ "### _persistBluetoothDevice app %!@(MISSING) device %!@(MISSING) inRequirePairing:%!d(MISSING) inPairCTKD:%!d(MISSING)"
+ "### _reportEvent event %!@(MISSING) _currentTaskEndEvent %!@(MISSING) errorcode %!@(MISSING) endTask %!s(MISSING) %!@(MISSING)"
+ "### cancelCurrentTask cbManager %!@(MISSING) tasks %!@(MISSING)"
+ "### cancelCurrentTask no more tasks"
+ "### cancelCurrentTask task cancelled %!@(MISSING)"
+ "### device did not require pairing, but its pairing. Aborting"
+ "### modifyAccessoryDevice CBPeripheral %!@(MISSING)"
+ "### modifyAccessoryDevice CBPeripheral %!@(MISSING) setting bridging property %!@(MISSING)"
+ "### runMigrationWithDiscovery CBPeripheral to migrate:  %!@(MISSING)"
+ "### runMigrationWithDiscovery centralManager Off to migrate: %!l(MISSING)d for %!@(MISSING)"
+ "### runMigrationWithDiscovery single centralManager Off to migrate: %!l(MISSING)d"
+ "%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING)"
+ "-[DABluetoothPairingManager _addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:]"
+ "-[DABluetoothPairingManager _reportEvent:error:endCurrentTask:]"
+ "-[DABluetoothPairingManager cancelCurrentTask]"
+ "-[DABluetoothPairingManager cancelCurrentTask]_block_invoke"
+ "-[DABluetoothPairingManager persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:completion:]"
+ "-[DADaemonServer _activate]"
+ "-[DADaemonServer _activate]_block_invoke_3"
+ "-[DADaemonServer _activate]_block_invoke_7"
+ "-[DADaemonServer _persistBluetoothDevice:device:requirePairing:pairWithCTKD:]"
+ "-[DADaemonServer _persistBluetoothDevice:device:requirePairing:pairWithCTKD:]_block_invoke"
+ "-[DADaemonServer _removeAllDevicesAndAppAccess]"
+ "-[DADaemonServer _removeAllDevicesAndAppAccess]_block_invoke"
+ "-[DADaemonServer _removeAllDevicesAndAppAccess]_block_invoke_2"
+ "-[DADaemonServer removeDiscovery:]_block_invoke_2"
+ "/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"
+ "@\"NSNumber\""
+ "@\"NSObject<OS_os_transaction>\""
+ "ASK_RELATED_RADIO_ADDRESS"
+ "BYSetupAssistantNeedsToRun"
+ "BluetoothTransportBridgingTimeoutSeconds: %!f(MISSING) -> %!f(MISSING)"
+ "Clearing All permissions and resetting database"
+ "DABluetoothEventAccessoryConnected"
+ "DAPrefKeyBluetoothTransportBridgingTimeoutSeconds"
+ "Device supports pairing but was not paired"
+ "Global session requires private entitlement"
+ "Listen for Privacy Reset"
+ "Reset All: Library folder not found"
+ "T@\"NSNumber\",&,N,V_taskTimeout"
+ "TB,N,V_appConfirmsAuth"
+ "_addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:"
+ "_appConfirmsAuth"
+ "_checkAppAccessInfoExpired: found CBPeripheral, %!@(MISSING) awaitingTransportBridging %!d(MISSING)"
+ "_currentTaskEndEvent"
+ "_expiredDeviceChecktransaction"
+ "_persistBluetoothDevice:device:requirePairing:pairWithCTKD:"
+ "_prefsBluetoothTransportBridgingTimeoutSeconds"
+ "_removeAllDevicesAndAppAccess"
+ "_reportEvent:error:endCurrentTask:"
+ "_resetPrivacySettingsToken"
+ "_taskTimeout"
+ "appConfirmsAuth"
+ "appConfirmsAuth %!d(MISSING)"
+ "cancelCurrentTask"
+ "cancelCurrentTask pending task %!@(MISSING)"
+ "com.apple.Preferences.ResetPrivacyWarningsNotification"
+ "com.apple.accessorysetupkit.expireddevicecheck"
+ "customProperty:"
+ "getCurrentTaskBluetoothIdentifier"
+ "initWithBluetoothIdentifier:pairedCTKD:appConfirmsAuth:pairingRequired:"
+ "initWithMigration:"
+ "pairingRequired"
+ "persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:completion:"
+ "setAppConfirmsAuth:"
+ "setTaskTimeout:"
+ "taskTimeout"
+ "taskTimeout %!@(MISSING) seconds"
+ "v32@?0@\"NSString\"8@\"DADevice\"16^B24"
+ "v36@0:8q16@24B32"
+ "v40@0:8@16@24B32B36"
+ "v60@0:8@16B24B28@32@40B48@?52"
+ "v64@0:8@16@?24q32B40@44@52B60"
- "\x01\x12\x11"
- "\x02\x11\x12\x13\xd9\x13"
- "### _persistBluetoothDevice BT pairing manager event %!@(MISSING) %!@(MISSING) %!@(MISSING)"
- "### _persistBluetoothDevice app %!@(MISSING) device %!@(MISSING) inRequirePairing:%!d(MISSING) inPairCTKD:%!d(MISSING) inShowPrivacySyncAlert:%!d(MISSING)"
- "### _reportEvent event %!@(MISSING) lastReportedEvent %!@(MISSING) errorcode %!@(MISSING) %!@(MISSING)"
- "### runMigrationWithDiscovery CBPeriperal to migrate:  %!@(MISSING)"
- "### runMigrationWithDiscovery Cannot since app already onboarded accessories"
- "-[DABluetoothPairingManager _addNewTask:completion:bluetoothOp:pairCTKD:showSyncAlert:displayName:]"
- "-[DABluetoothPairingManager _reportEvent:error:]"
- "-[DABluetoothPairingManager persistBluetoothDevice:pairingRequired:pairWithCTKD:showPrivacySyncAlert:displayName:completion:]"
- "-[DADaemonServer _activate]_block_invoke_6"
- "-[DADaemonServer _persistBluetoothDevice:device:requirePairing:pairWithCTKD:showPrivacySyncAlert:]"
- "-[DADaemonServer _persistBluetoothDevice:device:requirePairing:pairWithCTKD:showPrivacySyncAlert:]_block_invoke"
- "PrivacySyncAlert %!d(MISSING)"
- "TB,N,V_showPrivacySyncAlert"
- "Using containerized path %!s(MISSING)"
- "_PENDING_PRIVACY_SYNC_POPUP_"
- "_addNewTask:completion:bluetoothOp:pairCTKD:showSyncAlert:displayName:"
- "_persistBluetoothDevice:device:requirePairing:pairWithCTKD:showPrivacySyncAlert:"
- "_reportEvent:error:"
- "_reportedEvent"
- "_showPrivacySyncAlert"
- "initWithBluetoothIdentifier:pairedCTKD:"
- "persistBluetoothDevice:pairingRequired:pairWithCTKD:showPrivacySyncAlert:displayName:completion:"
- "setShowPrivacySyncAlert:"
- "showPrivacySyncAlert"
- "v32@0:8q16@24"
- "v44@0:8@16@24B32B36B40"
- "v52@0:8@16B24B28B32@36@?44"
- "v56@0:8@16@?24q32B40B44@48"

```
