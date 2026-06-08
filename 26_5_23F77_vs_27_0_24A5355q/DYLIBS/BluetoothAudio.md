## BluetoothAudio

> `/System/Library/PrivateFrameworks/BluetoothAudio.framework/BluetoothAudio`

```diff

-195.7.1.2.0
-  __TEXT.__text: 0x8680
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x1d0
+2700.37.0.0.0
+  __TEXT.__text: 0x8324
+  __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x470
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x3e9
-  __TEXT.__oslogstring: 0xa21
+  __TEXT.__cstring: 0x3f9
+  __TEXT.__oslogstring: 0xa83
   __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x9f0
-  __TEXT.__objc_methtype: 0x16c
-  __TEXT.__objc_stubs: 0xcc0
-  __DATA_CONST.__got: 0x228
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x248
+  __DATA_CONST.__got: 0x228
+  __AUTH_CONST.__const: 0x250
   __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x280
-  __DATA.__objc_ivar: 0x28
+  __AUTH_CONST.__objc_const: 0x2b0
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x2c
   __DATA.__bss: 0x1
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0145E84A-69D4-33E0-A9ED-47E7768C5F40
-  Functions: 173
-  Symbols:   709
-  CStrings:  341
+  UUID: 6F0F5A85-3050-3D33-9917-676503A0EC2C
+  Functions: 174
+  Symbols:   720
+  CStrings:  192
 
Symbols:
+ -[BluetoothBridge lecaSessionIDCache]
+ -[BluetoothBridge removeDeviceFromFigE:]
+ -[BluetoothBridge setLecaSessionIDCache:]
+ _OBJC_IVAR_$_BluetoothBridge._lecaSessionIDCache
+ ___31-[BluetoothBridge addListeners]_block_invoke.40
+ ___31-[BluetoothBridge addListeners]_block_invoke.41.cold.1
+ ___block_literal_global.44
+ _endpoint_SetUserRouted.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$lecaSessionID
+ _objc_msgSend$lecaSessionIDCache
+ _objc_msgSend$removeDeviceFromFigE:
+ _objc_msgSend$removeObjectForKey:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- ___31-[BluetoothBridge addListeners]_block_invoke.42
- ___31-[BluetoothBridge addListeners]_block_invoke.42.cold.1
- ___block_literal_global.45
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "DeviceSupportsWirelessSplitting"
+ "Removing LECA device using cached session ID %@"
+ "Set UserRouted failed: device not found for ID %@"
- ".cxx_destruct"
- "2zyzecwSf2ZYRpB3tuQhOQ"
- "@\"CBDiscovery\""
- "@\"CUSystemMonitor\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@16@0:8"
- "@24@0:8@16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B28@0:8C16@20"
- "C24@0:8@16"
- "T@\"CBDiscovery\",&,V_deviceDiscovery"
- "T@\"CUSystemMonitor\",&,V_systemMonitor"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,V_connectedSemaphore"
- "T@?,C,V_activation"
- "T@?,C,V_activationTimeoutBlock"
- "T@?,C,V_lowerScanRate"
- "TB,N,V_noHFPSupport"
- "TB,V_targetUserSession"
- "T^{OpaqueFigEndpointManager=},N,V_manager"
- "^{OpaqueFigEndpointManager=}"
- "^{OpaqueFigEndpointManager=}16@0:8"
- "^{__CFDictionary=}24@0:8@16"
- "_activation"
- "_activationTimeoutBlock"
- "_connectedSemaphore"
- "_deviceDiscovery"
- "_lowerScanRate"
- "_manager"
- "_noHFPSupport"
- "_queue"
- "_systemMonitor"
- "_targetUserSession"
- "activateWithCompletion:"
- "activation"
- "activationTimeoutBlock"
- "addListeners"
- "addressFromDevice:"
- "allKeys"
- "appearanceValue"
- "arrayByAddingObjectsFromArray:"
- "autoAncCapability"
- "batteryLevelCase"
- "batteryLevelLeft"
- "batteryLevelMain"
- "batteryLevelRight"
- "boolForKey:"
- "btAddressData"
- "connectToAddress:completionHandler:"
- "connectedSemaphore"
- "connectedServices"
- "controllerInfoAndReturnError:"
- "conversationDetectCapability"
- "conversationDetectConfig"
- "countByEnumeratingWithState:objects:count:"
- "createDescriptionWithDevice:"
- "deviceDiscovery"
- "deviceFlags"
- "deviceFromIdentifier:"
- "deviceType"
- "devicesWithDiscoveryFlags:error:"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "discoveryFlags"
- "firstUnlocked"
- "gapaFlags"
- "getHFPSupportStatus"
- "identifier"
- "init"
- "invalidate"
- "isConnected:"
- "isDeviceSupportedWithType:VIDsrc:VID:PID:"
- "isEqual:"
- "isEqualToString:"
- "isEquivalentToCBDevice:compareFlags:"
- "isHALPublished:device:"
- "listeningMode"
- "lowerScanRate"
- "manager"
- "modifyDevice:settings:completion:"
- "name"
- "nameFromDevice:"
- "noHFPSupport"
- "numberWithBool:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedShort:"
- "objectForKeyedSubscript:"
- "primaryPlacement"
- "productID"
- "proximityPairingPrimaryPlacement"
- "proximityPairingSecondaryPlacement"
- "queue"
- "secondaryPlacement"
- "setActivation:"
- "setActivationTimeoutBlock:"
- "setAudioRouteHidden:"
- "setBleRSSIThresholdHint:"
- "setBleScanRate:"
- "setConnectedSemaphore:"
- "setConnectionFlags:"
- "setConversationDetectConfig:"
- "setDeviceDiscovery:"
- "setDeviceFlagsMask:"
- "setDeviceFlagsValue:"
- "setDeviceFoundHandler:"
- "setDeviceLostHandler:"
- "setDiscoveryFlags:"
- "setDispatchQueue:"
- "setFirstUnlockHandler:"
- "setIdentifier:"
- "setListeningMode:"
- "setLowerScanRate:"
- "setManager:"
- "setNoHFPSupport:"
- "setObject:forKey:"
- "setPeerDevice:"
- "setQueue:"
- "setServiceFlags:"
- "setSpatialAudioAllowed:"
- "setSpatialAudioMode:"
- "setSystemMonitor:"
- "setTargetUserSession:"
- "sharedBluetoothBridge"
- "shouldRemoveDevice:"
- "smartRoutingMode"
- "spatialAudioMode"
- "standardUserDefaults"
- "startLEScanning:"
- "stopLEScanning"
- "stringWithFormat:"
- "supportedFormats:"
- "supportedServices"
- "systemMonitor"
- "targetUserSession"
- "uidFromDevice:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8^{OpaqueFigEndpointManager=}16"
- "v32@0:8@16@?24"
- "vendorID"
- "vendorIDSource"

```
