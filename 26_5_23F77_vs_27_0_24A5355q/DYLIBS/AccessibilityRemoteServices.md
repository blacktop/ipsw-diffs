## AccessibilityRemoteServices

> `/System/Library/PrivateFrameworks/AccessibilityRemoteServices.framework/AccessibilityRemoteServices`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x4ba8
-  __TEXT.__auth_stubs: 0x3d0
+3229.1.6.0.0
+  __TEXT.__text: 0x4bb8
   __TEXT.__objc_methlist: 0x2e0
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__cstring: 0xd54
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x17c
+  __TEXT.__cstring: 0xd61
   __TEXT.__oslogstring: 0x30a
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0xcf0
-  __TEXT.__objc_methtype: 0x21a
-  __TEXT.__objc_stubs: 0xbe0
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x558
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0xd0
   __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0xfc0
   __AUTH_CONST.__objc_const: 0x6e0
   __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x54
   __DATA.__bss: 0x40

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
-  - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7701E391-2F68-30E0-A197-6973B1594C23
-  Functions: 118
-  Symbols:   581
-  CStrings:  484
+  UUID: 3951FA2E-709C-3BD7-ABB6-E2CE60940774
+  Functions: 105
+  Symbols:   559
+  CStrings:  300
 
Symbols:
+ GCC_except_table100
+ GCC_except_table15
+ GCC_except_table27
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table75
+ ___block_literal_global.232
+ ___block_literal_global.57
+ ___block_literal_global.82
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
- +[AXRDeviceDiscoveryManager sharedInstance].cold.1
- GCC_except_table0
- GCC_except_table12
- GCC_except_table16
- GCC_except_table2
- GCC_except_table6
- GCC_except_table9
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- __AXRBundle.cold.1
- ___45-[AXRemoteReceiver initWithEventID:delegate:]_block_invoke.5.cold.1
- ___45-[AXRemoteReceiver initWithEventID:delegate:]_block_invoke.7.cold.1
- ___65-[AXRemoteDevice sendPayload:withEventID:withTimeout:completion:]_block_invoke.cold.1
- _ax_remote_connection_log.cold.1
- _ax_remote_daemon_log.cold.1
- _ax_remote_event_log.cold.1
- _ax_remote_general_log.cold.1
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[AXRDeviceDiscoveryManager cachedDiscoveredDevices] : 256 -> 260
~ ___52-[AXRDeviceDiscoveryManager cachedDiscoveredDevices]_block_invoke : 104 -> 100
~ -[AXRDeviceDiscoveryManager _enumerateObservers:] : 312 -> 324
~ -[AXRDeviceDiscoveryManager _init] : 904 -> 856
~ ___34-[AXRDeviceDiscoveryManager _init]_block_invoke : 108 -> 148
~ ___34-[AXRDeviceDiscoveryManager _init]_block_invoke.15 : 108 -> 148
~ ___34-[AXRDeviceDiscoveryManager _init]_block_invoke.18 : 108 -> 148
~ ___34-[AXRDeviceDiscoveryManager _init]_block_invoke.21 : 1584 -> 1716
~ ___34-[AXRDeviceDiscoveryManager _init]_block_invoke.29 : 88 -> 84
~ ___34-[AXRDeviceDiscoveryManager _init]_block_invoke_2 : 360 -> 364
~ ___34-[AXRDeviceDiscoveryManager _init]_block_invoke.31 : 88 -> 84
~ ___34-[AXRDeviceDiscoveryManager _init]_block_invoke_2.32 : 176 -> 172
~ -[AXRDeviceDiscoveryManager mineDevices] : 88 -> 80
~ ___67-[AXRDeviceDiscoveryManager _indexOfDeviceWithEffectiveIdentifier:]_block_invoke : 76 -> 72
~ -[AXRDeviceDiscoveryManager _discoveredDevicesChanged] : 160 -> 156
~ ___54-[AXRDeviceDiscoveryManager _discoveredDevicesChanged]_block_invoke : 140 -> 144
~ -[AXRDeviceDiscoveryManager setCompanionLinkClient:] : 64 -> 12
~ -[AXRDeviceDiscoveryManager setDiscoveredDevices:] : 64 -> 12
~ -[AXRDeviceDiscoveryManager setService:] : 64 -> 12
~ _AXRDeviceRemoteActionsForCurrentDevice : 192 -> 240
~ _AXRDeviceRemoteActionsForMediaForCurrentDevice : 168 -> 164
~ _AXRDeviceRemoteActionsForSwitchControlForCurrentDevice : 188 -> 184
~ _AXRDeviceRemoteActionsForVoiceOverForCurrentDevice : 228 -> 224
~ _AXRDevicePreferredRemoteActionsForCurrentDevice : 228 -> 412
~ _AXRDeviceRemoteActionsPayloadForCurrentDevice : 736 -> 1020
~ _AXRLocalizedStringForRemoteAction : 88 -> 84
~ _AXRLocalizedStringForRemoteActionWithDeviceType : 1084 -> 1072
~ _AXRLocalizedSectionTitleForPreferredContextType : 88 -> 124
~ -[AXRDeviceRemoteActionSectionContainer initWithLocalizedTitle:preferredContextType:remoteActions:] : 152 -> 160
~ -[AXRemoteDevice displayName] : 116 -> 96
~ -[AXRemoteDevice identifier] : 84 -> 76
~ -[AXRemoteDevice remoteActionsForPreferredContextType:] : 384 -> 388
~ -[AXRemoteDevice customizedRemoteActionForHandGestureEventUsage:] : 152 -> 128
~ -[AXRemoteDevice _setRemoteAction:forHandGestureEventUsage:] : 360 -> 332
~ -[AXRemoteDevice connectIfNecessary:] : 584 -> 576
~ ___37-[AXRemoteDevice connectIfNecessary:]_block_invoke : 236 -> 220
~ ___37-[AXRemoteDevice connectIfNecessary:]_block_invoke_2 : 124 -> 120
~ ___37-[AXRemoteDevice connectIfNecessary:]_block_invoke_3 : 724 -> 716
~ ___37-[AXRemoteDevice connectIfNecessary:]_block_invoke.6 : 1288 -> 1304
~ -[AXRemoteDevice _deviceName] : 88 -> 96
~ -[AXRemoteDevice disconnect] : 404 -> 384
~ ___28-[AXRemoteDevice disconnect]_block_invoke : 176 -> 172
~ -[AXRemoteDevice sendPayload:withEventID:withTimeout:completion:] : 464 -> 472
~ ___65-[AXRemoteDevice sendPayload:withEventID:withTimeout:completion:]_block_invoke : 520 -> 580
~ ___65-[AXRemoteDevice sendPayload:withEventID:withTimeout:completion:]_block_invoke.20 : 212 -> 208
~ -[AXRemoteDevice setDeviceRemoteActions:] : 64 -> 12
~ -[AXRemoteDevice setDeviceGestureCustomizations:] : 64 -> 12
~ -[AXRemoteDevice setDevice:] : 64 -> 12
~ -[AXRemoteDevice setDeviceLinkClient:] : 64 -> 12
~ ___ax_remote_general_log_block_invoke : 136 -> 132
~ ___ax_remote_connection_log_block_invoke : 136 -> 132
~ ___ax_remote_daemon_log_block_invoke : 136 -> 132
~ ___ax_remote_event_log_block_invoke : 136 -> 132
~ ____AXRBundle_block_invoke : 96 -> 92
~ _AXRLocalizedStringForKey : 88 -> 84
~ _AXRLocalizedStringForKeyWithDeviceType : 252 -> 300
~ -[AXRemoteReceiver initWithEventID:delegate:] : 956 -> 920
~ ___45-[AXRemoteReceiver initWithEventID:delegate:]_block_invoke : 184 -> 220
~ ___45-[AXRemoteReceiver initWithEventID:delegate:]_block_invoke.3 : 256 -> 248
~ ___45-[AXRemoteReceiver initWithEventID:delegate:]_block_invoke.5 : 196 -> 292
~ ___45-[AXRemoteReceiver initWithEventID:delegate:]_block_invoke.7 : 388 -> 460
~ -[AXRemoteReceiver setCompanionLinkClient:] : 64 -> 12
CStrings:
- ".cxx_destruct"
- "@\"<AXRemoteDeviceConnectionDelegate>\""
- "@\"<AXRemoteReceiverDelegate>\""
- "@\"IDSService\""
- "@\"NSArray\""
- "@\"NSHashTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"RPCompanionLinkClient\""
- "@\"RPCompanionLinkDevice\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8@16@24"
- "@40@0:8@16q24@32"
- "AXRDeviceDiscoveryManager"
- "AXRDeviceRemoteActionSectionContainer"
- "AXRemoteDevice"
- "AXRemoteReceiver"
- "B"
- "B16@0:8"
- "Q24@0:8@16"
- "T@\"<AXRemoteDeviceConnectionDelegate>\",W,N,V_connectionDelegate"
- "T@\"<AXRemoteReceiverDelegate>\",W,N,V_delegate"
- "T@\"IDSService\",&,N,V_service"
- "T@\"NSArray\",&,N,V_deviceRemoteActions"
- "T@\"NSArray\",R,N,V_remoteActions"
- "T@\"NSMutableArray\",&,N,V_discoveredDevices"
- "T@\"NSMutableDictionary\",&,N,V_deviceGestureCustomizations"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_localizedTitle"
- "T@\"RPCompanionLinkClient\",&,N,V_companionLinkClient"
- "T@\"RPCompanionLinkClient\",&,N,V_deviceLinkClient"
- "T@\"RPCompanionLinkDevice\",&,N,V_device"
- "TB,N,V_connected"
- "Tq,N,V_contextType"
- "Tq,N,V_deviceType"
- "Tq,R,N,V_preferredContextType"
- "T{os_unfair_lock_s=I},N,V_devicesLock"
- "UTF8String"
- "_AXRClassForBundle"
- "_companionLinkClient"
- "_connected"
- "_connectionDelegate"
- "_contextType"
- "_delegate"
- "_device"
- "_deviceGestureCustomizations"
- "_deviceLinkClient"
- "_deviceName"
- "_deviceQueue"
- "_deviceRemoteActions"
- "_deviceType"
- "_devicesLock"
- "_discoveredDevices"
- "_discoveredDevicesChanged"
- "_enumerateObservers:"
- "_indexOfDeviceWithEffectiveIdentifier:"
- "_init"
- "_localizedTitle"
- "_observers"
- "_observersLock"
- "_preferredContextType"
- "_queue"
- "_remoteActions"
- "_service"
- "_setRemoteAction:forHandGestureEventUsage:"
- "activateWithCompletion:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObserver:"
- "allObjects"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "boolValue"
- "bundleForClass:"
- "cachedDiscoveredDevices"
- "companionLinkClient"
- "componentsSeparatedByString:"
- "connectIfNecessary:"
- "connected"
- "connectionDelegate"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "customizedRemoteActionForHandGestureEventUsage:"
- "delegate"
- "device"
- "deviceDiscoveryManager:updatedDevices:"
- "deviceGestureCustomizations"
- "deviceLinkClient"
- "deviceRemoteActions"
- "devicesLock"
- "dictionaryWithObjects:forKeys:count:"
- "disconnect"
- "discoveredDevices"
- "displayName"
- "effectiveIdentifier"
- "identifier"
- "idsDeviceIdentifier"
- "indexOfObjectPassingTest:"
- "init"
- "initWithDevice:"
- "initWithEventID:delegate:"
- "initWithLocalizedTitle:preferredContextType:remoteActions:"
- "initWithService:"
- "integerValue"
- "invalidate"
- "isEqualToString:"
- "linkedDevicesWithRelationship:"
- "localizedStringForKey:value:table:"
- "localizedTitle"
- "mineDevices"
- "name"
- "numberWithDouble:"
- "numberWithUnsignedChar:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "proximity"
- "q16@0:8"
- "registerEventID:options:handler:"
- "registerRequestID:options:handler:"
- "remoteActionsForPreferredContextType:"
- "remoteDeviceDidUnexpectedlyDisconnect:"
- "remoteReceiver:connectingDevice:setupConnection:withOptions:"
- "remoteReceiver:didActivateWithError:"
- "remoteReceiver:didReceivePayload:withOptions:"
- "remoteReceiverDidDisconnect:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObserver:"
- "sendEventID:event:destinationID:options:completion:"
- "sendPayload:withEventID:"
- "sendPayload:withEventID:withTimeout:completion:"
- "sendRequestID:request:options:responseHandler:"
- "service"
- "setAppID:"
- "setCompanionLinkClient:"
- "setConnected:"
- "setConnectionDelegate:"
- "setContextType:"
- "setControlFlags:"
- "setDelegate:"
- "setDestinationDevice:"
- "setDevice:"
- "setDeviceFoundHandler:"
- "setDeviceGestureCustomizations:"
- "setDeviceLinkClient:"
- "setDeviceLostHandler:"
- "setDeviceRemoteActions:"
- "setDeviceType:"
- "setDevicesLock:"
- "setDisconnectHandler:"
- "setDiscoveredDevices:"
- "setDispatchQueue:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setObject:forKeyedSubscript:"
- "setService:"
- "setServiceType:"
- "sharedInstance"
- "sourceVersion"
- "stringByAppendingString:"
- "stringWithFormat:"
- "uniqueIDOverride"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v48@0:8@16@24d32@?40"
- "weakObjectsHashTable"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
